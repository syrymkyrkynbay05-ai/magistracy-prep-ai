import React from 'react';
import { BookOpen, Brain, Clock, Database, Globe, ArrowRight, CheckCircle2, Users, Award, Zap, Target, GraduationCap, TrendingUp, Shield, Star } from 'lucide-react';
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

  const stats = [
    { value: "5000+", label: "Тапсырушылар", icon: Users },
    { value: "92%", label: "Өту көрсеткіші", icon: TrendingUp },
    { value: "150", label: "Макс балл", icon: Award },
    { value: "24/7", label: "Қолжетімділік", icon: Clock },
  ];

  const features = [
    { 
      icon: Target, 
      title: "Нақты емтихан форматы",
      description: "ҰБТ-ның толық симуляциясы, нақты уақыт режимінде"
    },
    { 
      icon: Brain, 
      title: "Адаптивті оқыту",
      description: "Сіздің деңгейіңізге бейімделген сұрақтар"
    },
    { 
      icon: Shield, 
      title: "Толық дайындық",
      description: "4 пән бойынша кешенді тестілеу"
    },
    { 
      icon: Zap, 
      title: "Жылдам нәтиже",
      description: "Тесттен кейін толық талдау мен ұсыныстар"
    },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50/30 to-indigo-50/50">
      
      {/* Hero Section */}
      <section className="relative overflow-hidden">
        {/* Background Elements */}
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
          <div className="absolute -top-40 -right-40 w-80 h-80 md:w-[500px] md:h-[500px] bg-gradient-to-br from-blue-400/20 to-indigo-400/20 rounded-full blur-3xl"></div>
          <div className="absolute -bottom-40 -left-40 w-80 h-80 md:w-[400px] md:h-[400px] bg-gradient-to-tr from-violet-400/20 to-purple-400/20 rounded-full blur-3xl"></div>
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-gradient-to-r from-blue-200/10 to-indigo-200/10 rounded-full blur-3xl"></div>
        </div>

        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 md:pt-20 pb-16 md:pb-24">
          {/* Badge */}
          <div className="flex justify-center mb-6 md:mb-8">
            <div className="inline-flex items-center gap-2 px-4 py-2 bg-white/80 backdrop-blur-sm border border-blue-100 rounded-full shadow-sm">
              <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
              <span className="text-xs md:text-sm font-medium text-slate-700">2025-2026 оқу жылына дайындық</span>
            </div>
          </div>

          {/* Main Heading */}
          <div className="text-center max-w-4xl mx-auto">
            <h1 className="text-3xl md:text-5xl lg:text-6xl font-bold text-slate-900 tracking-tight leading-tight mb-4 md:mb-6">
              <span className="bg-gradient-to-r from-blue-600 via-indigo-600 to-violet-600 bg-clip-text text-transparent">
                Магистратураға
              </span>
              <br />
              <span className="text-slate-800">Дайындық Платформасы</span>
            </h1>
            
            <p className="text-base md:text-xl text-slate-600 max-w-2xl mx-auto mb-8 md:mb-10 leading-relaxed px-4">
              Қазақстанның үздік университеттеріне түсуге дайындалыңыз. 
              Кешенді тестілеу, егжей-тегжейлі талдау және жеке ұсыныстар.
            </p>

            {/* Stats */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6 max-w-3xl mx-auto mb-10 md:mb-12">
              {stats.map((stat, idx) => (
                <div key={idx} className="bg-white/60 backdrop-blur-sm rounded-2xl p-4 md:p-5 border border-white shadow-sm hover:shadow-md transition-shadow">
                  <stat.icon className="w-5 h-5 md:w-6 md:h-6 text-blue-600 mx-auto mb-2" />
                  <div className="text-xl md:text-2xl font-bold text-slate-900">{stat.value}</div>
                  <div className="text-xs md:text-sm text-slate-500 font-medium">{stat.label}</div>
                </div>
              ))}
            </div>

            {/* CTA Section */}
            <div className="bg-white/80 backdrop-blur-sm rounded-3xl p-6 md:p-8 shadow-xl shadow-blue-900/5 border border-white max-w-xl mx-auto">
              <div className="flex items-center gap-2 mb-4">
                <GraduationCap className="w-5 h-5 text-blue-600" />
                <span className="text-sm font-semibold text-slate-700">Тестті бастау үшін</span>
              </div>
              
              <input
                type="text"
                value={name}
                onChange={(e) => {
                  setName(e.target.value);
                  if (error) setError(false);
                }}
                placeholder="Аты-жөніңізді жазыңыз"
                className={`
                  w-full px-5 py-4 rounded-xl border-2 transition-all duration-200 outline-none text-center text-lg
                  ${error 
                    ? 'border-red-400 bg-red-50 focus:border-red-500 placeholder-red-300' 
                    : 'border-slate-200 focus:border-blue-500 focus:bg-white bg-slate-50/50 placeholder-slate-400'}
                `}
              />
              {error && (
                <p className="text-red-500 text-sm mt-2 font-medium flex items-center justify-center gap-1">
                  <span>⚠️</span> Аты-жөніңізді жазуыңыз керек
                </p>
              )}

              <div className="flex flex-col sm:flex-row gap-3 mt-5">
                <button
                  onClick={handleStart}
                  disabled={isLoading}
                  className="flex-1 group relative overflow-hidden rounded-xl px-6 py-4 bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-semibold text-lg shadow-lg shadow-blue-500/25 transition-all duration-300 hover:shadow-blue-500/40 hover:scale-[1.02] active:scale-[0.98] disabled:opacity-70 disabled:cursor-wait"
                >
                  <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-700"></div>
                  <div className="relative flex items-center justify-center gap-2">
                    {isLoading ? (
                      <>
                        <svg className="animate-spin h-5 w-5" viewBox="0 0 24 24">
                          <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none"></circle>
                          <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                        </svg>
                        <span>Жүктелуде...</span>
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
                  className="px-6 py-4 rounded-xl border-2 border-slate-200 bg-white text-slate-700 font-semibold hover:bg-slate-50 hover:border-slate-300 transition-all flex items-center justify-center gap-2"
                >
                  <BookOpen className="w-5 h-5 text-blue-600" />
                  <span>Бағдарлама</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Subjects Section */}
      <section className="py-12 md:py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-10 md:mb-14">
            <span className="inline-block px-4 py-1.5 bg-blue-50 text-blue-700 rounded-full text-xs md:text-sm font-semibold mb-4">
              Тест құрылымы
            </span>
            <h2 className="text-2xl md:text-4xl font-bold text-slate-900 mb-3">
              4 пән бойынша кешенді тестілеу
            </h2>
            <p className="text-slate-500 max-w-xl mx-auto text-sm md:text-base">
              Нағыз емтихан форматында 235 минут ішінде 130 сұрақ
            </p>
          </div>

          <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6">
            {[
              { id: SubjectId.ENGLISH, icon: Globe, gradient: 'from-blue-500 to-indigo-600', bg: 'bg-blue-50' },
              { id: SubjectId.TGO, icon: Brain, gradient: 'from-violet-500 to-purple-600', bg: 'bg-violet-50' },
              { id: SubjectId.ALGO, icon: BookOpen, gradient: 'from-rose-500 to-pink-600', bg: 'bg-rose-50' },
              { id: SubjectId.DB, icon: Database, gradient: 'from-amber-500 to-orange-600', bg: 'bg-amber-50' }
            ].map((item) => (
              <div 
                key={item.id} 
                className="group relative bg-white rounded-2xl md:rounded-3xl border border-slate-100 p-5 md:p-6 hover:shadow-xl hover:shadow-slate-200/50 transition-all duration-300 hover:-translate-y-1"
              >
                <div className={`w-12 h-12 md:w-14 md:h-14 rounded-xl md:rounded-2xl bg-gradient-to-br ${item.gradient} flex items-center justify-center text-white mb-4 shadow-lg group-hover:scale-110 transition-transform`}>
                  <item.icon className="w-6 h-6 md:w-7 md:h-7" />
                </div>
                <h3 className="font-bold text-slate-900 text-base md:text-lg mb-1">
                  {SUBJECTS[item.id].name}
                </h3>
                <div className="flex items-center gap-2 text-sm text-slate-500">
                  <span className="font-semibold text-slate-700">{SUBJECTS[item.id].totalQuestions}</span>
                  <span>сұрақ</span>
                  <span className="text-slate-300">•</span>
                  <span className="font-semibold text-slate-700">{SUBJECTS[item.id].maxScore}</span>
                  <span>балл</span>
                </div>
                <div className="mt-3 h-1.5 bg-slate-100 rounded-full overflow-hidden">
                  <div className={`h-full bg-gradient-to-r ${item.gradient} rounded-full`} style={{ width: `${(SUBJECTS[item.id].maxScore / 150) * 100}%` }}></div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-12 md:py-20 bg-gradient-to-b from-slate-50 to-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-10 md:mb-14">
            <span className="inline-block px-4 py-1.5 bg-indigo-50 text-indigo-700 rounded-full text-xs md:text-sm font-semibold mb-4">
              Неге біз?
            </span>
            <h2 className="text-2xl md:text-4xl font-bold text-slate-900 mb-3">
              Платформа артықшылықтары
            </h2>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {features.map((feature, idx) => (
              <div 
                key={idx}
                className="bg-white rounded-2xl p-6 border border-slate-100 hover:border-blue-200 hover:shadow-lg transition-all duration-300 group"
              >
                <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-blue-50 to-indigo-50 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                  <feature.icon className="w-6 h-6 text-blue-600" />
                </div>
                <h3 className="font-bold text-slate-900 mb-2">{feature.title}</h3>
                <p className="text-sm text-slate-500 leading-relaxed">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section className="py-12 md:py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-10 md:mb-14">
            <span className="inline-block px-4 py-1.5 bg-green-50 text-green-700 rounded-full text-xs md:text-sm font-semibold mb-4">
              Пікірлер
            </span>
            <h2 className="text-2xl md:text-4xl font-bold text-slate-900 mb-3">
              Біздің студенттер не дейді?
            </h2>
          </div>

          <div className="grid md:grid-cols-3 gap-6">
            {[
              { name: "Айгерім Н.", score: "142 балл", uni: "ҚазҰУ", text: "Осы платформа арқылы дайындалып, грантқа түстім!" },
              { name: "Асқар Т.", score: "138 балл", uni: "МУНУ", text: "Нақты емтихан сияқты, өте пайдалы болды." },
              { name: "Дана М.", score: "145 балл", uni: "ЕҰУ", text: "Ең жақсы дайындық құралы. Ұсынамын!" },
            ].map((review, idx) => (
              <div key={idx} className="bg-gradient-to-br from-slate-50 to-blue-50/50 rounded-2xl p-6 border border-slate-100">
                <div className="flex items-center gap-1 mb-4">
                  {[...Array(5)].map((_, i) => (
                    <Star key={i} className="w-4 h-4 text-amber-400 fill-amber-400" />
                  ))}
                </div>
                <p className="text-slate-700 mb-4 italic">"{review.text}"</p>
                <div className="flex items-center justify-between">
                  <div>
                    <div className="font-semibold text-slate-900">{review.name}</div>
                    <div className="text-sm text-slate-500">{review.uni}</div>
                  </div>
                  <div className="px-3 py-1 bg-green-100 text-green-700 rounded-full text-sm font-bold">
                    {review.score}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Final CTA */}
      <section className="py-12 md:py-20 bg-gradient-to-r from-blue-600 via-indigo-600 to-violet-600 relative overflow-hidden">
        <div className="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiNmZmYiIGZpbGwtb3BhY2l0eT0iMC4wNSI+PGNpcmNsZSBjeD0iMzAiIGN5PSIzMCIgcj0iMiIvPjwvZz48L2c+PC9zdmc+')] opacity-50"></div>
        <div className="relative max-w-4xl mx-auto px-4 text-center">
          <h2 className="text-2xl md:text-4xl font-bold text-white mb-4">
            Магистратураға бірінші қадам!
          </h2>
          <p className="text-blue-100 mb-8 text-base md:text-lg max-w-2xl mx-auto">
            Қазір тесттен өтіп, өз деңгейіңізді тексеріңіз. Тегін және тіркеусіз.
          </p>
          <button
            onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
            className="inline-flex items-center gap-2 px-8 py-4 bg-white text-blue-600 font-bold rounded-xl shadow-xl hover:shadow-2xl hover:scale-105 transition-all duration-300"
          >
            <span>Бастау</span>
            <ArrowRight className="w-5 h-5" />
          </button>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-8 bg-slate-900 text-slate-400">
        <div className="max-w-7xl mx-auto px-4 text-center">
          <div className="flex items-center justify-center gap-2 mb-4">
            <GraduationCap className="w-6 h-6 text-blue-400" />
            <span className="font-bold text-white">MagistracyPrep</span>
          </div>
          <p className="text-sm">
            © 2025 Магистратураға Дайындық. Барлық құқықтар қорғалған.
          </p>
        </div>
      </footer>
    </div>
  );
};

export default WelcomeScreen;