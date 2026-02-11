export enum SubjectId {
  ENGLISH = 'english',
  TGO = 'tgo',
  ALGO = 'algo',
  DB = 'db'
}

export enum QuestionType {
  SINGLE = 'SINGLE',
  MULTIPLE = 'MULTIPLE',
  AUDIO = 'AUDIO'
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
  audioUrl?: string;    // URL to audio file for listening questions
  context?: string;     // Additional context (e.g. "Listen to the dialogue...")
  readingPassage?: string; // Reading passage text for comprehension questions
  chartData?: ChartData; // Infographic data for visual questions
  options: Option[];
  correctOptionIds: string[]; // Array for multiple answers
  type: QuestionType;
  topic: string;
  difficulty?: Difficulty;
  languageLevel?: string; // A1/A2/B1/B2/C for CEFR levels
  hint?: string; // Explanation for wrong answers
}

// Chart Data Types for Infographics
export type ChartData = 
  | { type: 'bar'; data: number[]; labels: string[]; colors?: string[]; title?: string }
  | { type: 'pie'; data: number[]; labels: string[]; colors?: string[] }
  | { type: 'line'; data: number[]; labels: string[]; color?: string }
  | { type: 'table'; headers: string[]; rows: (string | number)[][] }
  | { type: 'comparison'; columnA: string; columnB: string }
  | { type: 'comparison_table'; title?: string; columnA: { header: string; content: string }; columnB: { header: string; content: string }; question?: string }
  | { type: 'circle'; radius: number; label?: string; showCenter?: boolean }
  | { type: 'math'; expressions: { label: string; value: string }[]; question?: string };


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