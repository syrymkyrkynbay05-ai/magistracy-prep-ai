import React from 'react';
import { X, Map } from 'lucide-react';
import { SubjectId, Question, UserAnswers } from '../../types';
import { SUBJECTS } from '../../constants';

interface AnswerMapModalProps {
  isOpen: boolean;
  onClose: () => void;
  questions: Question[];
  answers: UserAnswers;
  currentQuestionId: string;
  onSelectQuestion: (questionId: string) => void;
}

const AnswerMapModal: React.FC<AnswerMapModalProps> = ({
  isOpen,
  onClose,
  questions,
  answers,
  currentQuestionId,
  onSelectQuestion,
}) => {
  if (!isOpen) return null;

  // Group questions by subject
  const subjectList = Object.values(SUBJECTS);
  const questionsBySubject = subjectList.map(subject => ({
    subject,
    questions: questions.filter(q => q.subjectId === subject.id),
  }));

  const totalAnswered = questions.filter(q => answers[q.id] && answers[q.id].length > 0).length;
  const totalQuestions = questions.length;

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-[100]" onClick={onClose}>
      <div 
        className="bg-white rounded-lg shadow-2xl w-[95%] max-w-3xl max-h-[85vh] overflow-hidden animate-fade-in"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="bg-[#9B59B6] text-white px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Map className="w-6 h-6" />
            <h2 className="text-lg font-bold">Жауап картасы</h2>
          </div>
          <div className="flex items-center gap-4">
            <span className="text-sm bg-white/20 px-3 py-1 rounded-full">
              {totalAnswered} / {totalQuestions} жауап берілді
            </span>
            <button onClick={onClose} className="hover:bg-white/20 p-1 rounded transition">
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Legend */}
        <div className="px-6 py-3 bg-gray-50 border-b flex items-center gap-6 text-sm">
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-green-500 rounded"></div>
            <span>Жауап берілді</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-blue-500 rounded"></div>
            <span>Ағымдағы</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-gray-200 border border-gray-300 rounded"></div>
            <span>Бос</span>
          </div>
        </div>

        {/* Content */}
        <div className="p-4 overflow-y-auto max-h-[60vh] space-y-6">
          {questionsBySubject.map(({ subject, questions: subjectQuestions }) => {
            const answeredInSubject = subjectQuestions.filter(q => answers[q.id] && answers[q.id].length > 0).length;
            
            return (
              <div key={subject.id}>
                <div className="flex items-center justify-between mb-3">
                  <h3 className="font-bold text-gray-800">{subject.name}</h3>
                  <span className="text-sm text-gray-500">
                    {answeredInSubject} / {subjectQuestions.length}
                  </span>
                </div>
                
                <div className="grid grid-cols-10 gap-1.5">
                  {subjectQuestions.map((q, idx) => {
                    const isAnswered = answers[q.id] && answers[q.id].length > 0;
                    const isCurrent = q.id === currentQuestionId;

                    return (
                      <div
                        key={q.id}
                        onClick={() => {
                          onSelectQuestion(q.id);
                          onClose();
                        }}
                        className={`
                          w-8 h-8 flex items-center justify-center rounded cursor-pointer text-sm font-bold transition-all
                          ${isCurrent 
                            ? 'bg-blue-500 text-white ring-2 ring-blue-300 scale-110 z-10' 
                            : isAnswered 
                              ? 'bg-green-500 text-white hover:bg-green-600' 
                              : 'bg-gray-100 text-gray-500 border border-gray-300 hover:bg-gray-200'}
                        `}
                      >
                        {idx + 1}
                      </div>
                    );
                  })}
                </div>
              </div>
            );
          })}
        </div>

        {/* Footer */}
        <div className="px-6 py-4 bg-gray-50 border-t text-center">
          <p className="text-sm text-gray-500">
            Сұраққа өту үшін нөмірге басыңыз
          </p>
        </div>
      </div>
    </div>
  );
};

export default AnswerMapModal;
