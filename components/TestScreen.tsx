import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Navigate } from 'react-router-dom';
import { Question, SubjectId, UserAnswers, QuestionType } from '../types';
import { SUBJECTS } from '../constants';
import { Menu, User, FileText, Map, Calculator, Table, FlaskConical, LogOut } from 'lucide-react';

// Import Modals
import SectionsModal from './modals/SectionsModal';
import AnswerMapModal from './modals/AnswerMapModal';
import CalculatorModal from './modals/CalculatorModal';
import PeriodicTableModal from './modals/PeriodicTableModal';
import SolubilityTableModal from './modals/SolubilityTableModal';
import AudioPlayer from './AudioPlayer';

interface TestScreenProps {
  questions: Question[];
  durationMinutes: number;
  onFinish: (answers: UserAnswers) => void;
  userName: string;
}

const TestScreen: React.FC<TestScreenProps> = ({ questions, durationMinutes, onFinish, userName }) => {
  const { subjectId, qIndex } = useParams<{ subjectId: string; qIndex: string }>();
  const navigate = useNavigate();

  // Available audio dialogues (10 total)
  const AUDIO_DIALOGUES = [
    { id: 1, file: '/audio/dialogue_1.wav', title: 'Travel to Sydney' },
    { id: 2, file: '/audio/dialogue_2.wav', title: 'Birthday Party' },
    { id: 3, file: '/audio/dialogue_3.wav', title: 'University Library' },
    { id: 4, file: '/audio/dialogue_4.wav', title: 'Shopping Return' },
    { id: 5, file: '/audio/dialogue_5.wav', title: 'Job Interview' },
    { id: 6, file: '/audio/dialogue_6.wav', title: 'Doctor Appointment' },
    { id: 7, file: '/audio/dialogue_7.wav', title: 'Asking Directions' },
    { id: 8, file: '/audio/dialogue_8.wav', title: 'Renting Apartment' },
    { id: 9, file: '/audio/dialogue_9.wav', title: 'Sports Club' },
    { id: 10, file: '/audio/dialogue_10.wav', title: 'Ordering Food' },
  ];

  // Randomly select 2 dialogues on component mount (persisted for this test session)
  const [selectedDialogues] = useState(() => {
    const shuffled = [...AUDIO_DIALOGUES].sort(() => Math.random() - 0.5);
    return [shuffled[0], shuffled[1]];
  });

  // State
  const [answers, setAnswers] = useState<UserAnswers>({});
  
  // Resolve current state from URL
  const currentSubjectId = (subjectId as SubjectId) || SubjectId.ENGLISH;
  const currentQuestionIndex = qIndex ? parseInt(qIndex) - 1 : 0;

  const currentSubjectQuestions = questions.filter(q => q.subjectId === currentSubjectId);
  const currentQuestion = currentSubjectQuestions[currentQuestionIndex];

  // If URL is invalid, redirect to first question of current subject
  if (!currentQuestion && currentSubjectQuestions.length > 0) {
    return <Navigate to={`/test/${currentSubjectId}/q/1`} replace />;
  }

  const currentIndex = currentQuestionIndex;
  const currentQuestionId = currentQuestion?.id;

  // Get current audio dialogue based on question index (КТ format: 16 listening questions)
  // Questions 1-8: Audio 1, Questions 9-16: Audio 2
  const getCurrentDialogue = () => {
    if (currentIndex < 8) return selectedDialogues[0];
    if (currentIndex < 16) return selectedDialogues[1];
    return null;
  };

  // Modal States
  const [showSections, setShowSections] = useState(false);
  const [showAnswerMap, setShowAnswerMap] = useState(false);
  const [showCalculator, setShowCalculator] = useState(false);
  const [showPeriodicTable, setShowPeriodicTable] = useState(false);
  const [showSolubilityTable, setShowSolubilityTable] = useState(false);

  // Anti-cheat and Refresh Prevention
  useEffect(() => {
    // 1. Prevent refresh
    const handleBeforeUnload = (e: BeforeUnloadEvent) => {
      e.preventDefault();
      e.returnValue = '';
    };

    // 2. Prevent copy and right click
    const handleContextMenu = (e: MouseEvent) => e.preventDefault();
    const handleCopy = (e: ClipboardEvent) => e.preventDefault();
    const handleKeydown = (e: KeyboardEvent) => {
      // Block Ctrl+C, Ctrl+V, Ctrl+U (source), F12 (inspect)
      if ((e.ctrlKey && (e.key === 'c' || e.key === 'v' || e.key === 'u')) || e.key === 'F12') {
        e.preventDefault();
      }
    };

    window.addEventListener('beforeunload', handleBeforeUnload);
    window.addEventListener('contextmenu', handleContextMenu);
    window.addEventListener('copy', handleCopy);
    window.addEventListener('keydown', handleKeydown);

    return () => {
      window.removeEventListener('beforeunload', handleBeforeUnload);
      window.removeEventListener('contextmenu', handleContextMenu);
      window.removeEventListener('copy', handleCopy);
      window.removeEventListener('keydown', handleKeydown);
    };
  }, []);

  // Helpers
  const handleAnswer = (optionId: string) => {
    if (!currentQuestion) return; // Use the derived currentQuestion

    setAnswers(prev => {
      const currentSelection = prev[currentQuestionId] || [];
      if (currentQuestion.type === QuestionType.SINGLE) {
        return { ...prev, [currentQuestionId]: [optionId] };
      } else {
        if (currentSelection.includes(optionId)) {
          return { ...prev, [currentQuestionId]: currentSelection.filter(id => id !== optionId) };
        } else {
          return { ...prev, [currentQuestionId]: [...currentSelection, optionId] };
        }
      }
    });
  };

  const handleSelectQuestion = (questionId: string) => {
    const q = questions.find(q => q.id === questionId);
    if (q) {
      const sQuestions = questions.filter(sq => sq.subjectId === q.subjectId);
      const idx = sQuestions.findIndex(sq => sq.id === questionId);
      navigate(`/test/${q.subjectId}/q/${idx + 1}`);
    }
  };



  const handleNext = () => {
    if (currentIndex < currentSubjectQuestions.length - 1) {
      navigate(`/test/${currentSubjectId}/q/${currentIndex + 2}`);
    }
  };

  const handlePrev = () => {
    if (currentIndex > 0) {
      navigate(`/test/${currentSubjectId}/q/${currentIndex}`);
    }
  };

  const handleNextSubject = () => {
    const subjectIds = Object.values(SubjectId);
    const currIdx = subjectIds.indexOf(currentSubjectId);
    if(currIdx < subjectIds.length - 1) {
        navigate(`/test/${subjectIds[currIdx + 1]}/q/1`);
    } else {
        if(window.confirm("Бұл соңғы пән. Тестті аяқтауға сенімдісіз бе?")) {
            onFinish(answers);
        }
    }
  };

  const handleFinish = () => {
    if(window.confirm("Тестті аяқтауға сенімдісіз бе?")) {
      onFinish(answers);
    }
  };

  // Sidebar Tools
  const tools = [
    { icon: <User className="w-6 h-6" />, label: userName.split(' ')[0] || "Жасұлан", onClick: () => {} },
    { icon: <FileText className="w-6 h-6" />, label: "Бөлімдер", onClick: () => setShowSections(true) },
    { icon: <Map className="w-6 h-6" />, label: "Жауап картасы", onClick: () => setShowAnswerMap(true) },
    { icon: <Calculator className="w-6 h-6" />, label: "Калькулятор", onClick: () => setShowCalculator(true) },
    { icon: <Table className="w-6 h-6" />, label: "Менделеев кестесі", onClick: () => setShowPeriodicTable(true) },
    { icon: <FlaskConical className="w-6 h-6" />, label: "Ерігіштік кестесі", onClick: () => setShowSolubilityTable(true) },
  ];

  if (!currentQuestion) return <div>Loading...</div>;

  return (
    <div className="flex flex-col h-screen bg-[#F8F9FB] font-sans overflow-hidden">
      {/* 1. Full Width Top Header (Dark Blue) - Mobile Responsive */}
      <header className="bg-[#348FE2] h-[48px] md:h-[48px] flex items-center justify-between px-2 md:px-4 text-white shadow-md z-50 shrink-0">
          <div className="flex items-center gap-2 md:gap-4">
              <Menu className="w-5 h-5 md:w-6 md:h-6 cursor-pointer opacity-90 hover:opacity-100" />
              <div className="font-semibold text-xs md:text-base tracking-wide flex items-center gap-2 truncate max-w-[120px] md:max-w-none">
                 <span>{userName || 'Пердеев Азамат'}</span>
              </div>
          </div>
          <button 
              onClick={handleNextSubject}
              className="bg-white text-[#348FE2] px-2 md:px-4 py-1 rounded-[3px] text-[10px] md:text-xs font-bold hover:bg-slate-50 transition shadow-sm uppercase tracking-tight whitespace-nowrap"
          >
              Келесі пән &gt;
          </button>
      </header>

      {/* 2. Main Layout (Sidebar + Content) */}
      <div className="flex flex-1 overflow-hidden">
          
          {/* Sidebar (Left, Fixed Width) - Hidden on Mobile */}
          <div className="hidden md:flex w-[100px] bg-[#56CCF2] flex-col items-center py-4 text-white border-r border-[#4DBBE0] z-40">
              {/* Tools */}
              <div className="flex flex-col gap-4 w-full">
                  {tools.map((tool, index) => (
                      <div 
                          key={index}
                          onClick={tool.onClick}
                          className="flex flex-col items-center gap-1 cursor-pointer hover:bg-white/20 w-full py-2 transition rounded-md"
                      >
                          <div className="p-1">{tool.icon}</div>
                          <span className="text-[10px] font-medium leading-tight px-1 text-center">{tool.label}</span>
                      </div>
                  ))}
              </div>

              {/* Finish Button */}
              <div className="mt-auto mb-4 w-full">
                   <button 
                      onClick={handleFinish}
                      className="flex flex-col items-center gap-1 cursor-pointer hover:bg-red-500/20 w-full py-2 transition text-red-100"
                   >
                      <LogOut className="w-6 h-6" />
                      <span className="text-[10px]">Аяқтау</span>
                   </button>
              </div>
          </div>

          {/* Right Content Area */}
          <div className="flex-1 flex flex-col bg-white overflow-hidden relative">
              
              {/* Question Strip (Gray Background per screenshot) */}
              <div className="bg-[#EAEAEA] border-b border-gray-300 py-2 px-2 overflow-x-auto custom-scrollbar shrink-0 shadow-inner">
                  <div className="flex items-center gap-1.5 min-w-max px-2">
                  {currentSubjectQuestions.map((q, idx) => {
                      const isAnswered = answers[q.id] && answers[q.id].length > 0;
                      const isCurrent = idx === currentQuestionIndex;
                      
                      return (
                          <div 
                              key={q.id}
                              onClick={() => navigate(`/test/${currentSubjectId}/q/${idx + 1}`)}
                              className={`
                                  w-8 h-8 flex items-center justify-center rounded-[3px] cursor-pointer text-sm font-bold transition-all select-none border shadow-sm
                                  ${isCurrent 
                                      ? 'bg-[#3498DB] text-white border-[#2980B9] ring-2 ring-blue-300 z-10' 
                                      : isAnswered 
                                          ? 'bg-[#2ECC71] text-white border-[#27AE60]' 
                                          : 'bg-gradient-to-b from-white to-gray-50 text-blue-400 border-gray-300 hover:border-blue-400 hover:text-blue-500'}
                              `}
                          >
                              {idx + 1}
                          </div>
                      );
                  })}
                  </div>
              </div>

              {/* Main Question Card Area */}
              <div className="flex-1 overflow-y-auto bg-white p-4 md:px-8 md:py-6">
                  <div className="max-w-6xl mx-auto h-full flex flex-col">
                      
                      {/* Nav Bar - Mobile Responsive */}
                      <div className="flex flex-col md:flex-row items-center justify-between pb-4 border-b-2 border-slate-200 mb-4 md:mb-6 gap-3 md:gap-0">
                          <button 
                              onClick={handlePrev}
                              disabled={currentIndex === 0}
                              className="w-full md:w-auto bg-[#3498DB] text-white px-4 md:px-5 py-2 rounded-[4px] text-sm font-bold shadow hover:bg-[#2980B9] disabled:opacity-50 disabled:shadow-none transition-colors order-2 md:order-1"
                          >
                              &lt; Алдыңғы
                          </button>
                          
                          <div className="text-center order-1 md:order-2">
                             <div className="text-sm md:text-lg font-bold text-slate-800 uppercase tracking-tight">
                                {SUBJECTS[currentSubjectId].name}
                             </div>
                             <span className="text-slate-500 font-semibold text-xs md:hidden">Сұрақ {currentIndex + 1}/{currentSubjectQuestions.length}</span>
                          </div>

                          <div className="flex items-center gap-2 md:gap-4 w-full md:w-auto order-3">
                              <span className="hidden md:inline text-slate-500 font-semibold text-sm">Сұрақ № {currentIndex + 1}</span>
                              <button 
                                  onClick={handleNext}
                                  disabled={currentIndex === currentSubjectQuestions.length - 1}
                                  className="flex-1 md:flex-none bg-[#3498DB] text-white px-4 md:px-6 py-2 rounded-[4px] text-sm font-bold shadow hover:bg-[#2980B9] disabled:opacity-50 disabled:shadow-none transition-colors"
                              >
                                  Келесі &gt;
                              </button>
                          </div>
                      </div>

                      {/* Question Content */}
                      <div className="flex-1">
                          {/* Audio Player for English Listening Section (КТ: First 16 questions) */}
                          {currentSubjectId === SubjectId.ENGLISH && currentIndex < 16 && getCurrentDialogue() && (
                              <div className="mb-6">
                                  <AudioPlayer src={getCurrentDialogue()!.file} />
                              </div>
                          )}

                          {/* Language Level Badge for English */}
                          {currentSubjectId === SubjectId.ENGLISH && currentQuestion.languageLevel && (
                              <div className="mb-3">
                                  <span className={`
                                      inline-flex items-center px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider
                                      ${currentQuestion.languageLevel === 'A1' ? 'bg-green-100 text-green-700' : ''}
                                      ${currentQuestion.languageLevel === 'A2' ? 'bg-blue-100 text-blue-700' : ''}
                                      ${currentQuestion.languageLevel === 'B1' ? 'bg-yellow-100 text-yellow-700' : ''}
                                      ${currentQuestion.languageLevel === 'B2' ? 'bg-orange-100 text-orange-700' : ''}
                                      ${currentQuestion.languageLevel === 'C' ? 'bg-red-100 text-red-700' : ''}
                                  `}>
                                      {currentQuestion.languageLevel} деңгей
                                  </span>
                              </div>
                          )}

                          <div className="text-2xl font-serif text-slate-900 leading-relaxed mb-6 font-medium">
                              {currentQuestion.text}
                          </div>

                          {/* Reading Passage for Comprehension Questions */}
                          {currentQuestion.readingPassage && (
                            <div className="bg-gradient-to-r from-amber-50 to-orange-50 border border-amber-200 rounded-xl p-5 mb-6 shadow-sm">
                                <div className="prose prose-sm max-w-none text-slate-700 leading-relaxed">
                                    <p className="whitespace-pre-line">{currentQuestion.readingPassage}</p>
                                </div>
                            </div>
                          )}

                          {currentQuestion.codeSnippet && (
                            <div className="bg-[#1E1E1E] text-white p-5 rounded-md shadow-inner font-mono text-sm mb-8 overflow-x-auto border border-gray-700">
                                <pre>{currentQuestion.codeSnippet}</pre>
                            </div>
                          )}

                          <div className="grid gap-4 max-w-4xl">
                              {currentQuestion.options.map((option, idx) => {
                                  const isSelected = (answers[currentQuestionId] || []).includes(option.id);
                                  const letter = String.fromCharCode(65 + idx);
                                  
                                  return (
                                      <div 
                                          key={option.id}
                                          onClick={() => handleAnswer(option.id)}
                                          className="flex items-start gap-4 p-2 rounded hover:bg-slate-50 cursor-pointer group select-none transition-colors"
                                      >
                                          {/* Checkbox Square Style for ALL Types */}
                                          <div className={`
                                              w-6 h-6 border-2 flex items-center justify-center bg-white rounded-[3px] shadow-sm mt-0.5
                                              ${isSelected ? 'border-[#3498DB] bg-blue-50' : 'border-gray-300 group-hover:border-[#3498DB]'}
                                          `}>
                                              {isSelected && <div className="w-3.5 h-3.5 bg-[#3498DB] rounded-[1px]"></div>}
                                          </div>

                                          <div className="text-lg text-slate-800 font-serif leading-snug pt-0.5">
                                              <span className="font-bold mr-2 uppercase">{letter})</span>
                                              {option.text}
                                          </div>
                                      </div>
                                  );
                              })}
                          </div>
                      </div>

                  </div>
              </div>

          </div>
      </div>

      {/* MODALS */}
      <SectionsModal 
        isOpen={showSections}
        onClose={() => setShowSections(false)}
        questions={questions}
        answers={answers}
        currentSubjectId={currentSubjectId}
        onSelectSubject={(id) => navigate(`/test/${id}/q/1`)}
      />

      <AnswerMapModal 
        isOpen={showAnswerMap}
        onClose={() => setShowAnswerMap(false)}
        questions={questions}
        answers={answers}
        currentQuestionId={currentQuestionId}
        onSelectQuestion={handleSelectQuestion}
      />

      <CalculatorModal 
        isOpen={showCalculator}
        onClose={() => setShowCalculator(false)}
      />

      <PeriodicTableModal 
        isOpen={showPeriodicTable}
        onClose={() => setShowPeriodicTable(false)}
      />

      <SolubilityTableModal 
        isOpen={showSolubilityTable}
        onClose={() => setShowSolubilityTable(false)}
      />

      {/* Mobile Bottom Navigation - Only visible on mobile */}
      <div className="md:hidden fixed bottom-0 left-0 right-0 bg-[#56CCF2] border-t border-[#4DBBE0] flex justify-around items-center py-2 px-1 z-50 safe-area-bottom">
        <button onClick={() => setShowSections(true)} className="flex flex-col items-center text-white p-1">
          <FileText className="w-5 h-5" />
          <span className="text-[9px] mt-0.5">Бөлімдер</span>
        </button>
        <button onClick={() => setShowAnswerMap(true)} className="flex flex-col items-center text-white p-1">
          <Map className="w-5 h-5" />
          <span className="text-[9px] mt-0.5">Карта</span>
        </button>
        <button onClick={() => setShowCalculator(true)} className="flex flex-col items-center text-white p-1">
          <Calculator className="w-5 h-5" />
          <span className="text-[9px] mt-0.5">Есептеу</span>
        </button>
        <button onClick={handleFinish} className="flex flex-col items-center text-red-100 p-1">
          <LogOut className="w-5 h-5" />
          <span className="text-[9px] mt-0.5">Аяқтау</span>
        </button>
      </div>
    </div>
  );
};

export default TestScreen;