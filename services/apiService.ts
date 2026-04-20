import { Question, SubjectId } from "../types";
import { authHeaders } from "./authService";

// Use localhost or local IP for local development, empty string for production
const API_BASE_URL = (window.location.hostname === 'localhost' || window.location.hostname.match(/^\d{1,3}\./)) 
  ? `http://${window.location.hostname}:8000` 
  : '';

export const generateQuestionsForSubject = async (
  subjectId: SubjectId, 
  count: number = 5 
): Promise<Question[]> => {
  try {
    const response = await fetch(`${API_BASE_URL}/generate`, {
      method: 'POST',
      headers: authHeaders(),
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