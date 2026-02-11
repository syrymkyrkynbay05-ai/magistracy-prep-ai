/**
 * Auth Service — register, login, token management, OTP password reset.
 * Токен localStorage-да сақталады — DevTools > Application > Local Storage.
 */

const API_BASE_URL = window.location.hostname === 'localhost' ? 'http://localhost:8000' : '';
const TOKEN_KEY = 'magistracy_access_token';
const USER_KEY = 'magistracy_user';

// ==================== Types ====================
export interface UserProfile {
  id: number;
  email: string;
  full_name: string;
  is_active: boolean;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
  user: UserProfile;
}

// ==================== Token Management ====================
export function getToken(): string | null {
  return localStorage.getItem(TOKEN_KEY);
}

export function setToken(token: string): void {
  localStorage.setItem(TOKEN_KEY, token);
}

export function removeToken(): void {
  localStorage.removeItem(TOKEN_KEY);
  localStorage.removeItem(USER_KEY);
}

export function getSavedUser(): UserProfile | null {
  const raw = localStorage.getItem(USER_KEY);
  if (!raw) return null;
  try { return JSON.parse(raw); } catch { return null; }
}

export function saveUser(user: UserProfile): void {
  localStorage.setItem(USER_KEY, JSON.stringify(user));
}

export function isAuthenticated(): boolean {
  return !!getToken();
}

export function authHeaders(): Record<string, string> {
  const token = getToken();
  return token
    ? { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` }
    : { 'Content-Type': 'application/json' };
}

// ==================== API Calls ====================

/** Тіркелу */
export async function register(email: string, full_name: string, password: string): Promise<AuthResponse> {
  const response = await fetch(`${API_BASE_URL}/auth/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, full_name, password }),
  });
  if (!response.ok) {
    const err = await response.json();
    throw new Error(err.detail || 'Тіркелу кезінде қате орын алды');
  }
  const data: AuthResponse = await response.json();
  setToken(data.access_token);
  saveUser(data.user);
  return data;
}

/** Кіру */
export async function login(email: string, password: string): Promise<AuthResponse> {
  const response = await fetch(`${API_BASE_URL}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password }),
  });
  if (!response.ok) {
    const err = await response.json();
    throw new Error(err.detail || 'Кіру кезінде қате орын алды');
  }
  const data: AuthResponse = await response.json();
  setToken(data.access_token);
  saveUser(data.user);
  return data;
}

/** Шығу */
export function logout(): void {
  removeToken();
}

/** Профиль алу */
export async function getProfile(): Promise<UserProfile> {
  const response = await fetch(`${API_BASE_URL}/auth/me`, {
    headers: authHeaders(),
  });
  if (!response.ok) {
    removeToken();
    throw new Error('Сессия аяқталды');
  }
  const user: UserProfile = await response.json();
  saveUser(user);
  return user;
}

/** Парольді ұмыту — OTP код жіберу */
export async function forgotPassword(email: string): Promise<string> {
  const response = await fetch(`${API_BASE_URL}/auth/forgot-password`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email }),
  });
  if (!response.ok) {
    const err = await response.json();
    throw new Error(err.detail || 'Қате орын алды');
  }
  const data = await response.json();
  return data.message;
}

/** OTP кодын тексеру */
export async function verifyOtp(email: string, otp_code: string): Promise<string> {
  const response = await fetch(`${API_BASE_URL}/auth/verify-otp`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, otp_code }),
  });
  if (!response.ok) {
    const err = await response.json();
    throw new Error(err.detail || 'Код қате');
  }
  const data = await response.json();
  return data.message;
}

/** Жаңа пароль орнату (OTP арқылы) */
export async function resetPassword(email: string, otp_code: string, newPassword: string): Promise<string> {
  const response = await fetch(`${API_BASE_URL}/auth/reset-password`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, otp_code, new_password: newPassword }),
  });
  if (!response.ok) {
    const err = await response.json();
    throw new Error(err.detail || 'Қате орын алды');
  }
  const data = await response.json();
  return data.message;
}

// ==================== History ====================

export interface HistoryItem {
  id: number;
  total_score: number;
  max_score: number;
  subject_scores: string; // JSON string
  correct_count: number;
  total_questions: number;
  created_at: string;
}

/** Тест тарихын алу */
export async function getHistory(): Promise<HistoryItem[]> {
  const response = await fetch(`${API_BASE_URL}/auth/history`, {
    headers: authHeaders(),
  });
  if (!response.ok) {
    throw new Error('Тарихты жүктеу мүмкін болмады');
  }
  return await response.json();
}

/** Тест нәтижесін өшіру */
export async function deleteHistoryItem(id: number): Promise<void> {
  const response = await fetch(`${API_BASE_URL}/auth/history/${id}`, {
    method: 'DELETE',
    headers: authHeaders(),
  });
  if (!response.ok) {
    throw new Error('Өшіру кезінде қате орын алды');
  }
}
