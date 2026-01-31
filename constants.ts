import { SubjectConfig, SubjectId } from './types';

export const EXAM_DURATION_MINUTES = 235;

export const SUBJECTS: Record<SubjectId, SubjectConfig> = {
  [SubjectId.ENGLISH]: {
    id: SubjectId.ENGLISH,
    name: "Шет тілі (Ағылшын)",
    totalQuestions: 50,
    maxScore: 50,
    description: "Listening, Grammar (Conditionals), Reading (Academic). 1 баллдан.",
    topics: [
      "Listening (Тыңдалым)",
      "Grammar & Vocabulary (Лексика-грамматика)",
      "Reading (Оқылым)"
    ]
  },
  [SubjectId.TGO]: {
    id: SubjectId.TGO,
    name: "Оқу дайындығын анықтау (ОДАТ)",
    totalQuestions: 30,
    maxScore: 30,
    description: "15 сұрақ — Сыни ойлау, 15 сұрақ — Аналитикалық ойлау.",
    topics: [
      "Аналитикалық ойлау (Логика, Графиктер)",
      "Сыни ойлау (Мәтіндік талдау)"
    ]
  },
  [SubjectId.ALGO]: {
    id: SubjectId.ALGO,
    name: "Алгоритмдер және деректер құрылымы",
    totalQuestions: 30,
    maxScore: 30,
    isProfile: true,
    description: "C++, Stack/Queue, Graphs, Big O. (1 балл)",
    topics: [
      "Программалау негіздері (C++)",
      "Деректер құрылымы (Stack, Queue, Tree)",
      "Графтар алгоритмі (Dijkstra, MST)",
      "Алгоритм күрделілігі (Big O)"
    ]
  },
  [SubjectId.DB]: {
    id: SubjectId.DB,
    name: "Дерекқор базасы (SQL)",
    totalQuestions: 20,
    maxScore: 40,
    isProfile: true,
    description: "Бір немесе бірнеше дұрыс жауап. (2 балл)",
    topics: [
      "ER-модельдеу және Жобалау",
      "Реляциялық модель және Нормализация",
      "SQL (Практикалық сұраныстар)",
      "Архитектура және ACID"
    ]
  }
};