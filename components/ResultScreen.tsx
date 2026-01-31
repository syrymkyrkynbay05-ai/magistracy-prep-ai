import React, { useState } from 'react';
import { Question, SubjectId, UserAnswers } from '../types';
import { SUBJECTS } from '../constants';
import { ChevronDown, ChevronUp, CheckCircle, XCircle, Trophy, Home, RotateCcw } from 'lucide-react';

interface ResultScreenProps {
  questions: Question[];
  answers: UserAnswers;
  onRestart: () => void;
  userName: string;
}

const ResultScreen: React.FC<ResultScreenProps> = ({ questions, answers, onRestart, userName }) => {
  const [expandedSubject, setExpandedSubject] = useState<SubjectId | null>(null);

  // Calculate scores per subject
  const subjectResults = Object.values(SUBJECTS).map(subject => {
    const subjectQuestions = questions.filter(q => q.subjectId === subject.id);
    let correctCount = 0;
    
    subjectQuestions.forEach(q => {
      const userAnswer = answers[q.id] || [];
      const correctAnswer = q.correctOptionIds || [];
      
      // Check if user's answer matches correct answer
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

        {/* Action Buttons */}
        <div className="flex items-center justify-center gap-4 mt-8">
          <button
            onClick={onRestart}
            className="flex items-center gap-2 bg-[#348FE2] text-white px-8 py-3 rounded-lg font-bold text-lg shadow-lg hover:bg-[#2980B9] transition"
          >
            <RotateCcw className="w-5 h-5" />
            Қайта тапсыру
          </button>
          <button
            onClick={() => window.location.reload()}
            className="flex items-center gap-2 bg-gray-600 text-white px-8 py-3 rounded-lg font-bold text-lg shadow-lg hover:bg-gray-700 transition"
          >
            <Home className="w-5 h-5" />
            Басты бетке
          </button>
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