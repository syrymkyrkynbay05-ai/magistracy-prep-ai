import React from 'react';
import { BookOpen, Brain, Clock, Database, Globe, ArrowRight, Sparkles, CheckCircle2 } from 'lucide-react';
import { SUBJECTS } from '../constants';
import { SubjectId } from '../types';

interface WelcomeScreenProps {
  onStart: (name: string) => void;
  isLoading: boolean;
  onViewProgram: () => void;
}

const WelcomeScreen: React.FC<WelcomeScreenProps> = ({ onStart, isLoading, onViewProgram }) => {
  const [name, setName] = React.useState('');
  const [error, setError] = React.useState(false);

  const handleStart = () => {
    if (!name.trim()) {
      setError(true);
      return;
    }
    onStart(name.trim());
  };
  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-6 relative overflow-hidden">
      {/* Fluent Gradient Background */}
      <div className="absolute top-0 left-0 w-full h-full bg-[#F8F9FB] -z-20"></div>
      <div className="absolute top-[-20%] right-[-10%] w-[600px] h-[600px] bg-blue-100/40 rounded-full blur-3xl -z-10 pointer-events-none"></div>
      <div className="absolute bottom-[-10%] left-[-10%] w-[500px] h-[500px] bg-indigo-100/40 rounded-full blur-3xl -z-10 pointer-events-none"></div>

      <div className="max-w-5xl w-full">
        {/* Header Section */}
        <div className="text-center mb-12 space-y-4">
          <div className="inline-flex items-center px-3 py-1 bg-white border border-blue-100 rounded-full shadow-sm mb-4">
            <Sparkles className="w-4 h-4 text-blue-600 mr-2" />
            <span className="text-sm font-medium text-blue-700">AI-Powered Exam Simulator</span>
          </div>
          <h1 className="text-4xl md:text-5xl font-bold text-slate-900 tracking-tight leading-tight">
            Магистратураға Дайындық (КТ)
          </h1>
          <p className="text-lg text-slate-500 max-w-2xl mx-auto leading-relaxed">
            Кешенді Тестілеуге арналған заманауи дайындық платформасы. 
            Жасанды интеллект көмегімен нақты емтихан форматында жаттығыңыз.
          </p>
        </div>

        {/* Info Cards (Floating Depth) */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
          <div className="bg-white p-6 rounded-2xl shadow-[0_2px_8px_rgba(0,0,0,0.04)] border border-slate-100/50 flex items-start space-x-4 transition-transform hover:-translate-y-1 duration-300">
            <div className="w-12 h-12 bg-blue-50 rounded-xl flex items-center justify-center text-blue-600 flex-shrink-0">
              <Clock className="w-6 h-6" />
            </div>
            <div>
              <h3 className="text-lg font-semibold text-slate-900 mb-1">235 Минут</h3>
              <p className="text-slate-500 text-sm leading-relaxed">
                Нақты уақыт режиміндегі толық симуляция. Уақытты тиімді басқаруды үйреніңіз.
              </p>
            </div>
          </div>
          <div className="bg-white p-6 rounded-2xl shadow-[0_2px_8px_rgba(0,0,0,0.04)] border border-slate-100/50 flex items-start space-x-4 transition-transform hover:-translate-y-1 duration-300">
            <div className="w-12 h-12 bg-emerald-50 rounded-xl flex items-center justify-center text-emerald-600 flex-shrink-0">
              <CheckCircle2 className="w-6 h-6" />
            </div>
            <div>
              <h3 className="text-lg font-semibold text-slate-900 mb-1">150 Максималды балл</h3>
              <p className="text-slate-500 text-sm leading-relaxed">
                Шекті балл жинауға және грантқа түсу мүмкіндігін арттыруға бағытталған.
              </p>
            </div>
          </div>
        </div>

        {/* Subject Grid */}
        <div className="mb-12">
          <h2 className="text-xl font-semibold text-slate-800 mb-6 px-1">Тест Құрылымы</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            {[
              { id: SubjectId.ENGLISH, icon: Globe, color: 'text-indigo-600', bg: 'bg-indigo-50' },
              { id: SubjectId.TGO, icon: Brain, color: 'text-violet-600', bg: 'bg-violet-50' },
              { id: SubjectId.ALGO, icon: BookOpen, color: 'text-rose-600', bg: 'bg-rose-50' },
              { id: SubjectId.DB, icon: Database, color: 'text-amber-600', bg: 'bg-amber-50' }
            ].map((item) => (
              <div key={item.id} className="group bg-white p-5 rounded-2xl border border-slate-200 hover:border-blue-300 hover:shadow-md transition-all duration-200">
                <div className={`${item.bg} w-10 h-10 rounded-xl flex items-center justify-center ${item.color} mb-3 group-hover:scale-110 transition-transform`}>
                  <item.icon className="w-5 h-5" />
                </div>
                <h4 className="font-semibold text-slate-900 mb-1">{SUBJECTS[item.id].name}</h4>
                <p className="text-xs text-slate-500 font-medium">
                  {SUBJECTS[item.id].totalQuestions} сұрақ | {SUBJECTS[item.id].maxScore} балл
                </p>
              </div>
            ))}
          </div>
        </div>

        {/* Name Input Section */}
        <div className="max-w-md mx-auto mb-8 w-full">
          <label className="block text-sm font-semibold text-slate-700 mb-2 ml-1">Аты-жөніңізді енгізіңіз</label>
          <input
            type="text"
            value={name}
            onChange={(e) => {
              setName(e.target.value);
              if (error) setError(false);
            }}
            placeholder="Мысалы: Айтбаев Жасұлан"
            className={`
              w-full px-5 py-4 rounded-xl border-2 transition-all duration-200 outline-none
              ${error ? 'border-red-400 bg-red-50 focus:border-red-500' : 'border-slate-200 focus:border-blue-500 focus:bg-white bg-white/50'}
            `}
          />
          {error && <p className="text-red-500 text-xs mt-2 ml-1 font-medium">Тестті бастау үшін аты-жөніңізді жазуыңыз керек</p>}
        </div>

        {/* CTA Section */}
        <div className="flex flex-col items-center">
          <div className="flex flex-col sm:flex-row items-center gap-4">
            <button
              onClick={handleStart}
              disabled={isLoading}
              className={`
                relative group overflow-hidden rounded-xl px-10 py-4 
                bg-[#0078d4] text-white font-semibold text-lg shadow-lg shadow-blue-500/30 
                transition-all duration-300 hover:shadow-blue-500/40 active:scale-[0.98]
                disabled:opacity-70 disabled:cursor-wait
              `}
            >
              <div className="absolute inset-0 w-full h-full bg-gradient-to-r from-transparent via-white/10 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-700 ease-in-out"></div>
              <div className="flex items-center gap-3">
                {isLoading ? (
                  <>
                    <svg className="animate-spin h-5 w-5 text-white/90" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    <span>Дайындалуда...</span>
                  </>
                ) : (
                  <>
                    <span>Тестті Бастау</span>
                    <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
                  </>
                )}
              </div>
            </button>

            <button
              onClick={onViewProgram}
              className="flex items-center gap-2 px-8 py-4 rounded-xl border border-slate-200 bg-white text-slate-700 font-semibold hover:bg-slate-50 transition-all active:scale-95"
            >
              <BookOpen className="w-5 h-5 text-blue-600" />
              <span>Бағдарламаны Көру</span>
            </button>
          </div>
          <p className="mt-4 text-sm text-slate-400 font-medium">Gemini AI арқылы генерацияланады</p>
        </div>
      </div>
    </div>
  );
};

export default WelcomeScreen;