export enum SubjectId {
  ENGLISH = 'english',
  TGO = 'tgo',
  ALGO = 'algo',
  DB = 'db'
}

export enum QuestionType {
  SINGLE = 'SINGLE',
  MULTIPLE = 'MULTIPLE'
}

export enum Difficulty {
  EASY = 'easy',
  MEDIUM = 'medium',
  HARD = 'hard'
}

export interface Option {
  id: string;
  text: string;
}

export interface Question {
  id: string;
  subjectId: SubjectId;
  text: string;
  codeSnippet?: string; // For C++ or SQL code blocks
  options: Option[];
  correctOptionIds: string[]; // Array for multiple answers
  type: QuestionType;
  topic: string;
  difficulty?: Difficulty;
  hint?: string; // Explanation for wrong answers
}

export interface SubjectConfig {
  id: SubjectId;
  name: string;
  totalQuestions: number;
  maxScore: number;
  topics: string[];
  description: string;
  isProfile?: boolean;
}

// New Interface for Database Definitions
export interface SubjectDefinition {
  id: SubjectId;
  name: string;
  promptContext: string;
  questionTypeInstruction: string;
  defaultQuestionType: QuestionType;
  subCategories: {
    name: string;
    description: string;
    examples?: string[];
  }[];
}

export interface UserAnswers {
  [questionId: string]: string[]; // Array of selected option IDs
}

export interface TestResult {
  totalScore: number;
  maxScore: number;
  subjectScores: Record<SubjectId, { score: number; max: number }>;
  correctCount: number;
  totalQuestions: number;
}