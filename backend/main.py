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
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from dotenv import load_dotenv

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
)
from database import get_db, engine, Base

load_dotenv()

# Initialize database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Magistracy Prep AI Backend")

# Enable CORS for the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GenerateRequest(BaseModel):
    subject_id: SubjectId
    count: int = 5


@app.get("/")
async def root():
    return {"message": "Magistracy Prep AI API is running with SQLite"}


@app.post("/generate", response_model=List[Question])
async def generate_questions(request: GenerateRequest, db: Session = Depends(get_db)):
    # Fetch random questions from the database for the given subject
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
                options=options,
                correctOptionIds=correct_ids,
                type=db_q.type,
                topic=db_q.topic or "General",
                difficulty=db_q.difficulty or "medium",
                hint=db_q.hint,
            )
        )

    # Sort questions by difficulty: easy -> medium -> hard
    difficulty_order = {"easy": 0, "medium": 1, "hard": 2}
    questions.sort(key=lambda q: difficulty_order.get(q.difficulty, 1))

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
async def calculate_results(request: CalculateRequest):
    # Calculation logic remains the same as it works on Pydantic models
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
            # DB Questions are usually 2 points
            q_max_points = 2

            # Exact match logic for full points
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

    return TestResult(
        totalScore=total_score,
        maxScore=total_max_score,
        subjectScores=subject_scores,
        correctCount=correct_count,
        totalQuestions=len(request.questions),
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
