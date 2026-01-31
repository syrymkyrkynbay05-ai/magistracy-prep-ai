import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, useNavigate, Navigate } from 'react-router-dom';
import { Question, SubjectId, UserAnswers } from './types';
import { EXAM_DURATION_MINUTES } from './constants';
import { generateQuestionsForSubject } from './services/apiService';
import WelcomeScreen from './components/WelcomeScreen';
import TestScreen from './components/TestScreen';
import ResultScreen from './components/ResultScreen';
import SyllabusScreen from './components/SyllabusScreen';

const RootApp: React.FC = () => {
  const [userName, setUserName] = useState('');
  const [questions, setQuestions] = useState<Question[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [userAnswers, setUserAnswers] = useState<UserAnswers>({});
  const navigate = useNavigate();

  const startTest = async (name: string) => {
    setUserName(name);
    setIsLoading(true);
    try {
      const p1 = generateQuestionsForSubject(SubjectId.ENGLISH, 50);
      const p2 = generateQuestionsForSubject(SubjectId.TGO, 30);
      const p3 = generateQuestionsForSubject(SubjectId.ALGO, 30);
      const p4 = generateQuestionsForSubject(SubjectId.DB, 20);

      const results = await Promise.all([p1, p2, p3, p4]);
      const allQuestions = results.flat();

      if (allQuestions.length === 0) {
        alert("Failed to generate questions. Please check your API Key or try again.");
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
            />
          } 
        />
        <Route 
          path="/program/:subjectId?" 
          element={<SyllabusScreen onBack={() => navigate('/home')} />} 
        />
        <Route 
          path="/test/:subjectId/q/:qIndex" 
          element={
            questions.length > 0 ? (
              <TestScreen 
                questions={questions} 
                durationMinutes={EXAM_DURATION_MINUTES} 
                onFinish={handleFinishTest}
                userName={userName}
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
                userName={userName}
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