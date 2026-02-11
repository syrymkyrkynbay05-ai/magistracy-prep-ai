import React, { useState, useEffect } from 'react';
import { Question, SubjectId, UserAnswers } from '../types';
import { SUBJECTS } from '../constants';
import { ChevronDown, ChevronUp, CheckCircle, XCircle, Trophy, Home, RotateCcw, BookOpen, TrendingUp, Target, BarChart3 } from 'lucide-react';

interface ResultScreenProps {
  questions: Question[];
  answers: UserAnswers;
  onRestart: () => void;
  onPracticeWrong?: (wrongQuestions: Question[]) => void;
  userName: string;
}

const HISTORY_KEY = 'test_history';

const TOPIC_NAMES: Record<string, string> = {
  'critical_thinking': 'Сыни ойлау',
  'analytical_thinking': 'Аналитикалық ойлау',
  'listening': 'Тыңдалым',
  'reading': 'Оқылым',
  'grammar': 'Грамматика / Лексика',
  'db_er': 'ER-модельдеу',
  'db_sql': 'SQL сұраныстары',
  'db_theory': 'Мәліметтер базасының теориясы',
  'algo_cpp': 'C++ негіздері',
  'algo_ds': 'Мәліметтер құрылымы',
  'algo_graphs': 'Графтар алгоритмі',
  'algo_complexity': 'Алгоритмдік күрделілік'
};

const calculateCEFRLevel = (levelStats: Record<string, { correct: number; total: number }>): string => {
  const getPercentage = (level: string) => {
    const stats = levelStats[level];
    if (!stats || stats.total === 0) return 100;
    return (stats.correct / stats.total) * 100;
  };
  const a1Pct = getPercentage('A1');
  const a2Pct = getPercentage('A2');
  const b1Pct = getPercentage('B1');
  const b2Pct = getPercentage('B2');
  const cPct = getPercentage('C');

  if (a1Pct >= 90 && a2Pct >= 80 && b1Pct >= 70 && b2Pct >= 60 && cPct >= 50) return 'C1';
  if (a1Pct >= 80 && a2Pct >= 70 && b1Pct >= 60 && b2Pct >= 50) return 'B2';
  if (a1Pct >= 70 && a2Pct >= 60 && b1Pct >= 50) return 'B1';
  if (a1Pct >= 50 && a2Pct >= 50) return 'A2';
  if (a1Pct >= 50) return 'A1';
  return 'Pre-A1';
};

import { authHeaders } from '../services/authService';

const API_BASE_URL = window.location.hostname === 'localhost' ? 'http://localhost:8000' : '';

const ResultScreen: React.FC<ResultScreenProps> = ({ questions, answers, onRestart, onPracticeWrong, userName }) => {
  const [expandedSubject, setExpandedSubject] = useState<SubjectId | null>(null);
  const [isSaving, setIsSaving] = useState(false);

  const subjectResults = Object.values(SUBJECTS).map(subject => {
    const subjectQuestions = questions.filter(q => q.subjectId === subject.id);
    let correctCount = 0;
    const topicStats: Record<string, { correct: number; total: number }> = {};
    
    subjectQuestions.forEach(q => {
      const userAnswer = answers[q.id] || [];
      const correctIds = q.correctOptionIds || [];
      const isCorrect = userAnswer.length === correctIds.length && userAnswer.every(id => correctIds.includes(id));
      
      if (isCorrect) correctCount++;
      
      if (!topicStats[q.topic]) topicStats[q.topic] = { correct: 0, total: 0 };
      topicStats[q.topic].total++;
      if (isCorrect) topicStats[q.topic].correct++;
    });

    return { subject, total: subjectQuestions.length, correct: correctCount, questions: subjectQuestions, topicStats };
  });

  const totalScore = subjectResults.reduce((sum, r) => sum + r.correct, 0);
  const totalQuestions = subjectResults.reduce((sum, r) => sum + r.total, 0);

  useEffect(() => {
    const saveResults = async () => {
      try {
        setIsSaving(true);
        await fetch(`${API_BASE_URL}/calculate`, {
          method: 'POST',
          headers: authHeaders(),
          body: JSON.stringify({ questions, answers }),
        });
        console.log("Results saved to database");
      } catch (error) {
        console.error("Failed to save results:", error);
      } finally {
        setIsSaving(false);
      }
    };
    saveResults();
  }, []);

  return (
    <div className="min-h-screen bg-[#F5F7FA] pb-20">
      <header className="bg-[#348FE2] text-white py-10 shadow-lg text-center">
        <Trophy className="w-16 h-16 text-yellow-300 mx-auto mb-4" />
        <h1 className="text-4xl font-black mb-2 uppercase tracking-tighter">Тест нәтижесі</h1>
        <p className="text-xl text-blue-100 font-light">{userName}, құттықтаймыз!</p>
      </header>

      <div className="max-w-5xl mx-auto px-4 -mt-8">
        {/* Total Score Card */}
        <div className="bg-white rounded-3xl shadow-2xl p-8 mb-8 flex flex-col md:flex-row items-center justify-between gap-8 border border-white">
          <div className="text-center md:text-left">
            <div className="text-gray-500 font-bold uppercase tracking-widest text-sm mb-2">Жалпы нәтиже</div>
            <div className="text-7xl font-black text-slate-900 leading-none">
              {totalScore} <span className="text-3xl text-gray-300 font-normal">/ {totalQuestions}</span>
            </div>
            <div className="mt-4 flex gap-2">
              <span className="px-4 py-2 bg-green-100 text-green-700 rounded-full font-bold shadow-sm">
                Дұрыс: {totalScore}
              </span>
              <span className="px-4 py-2 bg-red-100 text-red-700 rounded-full font-bold shadow-sm">
                Қате: {totalQuestions - totalScore}
              </span>
            </div>
          </div>
          
          <div className="relative w-40 h-40">
            <svg className="w-full h-full" viewBox="0 0 36 36">
              <circle cx="18" cy="18" r="16" fill="none" className="stroke-gray-100" strokeWidth="4" />
              <circle cx="18" cy="18" r="16" fill="none" className="stroke-blue-500" strokeWidth="4" 
                strokeDasharray={`${(totalScore/totalQuestions)*100}, 100`} strokeLinecap="round" transform="rotate(-90 18 18)" />
            </svg>
            <div className="absolute inset-0 flex items-center justify-center text-3xl font-black text-blue-600">
              {Math.round((totalScore/totalQuestions)*100)}%
            </div>
          </div>
        </div>

        {/* PRO Analytics: Subject & Topic Breakdown */}
        <h2 className="text-2xl font-black text-slate-800 mb-6 flex items-center gap-3">
          <BarChart3 className="w-8 h-8 text-blue-500" />
          Тереңдетілген аналитика
        </h2>

        <div className="grid gap-6">
          {subjectResults.map((result) => (
            <div key={result.subject.id} className="bg-white rounded-3xl shadow-lg overflow-hidden border border-gray-100 group">
              <div 
                onClick={() => setExpandedSubject(expandedSubject === result.subject.id ? null : result.subject.id)}
                className="p-6 cursor-pointer flex flex-col md:flex-row md:items-center justify-between gap-4 hover:bg-slate-50 transition"
              >
                <div className="flex-1">
                  <h3 className="text-xl font-black text-slate-800 mb-2">{result.subject.name}</h3>
                  <div className="flex flex-wrap gap-2">
                    {Object.entries(result.topicStats).map(([topic, stats]) => (
                      <div key={topic} className="px-3 py-1 bg-blue-50 text-blue-600 rounded-lg text-xs font-bold border border-blue-100">
                        {TOPIC_NAMES[topic] || topic}: {stats.correct}/{stats.total}
                      </div>
                    ))}
                  </div>
                </div>
                <div className="flex items-center gap-6">
                  <div className="text-center">
                    <div className="text-3xl font-black text-blue-600">
                      {result.correct} <span className="text-sm text-gray-300">/ {result.total}</span>
                    </div>
                    <div className="text-[10px] font-bold text-gray-400 uppercase tracking-widest">Ұпай</div>
                  </div>
                  {expandedSubject === result.subject.id ? <ChevronUp /> : <ChevronDown />}
                </div>
              </div>

              {expandedSubject === result.subject.id && (
                <div className="p-6 bg-slate-50 border-t border-gray-100">
                   <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                     {Object.entries(result.topicStats).map(([topic, stats]) => {
                       const pct = Math.round((stats.correct / stats.total) * 100);
                       return (
                         <div key={topic} className="bg-white p-5 rounded-2xl shadow-sm border border-gray-100">
                           <div className="flex justify-between items-center mb-3">
                             <span className="font-bold text-slate-700">{TOPIC_NAMES[topic] || topic}</span>
                             <span className={`text-sm font-black ${pct >= 70 ? 'text-green-600' : pct >= 40 ? 'text-orange-500' : 'text-red-500'}`}>
                               {stats.correct} / {stats.total}
                             </span>
                           </div>
                           <div className="w-full bg-slate-100 h-2.5 rounded-full overflow-hidden">
                             <div className={`h-full transition-all duration-1000 ${pct >= 70 ? 'bg-green-500' : pct >= 40 ? 'bg-orange-500' : 'bg-red-500'}`}
                               style={{ width: `${pct}%` }} />
                           </div>
                         </div>
                       );
                     })}
                   </div>

                   {/* Answer Matrix */}
                   <div className="mt-8 overflow-x-auto">
                     <table className="w-full text-xs font-bold">
                        <thead>
                          <tr className="text-gray-400 uppercase tracking-widest border-b border-gray-200">
                            <th className="py-3 text-left">Сұрақ:</th>
                            {result.questions.map((_, i) => <th key={i} className="px-2 text-center">{i+1}</th>)}
                          </tr>
                        </thead>
                        <tbody>
                          <tr className="border-b border-gray-100">
                            <td className="py-4 text-slate-500">Нәтиже:</td>
                            {result.questions.map((q, i) => {
                              const userAnswer = answers[q.id] || [];
                              const isCorrect = userAnswer.length === q.correctOptionIds.length && userAnswer.every(id => q.correctOptionIds.includes(id));
                              return (
                                <td key={i} className="px-2 text-center">
                                  {isCorrect ? <CheckCircle className="w-5 h-5 text-green-500 mx-auto" /> : <XCircle className="w-5 h-5 text-red-400 mx-auto" />}
                                </td>
                              );
                            })}
                          </tr>
                        </tbody>
                     </table>
                   </div>
                </div>
              )}
            </div>
          ))}
        </div>

        {/* Footer Actions */}
        <div className="mt-12 flex flex-wrap justify-center gap-4">
           <button onClick={onRestart} className="flex items-center gap-2 bg-blue-600 text-white px-8 py-4 rounded-2xl font-black shadow-xl hover:scale-105 transition">
             <RotateCcw /> Қайта тапсыру
           </button>
           <button onClick={() => window.location.reload()} className="flex items-center gap-2 bg-slate-800 text-white px-8 py-4 rounded-2xl font-black shadow-xl hover:scale-105 transition">
             <Home /> Басты бет
           </button>
        </div>
      </div>
    </div>
  );
};

export default ResultScreen;