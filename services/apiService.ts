import { Question, SubjectId } from "../types";

// Use relative URL for production (same server serves both frontend and backend)
const API_BASE_URL = '';

export const generateQuestionsForSubject = async (
  subjectId: SubjectId, 
  count: number = 5 
): Promise<Question[]> => {
  try {
    const response = await fetch(`${API_BASE_URL}/generate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        subject_id: subjectId,
        count: count,
      }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      console.error("Backend Error:", errorData);
      return [];
    }

    const questions: Question[] = await response.json();
    return questions;
  } catch (error) {
    console.error("Fetch Error:", error)
    return [];
  }
};

export const getSyllabus = async (subjectId: string): Promise<string> => {
  try {
    const response = await fetch(`${API_BASE_URL}/syllabus/${subjectId}`);
    if (!response.ok) return "Мәлімет табылмады.";
    const data = await response.json();
    return data.content;
  } catch (error) {
    console.error("Fetch Error:", error);
    return "Қате орын алды.";
  }
};