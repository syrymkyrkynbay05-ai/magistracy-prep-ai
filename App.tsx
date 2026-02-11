import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, useNavigate, Navigate } from 'react-router-dom';
import { Question, SubjectId, UserAnswers } from './types';
import { EXAM_DURATION_MINUTES } from './constants';
import { generateQuestionsForSubject } from './services/apiService';
import { isAuthenticated, getSavedUser, logout, getProfile, UserProfile } from './services/authService';
import AuthScreen from './components/AuthScreen';
import WelcomeScreen from './components/WelcomeScreen';
import TestScreen from './components/TestScreen';
import ResultScreen from './components/ResultScreen';
import SyllabusScreen from './components/SyllabusScreen';
import HistoryScreen from './components/HistoryScreen';

const RootApp: React.FC = () => {
  const [user, setUser] = useState<UserProfile | null>(getSavedUser());
  const [isCheckingAuth, setIsCheckingAuth] = useState(true);
  const [questions, setQuestions] = useState<Question[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [userAnswers, setUserAnswers] = useState<UserAnswers>({});
  const navigate = useNavigate();

  // Check auth on mount
  useEffect(() => {
    const checkAuth = async () => {
      if (isAuthenticated()) {
        try {
          const profile = await getProfile();
          setUser(profile);
        } catch {
          // Token expired or invalid
          logout();
          setUser(null);
        }
      }
      setIsCheckingAuth(false);
    };
    checkAuth();
  }, []);

  const handleAuthSuccess = (userData: { id: number; email: string; full_name: string }) => {
    setUser(userData as UserProfile);
    navigate('/home');
  };

  const handleLogout = () => {
    logout();
    setUser(null);
    navigate('/');
  };

  const startTest = async (name: string) => {
    setIsLoading(true);
    try {
      const p1 = generateQuestionsForSubject(SubjectId.ENGLISH, 50);
      const p2 = generateQuestionsForSubject(SubjectId.TGO, 30);
      const p3 = generateQuestionsForSubject(SubjectId.ALGO, 30);
      const p4 = generateQuestionsForSubject(SubjectId.DB, 20);

      const results = await Promise.all([p1, p2, p3, p4]);
      const allQuestions = results.flat();

      if (allQuestions.length === 0) {
        alert("Сұрақтарды жүктеу кезінде қате орын алды. Қайта көріңіз.");
        setIsLoading(false);
        return;
      }

      setQuestions(allQuestions);
      setUserAnswers({});
      navigate('/test');
    } catch (error) {
      console.error(error);
      alert("An error occurred while starting the test.");
    } finally {
      setIsLoading(false);
    }
  };

  const handleFinishTest = (answers: UserAnswers) => {
    setUserAnswers(answers);
    navigate('/result');
  };

  const handleRestart = () => {
    setQuestions([]);
    setUserAnswers({});
    navigate('/home');
  };

  const handlePracticeWrong = (wrongQuestions: Question[]) => {
    setQuestions(wrongQuestions);
    setUserAnswers({});
    navigate('/test');
  };

  // Show loading during auth check
  if (isCheckingAuth) {
    return (
      <div className="min-h-screen bg-[#07090d] flex items-center justify-center">
        <div className="text-slate-500 font-bold animate-pulse">Жүктелуде...</div>
      </div>
    );
  }

  // If not authenticated, show auth screen
  if (!user) {
    return <AuthScreen onAuthSuccess={handleAuthSuccess} />;
  }

  // Authenticated: show main app
  return (
    <div className="font-sans">
      <Routes>
        <Route path="/" element={<Navigate to="/home" replace />} />
        <Route 
          path="/home" 
          element={
            <WelcomeScreen 
              onStart={startTest} 
              isLoading={isLoading} 
              onViewProgram={() => navigate('/program')}
              onViewHistory={() => navigate('/history')}
              userName={user.full_name}
              onLogout={handleLogout}
            />
          } 
        />
        <Route 
          path="/program/:subjectId?" 
          element={<SyllabusScreen onBack={() => navigate('/home')} />} 
        />
        <Route 
          path="/history" 
          element={<HistoryScreen onBack={() => navigate('/home')} />} 
        />
        <Route 
          path="/test/:subjectId/q/:qIndex" 
          element={
            questions.length > 0 ? (
              <TestScreen 
                questions={questions} 
                durationMinutes={EXAM_DURATION_MINUTES} 
                onFinish={handleFinishTest}
                userName={user.full_name}
              />
            ) : (
              <Navigate to="/home" replace />
            )
          } 
        />
        <Route path="/test" element={<Navigate to={`/test/${SubjectId.ENGLISH}/q/1`} replace />} />
        <Route 
          path="/result" 
          element={
            questions.length > 0 ? (
              <ResultScreen 
                questions={questions}
                answers={userAnswers}
                onRestart={handleRestart}
                onPracticeWrong={handlePracticeWrong}
                userName={user.full_name}
              />
            ) : (
              <Navigate to="/home" replace />
            )
          } 
        />
      </Routes>
    </div>
  );
};

const App: React.FC = () => (
  <Router>
    <RootApp />
  </Router>
);

export default App;