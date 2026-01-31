import React from 'react';
import { X, BookOpen, CheckCircle } from 'lucide-react';
import { SubjectId, Question, UserAnswers } from '../../types';
import { SUBJECTS } from '../../constants';

interface SectionsModalProps {
  isOpen: boolean;
  onClose: () => void;
  questions: Question[];
  answers: UserAnswers;
  currentSubjectId: SubjectId;
  onSelectSubject: (subjectId: SubjectId) => void;
}

const SectionsModal: React.FC<SectionsModalProps> = ({
  isOpen,
  onClose,
  questions,
  answers,
  currentSubjectId,
  onSelectSubject,
}) => {
  if (!isOpen) return null;

  const subjectList = Object.values(SUBJECTS);

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-[100]" onClick={onClose}>
      <div 
        className="bg-white rounded-lg shadow-2xl w-[90%] max-w-md max-h-[80vh] overflow-hidden animate-fade-in"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="bg-[#3498DB] text-white px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <BookOpen className="w-6 h-6" />
            <h2 className="text-lg font-bold">Бөлімдер</h2>
          </div>
          <button onClick={onClose} className="hover:bg-white/20 p-1 rounded transition">
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Content */}
        <div className="p-4 space-y-3">
          {subjectList.map((subject) => {
            const subjectQuestions = questions.filter(q => q.subjectId === subject.id);
            const answeredCount = subjectQuestions.filter(q => answers[q.id] && answers[q.id].length > 0).length;
            const totalCount = subjectQuestions.length;
            const isActive = currentSubjectId === subject.id;
            const isComplete = answeredCount === totalCount && totalCount > 0;

            return (
              <div
                key={subject.id}
                onClick={() => {
                  onSelectSubject(subject.id);
                  onClose();
                }}
                className={`
                  p-4 rounded-lg border-2 cursor-pointer transition-all
                  ${isActive 
                    ? 'border-[#3498DB] bg-blue-50 shadow-md' 
                    : 'border-gray-200 hover:border-[#3498DB] hover:bg-gray-50'}
                `}
              >
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-3">
                    {isComplete ? (
                      <CheckCircle className="w-6 h-6 text-green-500" />
                    ) : (
                      <div className={`w-6 h-6 rounded-full border-2 flex items-center justify-center text-xs font-bold
                        ${isActive ? 'border-[#3498DB] text-[#3498DB]' : 'border-gray-400 text-gray-400'}
                      `}>
                        {subjectList.indexOf(subject) + 1}
                      </div>
                    )}
                    <div>
                      <div className={`font-bold ${isActive ? 'text-[#3498DB]' : 'text-gray-800'}`}>
                        {subject.name}
                      </div>
                      <div className="text-sm text-gray-500">
                        {answeredCount} / {totalCount} сұрақ
                      </div>
                    </div>
                  </div>
                  
                  {/* Progress Bar */}
                  <div className="w-20 h-2 bg-gray-200 rounded-full overflow-hidden">
                    <div 
                      className="h-full bg-green-500 transition-all duration-300"
                      style={{ width: `${totalCount > 0 ? (answeredCount / totalCount) * 100 : 0}%` }}
                    />
                  </div>
                </div>
              </div>
            );
          })}
        </div>

        {/* Footer */}
        <div className="px-6 py-4 bg-gray-50 border-t text-center">
          <p className="text-sm text-gray-500">
            Бөлімге өту үшін басыңыз
          </p>
        </div>
      </div>
    </div>
  );
};

export default SectionsModal;
