import React, { useState, useEffect } from 'react';
import { Question, SubjectId, UserAnswers } from '../types';
import { SUBJECTS } from '../constants';
import { ChevronDown, ChevronUp, CheckCircle, XCircle, Trophy, Home, RotateCcw, BookOpen, TrendingUp, Target } from 'lucide-react';

interface ResultScreenProps {
  questions: Question[];
  answers: UserAnswers;
  onRestart: () => void;
  onPracticeWrong?: (wrongQuestions: Question[]) => void;
  userName: string;
}

// Storage key for test history
const HISTORY_KEY = 'test_history';

interface TestHistoryItem {
  date: string;
  score: number;
  total: number;
  percentage: number;
  subjectScores: Record<string, { correct: number; total: number }>;
  cefrLevel: string;
}

// CEFR Level calculation
const calculateCEFRLevel = (
  levelStats: Record<string, { correct: number; total: number }>
): string => {
  const getPercentage = (level: string) => {
    const stats = levelStats[level];
    if (!stats || stats.total === 0) return 100; // If no questions at this level, assume passed
    return (stats.correct / stats.total) * 100;
  };

  const a1Pct = getPercentage('A1');
  const a2Pct = getPercentage('A2');
  const b1Pct = getPercentage('B1');
  const b2Pct = getPercentage('B2');
  const cPct = getPercentage('C');

  // CEFR level determination based on specification
  if (a1Pct >= 90 && a2Pct >= 80 && b1Pct >= 70 && b2Pct >= 60 && cPct >= 50) {
    return 'C1';
  } else if (a1Pct >= 80 && a2Pct >= 70 && b1Pct >= 60 && b2Pct >= 50) {
    return 'B2';
  } else if (a1Pct >= 70 && a2Pct >= 60 && b1Pct >= 50) {
    return 'B1';
  } else if (a1Pct >= 50 && a2Pct >= 50) {
    return 'A2';
  } else if (a1Pct >= 50) {
    return 'A1';
  } else {
    return 'Pre-A1';
  }
};

const getLevelColor = (level: string): string => {
  switch (level) {
    case 'C1': return 'from-purple-500 to-pink-500';
    case 'B2': return 'from-orange-500 to-red-500';
    case 'B1': return 'from-yellow-500 to-orange-500';
    case 'A2': return 'from-blue-500 to-cyan-500';
    case 'A1': return 'from-green-500 to-teal-500';
    default: return 'from-gray-500 to-gray-600';
  }
};

const getLevelDescription = (level: string): string => {
  switch (level) {
    case 'C1': return 'Жоғары деңгей - Күрделі мәтіндерді түсінесіз';
    case 'B2': return 'Жоғары орта - Еркін қарым-қатынас жасай аласыз';
    case 'B1': return 'Орта деңгей - Күнделікті тақырыптарда сөйлей аласыз';
    case 'A2': return 'Бастапқы-орта - Қарапайым сөйлесуге қабілеттісіз';
    case 'A1': return 'Бастапқы деңгей - Негізгі сөздерді түсінесіз';
    default: return 'Дайындық қажет';
  }
};

const ResultScreen: React.FC<ResultScreenProps> = ({ questions, answers, onRestart, onPracticeWrong, userName }) => {
  const [expandedSubject, setExpandedSubject] = useState<SubjectId | null>(null);
  const [showHistory, setShowHistory] = useState(false);
  const [history, setHistory] = useState<TestHistoryItem[]>([]);

  // Calculate scores per subject
  const subjectResults = Object.values(SUBJECTS).map(subject => {
    const subjectQuestions = questions.filter(q => q.subjectId === subject.id);
    let correctCount = 0;
    
    subjectQuestions.forEach(q => {
      const userAnswer = answers[q.id] || [];
      const correctAnswer = q.correctOptionIds || [];
      
      const isCorrect = 
        userAnswer.length === correctAnswer.length &&
        userAnswer.every(id => correctAnswer.includes(id));
      
      if (isCorrect) correctCount++;
    });

    return {
      subject,
      total: subjectQuestions.length,
      correct: correctCount,
      questions: subjectQuestions,
    };
  });

  const totalScore = subjectResults.reduce((sum, r) => sum + r.correct, 0);
  const totalQuestions = subjectResults.reduce((sum, r) => sum + r.total, 0);

  // Calculate language level stats (for English)
  const englishQuestions = questions.filter(q => q.subjectId === SubjectId.ENGLISH);
  const levelStats: Record<string, { correct: number; total: number }> = {};
  
  englishQuestions.forEach(q => {
    const level = q.languageLevel || 'A2';
    if (!levelStats[level]) levelStats[level] = { correct: 0, total: 0 };
    levelStats[level].total++;
    
    const userAnswer = answers[q.id] || [];
    const correct = userAnswer.length === q.correctOptionIds.length && 
                   userAnswer.every(id => q.correctOptionIds.includes(id));
    if (correct) levelStats[level].correct++;
  });

  const cefrLevel = calculateCEFRLevel(levelStats);

  // Get wrong questions
  const wrongQuestions = questions.filter(q => {
    const userAnswer = answers[q.id] || [];
    const correct = userAnswer.length === q.correctOptionIds.length && 
                   userAnswer.every(id => q.correctOptionIds.includes(id));
    return !correct;
  });

  // Save to history on mount
  useEffect(() => {
    const historyItem: TestHistoryItem = {
      date: new Date().toLocaleString('kk-KZ'),
      score: totalScore,
      total: totalQuestions,
      percentage: totalQuestions > 0 ? Math.round((totalScore / totalQuestions) * 100) : 0,
      subjectScores: {},
      cefrLevel,
    };

    subjectResults.forEach(r => {
      if (r.total > 0) {
        historyItem.subjectScores[r.subject.name] = { correct: r.correct, total: r.total };
      }
    });

    // Load existing history
    const existingHistory = JSON.parse(localStorage.getItem(HISTORY_KEY) || '[]');
    
    // Add new result and keep only last 10
    const newHistory = [historyItem, ...existingHistory].slice(0, 10);
    
    localStorage.setItem(HISTORY_KEY, JSON.stringify(newHistory));
    setHistory(newHistory);
  }, []);

  // Get user's answer letter for a question
  const getAnswerLetter = (question: Question, userAnswer: string[]) => {
    if (!userAnswer || userAnswer.length === 0) return '—';
    
    return userAnswer
      .map(answerId => {
        const idx = question.options.findIndex(opt => opt.id === answerId);
        return idx >= 0 ? String.fromCharCode(65 + idx) : '?';
      })
      .join(', ');
  };

  // Check if answer is correct
  const isAnswerCorrect = (question: Question, userAnswer: string[]) => {
    if (!userAnswer || userAnswer.length === 0) return false;
    
    const correctAnswer = question.correctOptionIds || [];
    
    return (
      userAnswer.length === correctAnswer.length &&
      userAnswer.every(id => correctAnswer.includes(id))
    );
  };

  // Get correct answer letter
  const getCorrectLetter = (question: Question) => {
    const correctIds = question.correctOptionIds || [];
    return correctIds
      .map(id => {
        const idx = question.options.findIndex(opt => opt.id === id);
        return idx >= 0 ? String.fromCharCode(65 + idx) : '?';
      })
      .join(', ');
  };

  return (
    <div className="min-h-screen bg-[#F5F7FA] font-sans">
      {/* Header */}
      <header className="bg-[#348FE2] text-white py-6 shadow-lg">
        <div className="max-w-6xl mx-auto px-4 text-center">
          <div className="flex items-center justify-center gap-3 mb-2">
            <Trophy className="w-10 h-10 text-yellow-300" />
            <h1 className="text-3xl font-bold">Тест нәтижесі</h1>
          </div>
          <p className="text-blue-100">{userName}</p>
        </div>
      </header>

      <div className="max-w-6xl mx-auto px-4 py-8">
        
        {/* CEFR Level Card (for English) */}
        {englishQuestions.length > 0 && (
          <div className={`bg-gradient-to-r ${getLevelColor(cefrLevel)} rounded-2xl p-6 mb-8 text-white shadow-xl`}>
            <div className="flex items-center justify-between flex-wrap gap-4">
              <div>
                <div className="text-sm opacity-80 mb-1">Сіздің ағылшын тілі деңгейіңіз</div>
                <div className="text-5xl font-bold">{cefrLevel}</div>
                <div className="text-sm mt-2 opacity-90">{getLevelDescription(cefrLevel)}</div>
              </div>
              <div className="text-right">
                <Target className="w-16 h-16 opacity-50" />
              </div>
            </div>
            
            {/* Level breakdown */}
            <div className="mt-6 grid grid-cols-5 gap-2">
              {['A1', 'A2', 'B1', 'B2', 'C'].map(level => {
                const stats = levelStats[level];
                const pct = stats ? Math.round((stats.correct / stats.total) * 100) : 0;
                return (
                  <div key={level} className="bg-white/20 rounded-lg p-2 text-center">
                    <div className="font-bold">{level}</div>
                    <div className="text-xs">{stats ? `${stats.correct}/${stats.total}` : '—'}</div>
                    <div className="text-xs opacity-80">{stats ? `${pct}%` : ''}</div>
                  </div>
                );
              })}
            </div>
          </div>
        )}

        {/* Summary Table */}
        <div className="bg-white rounded-lg shadow-md overflow-hidden mb-8">
          <table className="w-full">
            <thead>
              <tr className="bg-gray-100 border-b-2 border-gray-200">
                <th className="text-left py-4 px-6 font-bold text-gray-700 text-lg">Бөлім:</th>
                <th className="text-center py-4 px-6 font-bold text-gray-700 text-lg">Бөлім бойынша ұпай саны:</th>
                <th className="text-center py-4 px-6 font-bold text-gray-700 text-lg w-40 bg-blue-50">Барлығы:</th>
              </tr>
            </thead>
            <tbody>
              {subjectResults.map((result, idx) => (
                <tr key={result.subject.id} className={idx % 2 === 0 ? 'bg-white' : 'bg-gray-50'}>
                  <td className="py-4 px-6 border-b border-gray-200 text-gray-800">
                    {result.subject.name}
                  </td>
                  <td className="py-4 px-6 border-b border-gray-200 text-center font-semibold text-lg">
                    {result.correct}
                  </td>
                  {idx === 0 && (
                    <td 
                      rowSpan={subjectResults.length} 
                      className="py-4 px-6 border-b border-gray-200 text-center align-middle bg-blue-50"
                    >
                      <div className="text-6xl font-bold text-[#348FE2]">{totalScore}</div>
                      <div className="text-gray-500 text-sm mt-1">/ {totalQuestions}</div>
                    </td>
                  )}
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* Action Buttons with Practice Wrong */}
        <div className="flex items-center justify-center gap-4 mb-8 flex-wrap">
          <button
            onClick={onRestart}
            className="flex items-center gap-2 bg-[#348FE2] text-white px-8 py-3 rounded-lg font-bold text-lg shadow-lg hover:bg-[#2980B9] transition"
          >
            <RotateCcw className="w-5 h-5" />
            Қайта тапсыру
          </button>
          
          {wrongQuestions.length > 0 && (
            <button
              onClick={() => onPracticeWrong?.(wrongQuestions)}
              className="flex items-center gap-2 bg-amber-500 text-white px-8 py-3 rounded-lg font-bold text-lg shadow-lg hover:bg-amber-600 transition"
            >
              <BookOpen className="w-5 h-5" />
              Қателерді қайталау ({wrongQuestions.length})
            </button>
          )}
          
          <button
            onClick={() => setShowHistory(!showHistory)}
            className="flex items-center gap-2 bg-purple-500 text-white px-8 py-3 rounded-lg font-bold text-lg shadow-lg hover:bg-purple-600 transition"
          >
            <TrendingUp className="w-5 h-5" />
            Тарих
          </button>
          
          <button
            onClick={() => window.location.reload()}
            className="flex items-center gap-2 bg-gray-600 text-white px-8 py-3 rounded-lg font-bold text-lg shadow-lg hover:bg-gray-700 transition"
          >
            <Home className="w-5 h-5" />
            Басты бетке
          </button>
        </div>

        {/* History Panel */}
        {showHistory && (
          <div className="bg-white rounded-lg shadow-md p-6 mb-8">
            <h3 className="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2">
              <TrendingUp className="w-6 h-6 text-purple-500" />
              Тест тарихы (соңғы 10)
            </h3>
            {history.length === 0 ? (
              <p className="text-gray-500">Әлі тест тапсырылмаған</p>
            ) : (
              <div className="overflow-x-auto">
                <table className="w-full text-sm">
                  <thead>
                    <tr className="bg-gray-100">
                      <th className="py-2 px-4 text-left">Күні</th>
                      <th className="py-2 px-4 text-center">Нәтиже</th>
                      <th className="py-2 px-4 text-center">%</th>
                      <th className="py-2 px-4 text-center">CEFR</th>
                    </tr>
                  </thead>
                  <tbody>
                    {history.map((item, idx) => (
                      <tr key={idx} className={idx === 0 ? 'bg-green-50 font-semibold' : ''}>
                        <td className="py-2 px-4 border-b">{item.date}</td>
                        <td className="py-2 px-4 border-b text-center">{item.score}/{item.total}</td>
                        <td className="py-2 px-4 border-b text-center">{item.percentage}%</td>
                        <td className="py-2 px-4 border-b text-center">
                          <span className={`px-2 py-1 rounded text-xs font-bold ${
                            item.cefrLevel === 'C1' ? 'bg-purple-100 text-purple-700' :
                            item.cefrLevel === 'B2' ? 'bg-orange-100 text-orange-700' :
                            item.cefrLevel === 'B1' ? 'bg-yellow-100 text-yellow-700' :
                            item.cefrLevel === 'A2' ? 'bg-blue-100 text-blue-700' :
                            'bg-green-100 text-green-700'
                          }`}>{item.cefrLevel}</span>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        )}

        {/* Detailed Results per Subject */}
        <h2 className="text-2xl font-bold text-gray-800 mb-4">Тестілеу деректері</h2>
        
        <div className="space-y-4">
          {subjectResults.map((result) => (
            <div key={result.subject.id} className="bg-white rounded-lg shadow-md overflow-hidden">
              {/* Subject Header */}
              <div 
                onClick={() => setExpandedSubject(expandedSubject === result.subject.id ? null : result.subject.id)}
                className="flex items-center justify-between p-4 cursor-pointer hover:bg-gray-50 transition border-b border-gray-200"
              >
                <div>
                  <div className="text-lg font-bold text-gray-800">Бөлім: {result.subject.name}</div>
                  <div className="text-sm text-gray-600 mt-1">
                    Жауаптар саны: <span className="font-semibold">{result.total}</span> | 
                    Бөлім бойынша ұпай саны: <span className="font-semibold text-green-600">{result.correct}</span>
                  </div>
                </div>
                <div className="flex items-center gap-4">
                  <div className="text-2xl font-bold text-[#348FE2]">
                    {result.correct} / {result.total}
                  </div>
                  {expandedSubject === result.subject.id ? (
                    <ChevronUp className="w-6 h-6 text-gray-500" />
                  ) : (
                    <ChevronDown className="w-6 h-6 text-gray-500" />
                  )}
                </div>
              </div>

              {/* Expanded Content */}
              {expandedSubject === result.subject.id && (
                <div className="p-4 overflow-x-auto">
                  <table className="w-full text-sm border-collapse">
                    <thead>
                      <tr className="bg-gray-100">
                        <td className="py-2 px-3 border border-gray-300 font-medium text-gray-700 whitespace-nowrap">
                          Тест тапсырмасының реті
                        </td>
                        {result.questions.map((_, idx) => (
                          <td key={idx} className="py-2 px-2 border border-gray-300 text-center font-bold min-w-[32px]">
                            {idx + 1}
                          </td>
                        ))}
                      </tr>
                    </thead>
                    <tbody>
                      {/* User's Answers Row */}
                      <tr>
                        <td className="py-2 px-3 border border-gray-300 font-medium text-gray-700 whitespace-nowrap">
                          Таңдауыңыз
                        </td>
                        {result.questions.map((q) => {
                          const userAnswer = answers[q.id] || [];
                          const letter = getAnswerLetter(q, userAnswer);
                          const correct = isAnswerCorrect(q, userAnswer);
                          
                          return (
                            <td 
                              key={q.id} 
                              className={`py-2 px-2 border border-gray-300 text-center font-bold
                                ${correct ? 'bg-green-100 text-green-700' : userAnswer.length > 0 ? 'bg-red-100 text-red-700' : 'bg-gray-100 text-gray-400'}
                              `}
                            >
                              {letter}
                            </td>
                          );
                        })}
                      </tr>
                      
                      {/* Correct Answers Row */}
                      <tr>
                        <td className="py-2 px-3 border border-gray-300 font-medium text-gray-700 whitespace-nowrap">
                          Дұрыс жауап
                        </td>
                        {result.questions.map((q) => (
                          <td 
                            key={q.id} 
                            className="py-2 px-2 border border-gray-300 text-center font-bold text-green-700 bg-green-50"
                          >
                            {getCorrectLetter(q)}
                          </td>
                        ))}
                      </tr>

                      {/* Points Row */}
                      <tr>
                        <td className="py-2 px-3 border border-gray-300 font-medium text-gray-700 whitespace-nowrap">
                          Ұпай
                        </td>
                        {result.questions.map((q) => {
                          const userAnswer = answers[q.id] || [];
                          const correct = isAnswerCorrect(q, userAnswer);
                          
                          return (
                            <td 
                              key={q.id} 
                              className={`py-2 px-2 border border-gray-300 text-center font-bold
                                ${correct ? 'text-green-600' : 'text-red-600'}
                              `}
                            >
                              {correct ? '1' : '0'}
                            </td>
                          );
                        })}
                      </tr>
                    </tbody>
                  </table>
                </div>
              )}
            </div>
          ))}
        </div>

        {/* Topic Analysis - Weak Areas */}
        {(() => {
          const topicStats: Record<string, { total: number; correct: number }> = {};
          questions.forEach(q => {
            if (!topicStats[q.topic]) topicStats[q.topic] = { total: 0, correct: 0 };
            topicStats[q.topic].total++;
            const userAnswer = answers[q.id] || [];
            const correct = userAnswer.length === q.correctOptionIds.length && userAnswer.every(id => q.correctOptionIds.includes(id));
            if (correct) topicStats[q.topic].correct++;
          });
          
          const weakTopics = Object.entries(topicStats)
            .filter(([_, stats]) => stats.total > 0 && (stats.correct / stats.total) < 0.5)
            .sort((a, b) => (a[1].correct / a[1].total) - (b[1].correct / b[1].total))
            .slice(0, 5);

          if (weakTopics.length === 0) return null;

          return (
            <div className="mt-8 bg-amber-50 border border-amber-200 rounded-lg p-6">
              <h3 className="text-xl font-bold text-amber-800 mb-4 flex items-center gap-2">
                📊 Қайталау қажет тақырыптар:
              </h3>
              <ul className="space-y-2">
                {weakTopics.map(([topic, stats]) => (
                  <li key={topic} className="flex items-center justify-between bg-white p-3 rounded-lg border border-amber-100">
                    <span className="font-medium text-gray-700">{topic}</span>
                    <span className="text-amber-600 font-bold">{stats.correct}/{stats.total} ({Math.round((stats.correct / stats.total) * 100)}%)</span>
                  </li>
                ))}
              </ul>
            </div>
          );
        })()}

        {/* Score Breakdown */}
        <div className="mt-8 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg p-6 text-white text-center shadow-xl">
          <div className="text-lg mb-2">Сіздің жалпы нәтижеңіз:</div>
          <div className="text-6xl font-bold mb-2">{totalScore} / {totalQuestions}</div>
          <div className="text-xl">
            {totalQuestions > 0 ? Math.round((totalScore / totalQuestions) * 100) : 0}%
          </div>
          <div className="mt-4 text-blue-100">
            {totalScore >= totalQuestions * 0.8 
              ? '🎉 Керемет! Сіз өте жақсы дайындалғансыз!' 
              : totalScore >= totalQuestions * 0.6 
                ? '👍 Жақсы нәтиже! Аздап дайындалу қажет.' 
                : '📚 Қосымша дайындық қажет. Көңіліңізді түсірмеңіз!'}
          </div>
        </div>

        {/* Certificate Download */}
        {totalScore >= totalQuestions * 0.6 && (
          <div className="mt-8 text-center">
            <button
              onClick={() => {
                const cert = document.createElement('div');
                cert.innerHTML = `
                  <div style="width:800px;height:600px;padding:40px;background:linear-gradient(135deg,#1a365d,#2b6cb0);color:white;font-family:Georgia,serif;text-align:center">
                    <div style="border:3px solid gold;padding:30px;height:100%;box-sizing:border-box">
                      <div style="font-size:24px;color:gold;margin-bottom:20px">🏆 СЕРТИФИКАТ 🏆</div>
                      <div style="font-size:18px;margin-bottom:40px">Магистратураға дайындық курсын сәтті аяқтады</div>
                      <div style="font-size:36px;font-weight:bold;margin-bottom:30px">${userName}</div>
                      <div style="font-size:20px;margin-bottom:20px">Нәтиже: ${totalScore}/${totalQuestions} (${Math.round((totalScore / totalQuestions) * 100)}%)</div>
                      <div style="font-size:18px;margin-bottom:10px;color:gold">CEFR деңгейі: ${cefrLevel}</div>
                      <div style="font-size:14px;color:#90cdf4">${new Date().toLocaleDateString('kk-KZ')}</div>
                    </div>
                  </div>
                `;
                document.body.appendChild(cert);
                const printWindow = window.open('', '_blank');
                if (printWindow) {
                  printWindow.document.write(cert.innerHTML);
                  printWindow.document.close();
                  printWindow.print();
                }
                document.body.removeChild(cert);
              }}
              className="bg-gradient-to-r from-yellow-400 to-orange-500 text-white px-8 py-4 rounded-xl font-bold text-lg shadow-lg hover:from-yellow-500 hover:to-orange-600 transition"
            >
              🎓 Сертификатты жүктеу
            </button>
          </div>
        )}

      </div>
    </div>
  );
};

export default ResultScreen;