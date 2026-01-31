from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
from sqlalchemy import Column, String, Integer, ForeignKey, Enum as SQLEnum, Text
from sqlalchemy.orm import relationship
from database import Base


class SubjectId(str, Enum):
    ENGLISH = "english"
    TGO = "tgo"
    ALGO = "algo"
    DB = "db"


class QuestionType(str, Enum):
    SINGLE = "SINGLE"
    MULTIPLE = "MULTIPLE"


class Difficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


# SQLAlchemy Models
class DBSubject(Base):
    __tablename__ = "subjects"
    id = Column(String(50), primary_key=True)
    name = Column(String(255), nullable=False)
    questions = relationship("DBQuestion", back_populates="subject")


class DBQuestion(Base):
    __tablename__ = "questions"
    id = Column(String(50), primary_key=True)
    subject_id = Column(String(50), ForeignKey("subjects.id"))
    text = Column(Text, nullable=False)
    code_snippet = Column(Text, nullable=True)
    type = Column(SQLEnum(QuestionType), nullable=False)
    topic = Column(String(255))

    subject = relationship("DBSubject", back_populates="questions")
    options = relationship(
        "DBOption", back_populates="question", cascade="all, delete-orphan"
    )
    correct_option_ids = Column(Text)  # Stored as comma-separated IDs or JSON string
    difficulty = Column(String(20), default="medium")
    hint = Column(Text, nullable=True)


class DBOption(Base):
    __tablename__ = "options"
    id = Column(String(50), primary_key=True)
    question_id = Column(String(50), ForeignKey("questions.id"))
    text = Column(Text, nullable=False)

    question = relationship("DBQuestion", back_populates="options")


# Pydantic Models for API
class Option(BaseModel):
    id: str
    text: str

    class Config:
        from_attributes = True


class Question(BaseModel):
    id: str
    subjectId: SubjectId
    text: str
    codeSnippet: Optional[str] = None
    options: List[Option]
    correctOptionIds: List[str]
    type: QuestionType
    topic: str
    difficulty: Optional[str] = "medium"
    hint: Optional[str] = None

    class Config:
        from_attributes = True


class SubCategory(BaseModel):
    name: str
    description: str


class SubjectDefinition(BaseModel):
    id: SubjectId
    name: str
    promptContext: str
    questionTypeInstruction: str
    defaultQuestionType: QuestionType
    subCategories: List[SubCategory]


class TestResult(BaseModel):
    totalScore: int
    maxScore: int
    subjectScores: dict  # map SubjectId -> {score, max}
    correctCount: int
    totalQuestions: int


class CalculateRequest(BaseModel):
    questions: List[Question]
    answers: dict  # map question_id -> list of selected option_ids
