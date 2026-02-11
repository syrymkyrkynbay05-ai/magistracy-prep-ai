import os
import sys
import uuid
import json
import random

# Add backend directory to path for imports when running from project root
backend_dir = os.path.dirname(os.path.abspath(__file__))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import unquote

from models import (
    DBQuestion,
    DBOption,
    DBSubject,
    Question,
    Option,
    SubjectId,
    QuestionType,
    CalculateRequest,
    TestResult,
    DBTestResult,
)
from database import get_db, engine, Base
from auth import DBUser, get_current_user  # Ensure users table is created
from auth_routes import router as auth_router

load_dotenv()

# Initialize database tables (including users)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Magistracy Prep AI Backend")

# Register auth routes
app.include_router(auth_router)

# Enable CORS for the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files from dist folder
project_root = Path(__file__).parent.parent
dist_folder = project_root / "dist"


class GenerateRequest(BaseModel):
    subject_id: SubjectId
    count: int = 5


@app.get("/health")
async def health():
    """Health check endpoint for Railway"""
    return {"status": "healthy"}


@app.post("/generate", response_model=List[Question])
async def generate_questions(
    request: GenerateRequest,
    db: Session = Depends(get_db),
    current_user: DBUser = Depends(get_current_user),
):
    """
    Generate questions for a subject.
    For English (KT format): 16 listening + 18 grammar + 16 reading = 50 questions
    """

    # For English subject: 16 Listening (DB) + 18 Grammar (DB) + 16 Reading (DB)
    if request.subject_id == SubjectId.ENGLISH:
        # Convert DBQuestion -> API Question
        def to_api_question(db_q: DBQuestion) -> Question:
            options = [Option(id=opt.id, text=opt.text) for opt in db_q.options]
            correct_ids = (
                db_q.correct_option_ids.split(",") if db_q.correct_option_ids else []
            )

            # Handle Audio URL stored in reading_passage
            audio_url = None
            reading_passage = (
                db_q.reading_passage if hasattr(db_q, "reading_passage") else None
            )

            # Parse AUDIO: prefix
            if reading_passage and reading_passage.startswith("AUDIO:"):
                audio_url = reading_passage.replace("AUDIO:", "").strip()
                reading_passage = None  # Clear passage since it's just a URL holder

            return Question(
                id=db_q.id,
                subjectId=request.subject_id,
                text=db_q.text,
                codeSnippet=db_q.code_snippet,
                readingPassage=reading_passage,
                audioUrl=audio_url,
                options=options,
                correctOptionIds=correct_ids,
                type=db_q.type,
                topic=db_q.topic or "General",
                difficulty=db_q.difficulty or "medium",
                languageLevel=(
                    db_q.language_level if hasattr(db_q, "language_level") else None
                ),
                hint=db_q.hint,
            )

        # 1) Listening questions (1-16): 2 audio texts × 8 questions each
        # Group questions by their audio file
        all_listening = (
            db.query(DBQuestion)
            .filter(DBQuestion.subject_id == request.subject_id.value)
            .filter(DBQuestion.topic.ilike("%listening%"))
            .filter(DBQuestion.reading_passage.like("AUDIO:%"))  # Only with audio URL
            .all()
        )

        # Group by audio file (reading_passage contains "AUDIO:/english/filename.mp3")
        audio_groups: dict[str, list] = {}
        for q in all_listening:
            audio_key = q.reading_passage if q.reading_passage else "unknown"
            if audio_key not in audio_groups:
                audio_groups[audio_key] = []
            audio_groups[audio_key].append(q)

        # Get list of audio files that have exactly 8 questions
        valid_audio_keys = [k for k, v in audio_groups.items() if len(v) >= 8]

        # Randomly select 2 audio texts for this test
        random.shuffle(valid_audio_keys)
        selected_audio_keys = valid_audio_keys[:2]  # Pick 2 audios

        listening_questions = []
        for audio_key in selected_audio_keys:
            group_questions = audio_groups[audio_key][:8]  # Take 8 questions

            # Shuffle question order within the group
            random.shuffle(group_questions)

            # Convert to API questions with shuffled options
            for db_q in group_questions:
                api_q = to_api_question(db_q)

                # Shuffle options order
                if api_q.options and len(api_q.options) > 1:
                    # Create mapping of old_id -> new shuffled position
                    shuffled_options = api_q.options.copy()
                    random.shuffle(shuffled_options)
                    api_q.options = shuffled_options

                listening_questions.append(api_q)

        # 2) Grammar/Vocabulary questions (17-34): take from DB excluding listening/reading
        grammar_qs = (
            db.query(DBQuestion)
            .filter(DBQuestion.subject_id == request.subject_id.value)
            .filter(~DBQuestion.topic.ilike("%listening%"))
            .filter(~DBQuestion.topic.ilike("%audio%"))
            .filter(~DBQuestion.topic.ilike("%reading%"))
            .order_by(func.random())
            .limit(18)
            .all()
        )

        # 3) Reading questions (35-50): 2 reading texts × 8 questions each
        # Group questions by their reading passage
        all_reading = (
            db.query(DBQuestion)
            .filter(DBQuestion.subject_id == request.subject_id.value)
            .filter(DBQuestion.topic.ilike("%reading%"))
            .filter(DBQuestion.reading_passage.isnot(None))
            .filter(DBQuestion.reading_passage != "")
            .all()
        )

        # Group by reading passage
        reading_groups: dict[str, list] = {}
        for q in all_reading:
            passage_key = q.reading_passage if q.reading_passage else "unknown"
            if passage_key not in reading_groups:
                reading_groups[passage_key] = []
            reading_groups[passage_key].append(q)

        # Get list of passages that have at least 8 questions
        valid_passage_keys = [k for k, v in reading_groups.items() if len(v) >= 8]

        # Randomly select 2 reading texts for this test
        random.shuffle(valid_passage_keys)
        selected_passage_keys = valid_passage_keys[:2]  # Pick 2 passages

        reading_questions = []
        for passage_key in selected_passage_keys:
            group_questions = reading_groups[passage_key][:8]  # Take 8 questions

            # Shuffle question order within the group
            random.shuffle(group_questions)

            # Convert to API questions with shuffled options
            for db_q in group_questions:
                api_q = to_api_question(db_q)

                # Shuffle options order (but correctOptionIds stay the same - they reference by ID)
                if api_q.options and len(api_q.options) > 1:
                    shuffled_options = api_q.options.copy()
                    random.shuffle(shuffled_options)
                    api_q.options = shuffled_options

                reading_questions.append(api_q)

        questions = (
            listening_questions
            + [to_api_question(q) for q in grammar_qs]
            + reading_questions
        )

        # If requested count is bigger (or DB pools are short), fill with random non-duplicate DB questions
        if len(questions) < request.count:
            existing_ids = {q.id for q in questions}
            additional = (
                db.query(DBQuestion)
                .filter(DBQuestion.subject_id == request.subject_id.value)
                .filter(~DBQuestion.id.in_(existing_ids) if existing_ids else True)
                .order_by(func.random())
                .limit(request.count - len(questions))
                .all()
            )
            questions.extend([to_api_question(q) for q in additional])

        return questions[: request.count]
    else:
        # For other subjects, use random selection
        db_questions = (
            db.query(DBQuestion)
            .filter(DBQuestion.subject_id == request.subject_id.value)
            .order_by(func.random())
            .limit(request.count)
            .all()
        )

    if not db_questions:
        raise HTTPException(
            status_code=404,
            detail=f"No questions found in database for {request.subject_id}. Please run seed_db.py first.",
        )

    questions = []
    for db_q in db_questions:
        options = [Option(id=opt.id, text=opt.text) for opt in db_q.options]
        correct_ids = (
            db_q.correct_option_ids.split(",") if db_q.correct_option_ids else []
        )

        questions.append(
            Question(
                id=db_q.id,
                subjectId=request.subject_id,
                text=db_q.text,
                codeSnippet=db_q.code_snippet,
                readingPassage=(
                    db_q.reading_passage if hasattr(db_q, "reading_passage") else None
                ),
                options=options,
                correctOptionIds=correct_ids,
                type=db_q.type,
                topic=db_q.topic or "General",
                difficulty=db_q.difficulty or "medium",
                languageLevel=(
                    db_q.language_level if hasattr(db_q, "language_level") else None
                ),
                hint=db_q.hint,
            )
        )

    return questions


@app.get("/syllabus/{subject_id}")
async def get_syllabus(subject_id: str):
    # Map subject_id to filenames
    mapping = {
        "english": "Ағылшын.md",
        "tgo": "ОДАТ.md",
        "algo": "Алгоритмдер.md",
        "db": "Дерекқорлар.md",
        "info": "info.md",
    }

    filename = mapping.get(subject_id)
    if not filename:
        raise HTTPException(status_code=404, detail="Syllabus not found")

    file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "Markdown", filename
    )

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"File {filename} not found")

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    return {"content": content}


@app.post("/calculate", response_model=TestResult)
async def calculate_results(
    request: CalculateRequest,
    current_user: DBUser = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # Calculation logic
    total_score = 0
    total_max_score = 0
    correct_count = 0

    subject_scores = {
        SubjectId.ENGLISH: {"score": 0, "max": 0},
        SubjectId.TGO: {"score": 0, "max": 0},
        SubjectId.ALGO: {"score": 0, "max": 0},
        SubjectId.DB: {"score": 0, "max": 0},
    }

    for q in request.questions:
        user_selected_ids = request.answers.get(q.id, [])

        q_points = 0
        q_max_points = 1

        if q.type == QuestionType.SINGLE:
            q_max_points = 1
            if (
                len(user_selected_ids) == 1
                and user_selected_ids[0] in q.correctOptionIds
            ):
                q_points = 1
                correct_count += 1
        else:
            q_max_points = 2
            is_exact_match = len(user_selected_ids) == len(q.correctOptionIds) and all(
                id in q.correctOptionIds for id in user_selected_ids
            )
            if is_exact_match:
                q_points = 2
                correct_count += 1

        total_score += q_points
        total_max_score += q_max_points

        if q.subjectId in subject_scores:
            subject_scores[q.subjectId]["score"] += q_points
            subject_scores[q.subjectId]["max"] += q_max_points

    # Save to database
    test_result = DBTestResult(
        user_id=current_user.id,
        total_score=total_score,
        max_score=total_max_score,
        subject_scores=json.dumps(subject_scores),
        correct_count=correct_count,
        total_questions=len(request.questions),
    )
    db.add(test_result)
    db.commit()

    return TestResult(
        totalScore=total_score,
        maxScore=total_max_score,
        subjectScores=subject_scores,
        correctCount=correct_count,
        totalQuestions=len(request.questions),
    )


# Mount static files for React assets (CSS, JS, images)
if dist_folder.exists():
    app.mount("/assets", StaticFiles(directory=dist_folder / "assets"), name="assets")
    if (dist_folder / "audio").exists():
        app.mount("/audio", StaticFiles(directory=dist_folder / "audio"), name="audio")
    if (dist_folder / "images").exists():
        app.mount(
            "/images", StaticFiles(directory=dist_folder / "images"), name="images"
        )
    # Serve english audio files from dist (after npm run build)
    if (dist_folder / "english").exists():
        app.mount(
            "/english",
            StaticFiles(directory=dist_folder / "english"),
            name="english_dist",
        )

# Mount public folder for development (audio files are in public/english)
public_folder = project_root / "public"
if public_folder.exists() and (public_folder / "english").exists():
    # Only mount if not already mounted from dist
    if not (dist_folder.exists() and (dist_folder / "english").exists()):
        app.mount(
            "/english",
            StaticFiles(directory=public_folder / "english"),
            name="english_public",
        )


# SPA fallback via 404 handler (allows /docs, /redoc to work)
from starlette.responses import JSONResponse


@app.exception_handler(404)
async def spa_fallback(request, exc):
    """
    Improved SPA fallback:
    1. Try to serve the exact file from 'dist' (e.g., logos, favicons).
    2. If not found and is a GET request, serve 'index.html'.
    3. Otherwise return 404 JSON.
    """
    if request.method == "GET":
        path = unquote(request.url.path.lstrip("/"))

        # 1. Check if the file exists in dist (for logos, favicons, etc. at root)
        if dist_folder.exists() and path:
            potential_file = dist_folder / path
            if potential_file.exists() and potential_file.is_file():
                return FileResponse(potential_file)

        # 2. SPA Fallback for non-API routes
        api_prefixes = (
            "api/",
            "generate",
            "submit",
            "calculate",
            "file/",
            "english/",
            "assets/",
            "audio/",
            "images/",
            "auth/",
        )
        if not any(path.startswith(p) for p in api_prefixes):
            index_file = dist_folder / "index.html"
            if index_file.exists():
                return FileResponse(index_file)

    return JSONResponse(status_code=404, content={"detail": "Not found"})


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
