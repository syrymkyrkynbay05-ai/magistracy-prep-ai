import { Question, SubjectId } from "../types";
import { authHeaders } from "./authService";

// Use Railway API for development, empty string for production
const API_BASE_URL = (window.location.hostname === 'localhost' || window.location.hostname.match(/^\d{1,3}\./)) 
  ? 'https://magistr.up.railway.app' 
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

export const getAdminStats = async () => {
  const res = await fetch(`${API_BASE_URL}/admin/stats`, { headers: authHeaders() });
  if (!res.ok) throw new Error("Failed to fetch admin stats");
  return res.json();
};

export const getAdminUsers = async () => {
  const res = await fetch(`${API_BASE_URL}/admin/users`, { headers: authHeaders() });
  if (!res.ok) throw new Error("Failed to fetch admin users");
  return res.json();
};

export const getUserResultsAdmin = async (userId: number) => {
  const res = await fetch(`${API_BASE_URL}/admin/user/${userId}/results`, { headers: authHeaders() });
  if (!res.ok) throw new Error("Failed to fetch user results");
  return res.json();
};