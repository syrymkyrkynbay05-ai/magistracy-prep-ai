import React, { useState } from 'react';
import { 
  BookOpen, Brain, Clock, Database, Globe, ArrowRight, 
  Award, Zap, Target, GraduationCap, TrendingUp, Shield, 
  Menu, X, Sparkles, ChevronRight, Play, ExternalLink
} from 'lucide-react';
import { SUBJECTS } from '../constants';
import { SubjectId } from '../types';

interface WelcomeScreenProps {
  onStart: (name: string) => void;
  isLoading: boolean;
  onViewProgram: () => void;
}

const WelcomeScreen: React.FC<WelcomeScreenProps> = ({ onStart, isLoading, onViewProgram }) => {
  const [name, setName] = useState('');
  const [error, setError] = useState(false);
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const handleStart = () => {
    if (!name.trim()) {
      setError(true);
      return;
    }
    onStart(name.trim());
  };

  const steps = [
    { 
      title: "Анықтау", 
      desc: "Өз бағытыңды таңда",
      icon: Target,
      color: "text-blue-400"
    },
    { 
      title: "Тестілеу", 
      desc: "КТ форматындағы тест",
      icon: Zap,
      color: "text-amber-400"
    },
    { 
      title: "Талдау", 
      desc: "Қатемен жұмыс",
      icon: Brain,
      color: "text-purple-400"
    },
    { 
      title: "Нәтиже", 
      desc: "Грантқа ие бол",
      icon: Award,
      color: "text-green-400"
    },
  ];

  return (
    <div className="min-h-screen bg-[#0a0c10] text-[#f8fafc] selection:bg-blue-500/30">
      
      {/* Navigation */}
      <nav className="fixed top-0 w-full z-50 glass-dark border-b border-white/5">
        <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
          <div className="flex items-center gap-3 group cursor-pointer">
            <div className="w-10 h-10 gradient-brand rounded-xl flex items-center justify-center shadow-lg shadow-blue-500/20 group-hover:scale-110 transition-transform">
              <GraduationCap className="text-white w-6 h-6" />
            </div>
            <span className="text-xl font-black tracking-tighter uppercase">Magistracy<span className="text-blue-500">AI</span></span>
          </div>

          <div className="hidden md:flex items-center gap-8">
            <button onClick={onViewProgram} className="text-sm font-medium text-slate-400 hover:text-white transition-colors">Бағдарлама</button>
            <a href="#stats" className="text-sm font-medium text-slate-400 hover:text-white transition-colors">Статистика</a>
            <button 
              onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
              className="px-5 py-2.5 bg-white text-black text-sm font-bold rounded-full hover:bg-slate-200 transition-all active:scale-95"
            >
              Бастау
            </button>
          </div>

          <button className="md:hidden" onClick={() => setIsMenuOpen(!isMenuOpen)}>
            {isMenuOpen ? <X /> : <Menu />}
          </button>
        </div>
      </nav>

      {/* Menu Mobile */}
      {isMenuOpen && (
        <div className="fixed inset-0 z-40 bg-black/95 backdrop-blur-xl flex flex-col items-center justify-center gap-8 md:hidden">
          <button onClick={onViewProgram} className="text-2xl font-bold">Бағдарлама</button>
          <a href="#stats" onClick={() => setIsMenuOpen(false)} className="text-2xl font-bold">Статистика</a>
          <button onClick={() => { setIsMenuOpen(false); handleStart(); }} className="px-10 py-4 gradient-brand rounded-full font-black">Бастау</button>
        </div>
      )}

      {/* Hero Section */}
      <section className="relative pt-40 pb-24 overflow-hidden">
        {/* Abstract Background Decoration */}
        <div className="absolute top-1/4 right-0 w-[600px] h-[600px] bg-blue-600/10 rounded-full blur-[120px] pointer-events-none"></div>
        <div className="absolute bottom-1/4 left-0 w-[500px] h-[500px] bg-purple-600/10 rounded-full blur-[100px] pointer-events-none"></div>
        
        <div className="max-w-7xl mx-auto px-6 grid lg:grid-cols-2 gap-16 items-center">
          <div className="relative z-10 text-center lg:text-left">
            <div className="inline-flex items-center gap-2 px-3 py-1 bg-white/5 border border-white/10 rounded-full mb-8">
              <Sparkles className="w-4 h-4 text-blue-400" />
              <span className="text-xs font-bold uppercase tracking-widest text-blue-400">Next Gen Learning</span>
            </div>
            
            <h1 className="text-5xl md:text-7xl font-black mb-8 leading-[1.1] tracking-tight">
              Болашағыңды <br />
              <span className="gradient-text">Бүгін Анықта.</span>
            </h1>
            
            <p className="text-lg md:text-xl text-slate-400 mb-12 max-w-xl leading-relaxed">
              Магистратураға дайындықтың ең тиімді платформасы. 
              Жасанды интеллект көмегімен жасалған 5000+ сұрақ және терең аналитика.
            </p>

            <div className="relative max-w-md mx-auto lg:mx-0">
               <div className="p-1 glass-dark rounded-2xl flex flex-col md:flex-row gap-2 shadow-2xl">
                 <input 
                   type="text" 
                   value={name}
                   onChange={(e) => { setName(e.target.value); if(error) setError(false); }}
                   placeholder="Аты-жөніңізді жазыңыз"
                   className={`flex-1 px-6 py-4 bg-transparent outline-none text-white placeholder-slate-500 font-medium ${error ? 'border-red-400' : ''}`}
                 />
                 <button 
                   onClick={handleStart}
                   disabled={isLoading}
                   className="px-8 py-4 gradient-brand text-white font-black rounded-xl hover:scale-[1.02] transition-all active:scale-95 flex items-center justify-center gap-3 disabled:opacity-50"
                 >
                   {isLoading ? 'Жүктелуде...' : <>Бастау <ChevronRight className="w-5 h-5"/></>}
                 </button>
               </div>
               {error && <p className="text-red-400 text-xs font-bold mt-3 ml-2 flex items-center gap-1"><span role="img">ℹ️</span> Аты-жөніңізді жазуды ұмытпаңыз</p>}
            </div>

            <div className="mt-12 flex items-center justify-center lg:justify-start gap-8 opacity-50 grayscale hover:grayscale-0 transition-all duration-500">
               <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Google_Logo.svg/1024px-Google_Logo.svg.png" className="h-6 object-contain" alt="Google" />
               <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Microsoft_Logo.svg/1024px-Microsoft_Logo.svg.png" className="h-6 object-contain" alt="MS" />
               <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/LinkedIn_Logo.svg/1024px-LinkedIn_Logo.svg.png" className="h-6 object-contain" alt="LinkedIn" />
            </div>
          </div>

          <div className="relative hidden lg:block">
            <div className="relative z-10 animate-float">
               <img 
                 src="/images/assets/hero_shape.png" 
                 alt="Premium Design Element" 
                 className="w-full max-w-[500px] h-auto drop-shadow-[0_0_80px_rgba(59,130,246,0.2)]" 
               />
            </div>
            {/* Ambient elements */}
            <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[120%] h-[120%] glass rounded-full blur-[100px] -z-10 opacity-20"></div>
          </div>
        </div>
      </section>

      {/* Steps Section */}
      <section className="py-24 border-y border-white/5 bg-white/[0.01]">
        <div className="max-w-7xl mx-auto px-6">
          <div className="grid grid-cols-2 lg:grid-cols-4 gap-8">
            {steps.map((step, i) => (
              <div key={i} className="group relative">
                <div className="mb-6 flex items-center gap-4">
                  <div className={`w-14 h-14 glass rounded-2xl flex items-center justify-center ${step.color} shadow-inner`}>
                    <step.icon className="w-7 h-7" />
                  </div>
                  <div className="h-px flex-1 bg-white/10 hidden lg:block"></div>
                </div>
                <h3 className="text-xl font-bold mb-2 group-hover:text-blue-400 transition-colors uppercase tracking-wider">{step.title}</h3>
                <p className="text-slate-500 text-sm font-medium">{step.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Subjects Cards */}
      <section className="py-32">
        <div className="max-w-7xl mx-auto px-6">
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-8 mb-20">
             <div className="max-w-2xl">
                <h2 className="text-4xl md:text-6xl font-black mb-6 tracking-tight">Дайындық <br/> <span className="text-slate-500">бағыттары.</span></h2>
                <p className="text-slate-400 font-medium">Кешенді тестілеудің барлық пәндерін қамтитын жаттығу жинақтары.</p>
             </div>
             <button onClick={onViewProgram} className="group flex items-center gap-2 text-sm font-black uppercase tracking-widest text-blue-400 hover:text-blue-300 transition-all">
                Бағдарламаны көру <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
             </button>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {[
              { id: SubjectId.ENGLISH, label: "English", desc: "Грамматика және Мәтін", icon: Globe, color: "from-sky-500/20 to-blue-500/20" },
              { id: SubjectId.TGO, label: "TGO", desc: "Логикалық ойлау", icon: Brain, color: "from-purple-500/20 to-indigo-500/20" },
              { id: SubjectId.ALGO, label: "Algorithms", desc: "Algorithm & C++", icon: Zap, color: "from-orange-500/20 to-rose-500/20" },
              { id: SubjectId.DB, label: "Databases", desc: "SQL & ER Models", icon: Database, color: "from-emerald-500/20 to-teal-500/20" }
            ].map((s) => (
              <div key={s.id} className="group relative glass rounded-[32px] p-8 hover:bg-white/[0.05] transition-all cursor-pointer overflow-hidden border border-white/5">
                <div className={`absolute inset-0 bg-gradient-to-br ${s.color} opacity-0 group-hover:opacity-100 transition-opacity duration-700`}></div>
                <div className="relative z-10">
                  <div className="w-14 h-14 bg-white/5 rounded-2xl flex items-center justify-center mb-8 border border-white/10">
                    <s.icon className="w-7 h-7" />
                  </div>
                  <h3 className="text-2xl font-black mb-2">{s.label}</h3>
                  <p className="text-slate-500 text-sm mb-8">{s.desc}</p>
                  <div className="flex items-center justify-between">
                     <span className="text-xs font-bold text-slate-500 uppercase tracking-widest">{SUBJECTS[s.id].totalQuestions} сұрақ</span>
                     <div className="w-8 h-8 rounded-full bg-white text-black flex items-center justify-center opacity-0 group-hover:opacity-100 transition-all">
                        <ArrowRight className="w-4 h-4" />
                     </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Bottom */}
      <section className="py-24 bg-gradient-to-b from-transparent to-black">
        <div className="max-w-4xl mx-auto px-6 text-center">
           <div className="w-20 h-20 bg-blue-500/10 rounded-full flex items-center justify-center mx-auto mb-10 border border-blue-500/20">
              <Zap className="text-blue-500 w-10 h-10" />
           </div>
           <h2 className="text-4xl md:text-6xl font-black mb-8 tracking-tighter italic uppercase">Time to scale.</h2>
           <p className="text-slate-500 text-lg mb-12">Дайындықты дәл қазір бастаңыз.</p>
           <button 
             onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
             className="px-12 py-5 gradient-brand rounded-full font-black text-xl shadow-2xl shadow-blue-500/40 hover:scale-110 transition-all active:scale-95"
           >
             Тегін тест бастау
           </button>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-24 border-t border-white/5">
        <div className="max-w-7xl mx-auto px-6 grid md:grid-cols-2 lg:grid-cols-4 gap-12 text-sm text-slate-500">
           <div>
              <div className="flex items-center gap-2 mb-6 grayscale brightness-200">
                <GraduationCap className="w-6 h-6 text-blue-500" />
                <span className="font-black text-white uppercase">MagistracyAI</span>
              </div>
              <p className="leading-relaxed">Магистратураға дайындықтың кәсіби деңгейі.</p>
           </div>
           <div>
              <h4 className="font-bold text-white mb-6 uppercase tracking-widest text-xs">Пәндер</h4>
              <nav className="flex flex-col gap-4">
                 <button className="text-left hover:text-white transition-colors">English Language</button>
                 <button className="text-left hover:text-white transition-colors">TGO Logic</button>
                 <button className="text-left hover:text-white transition-colors">Informatics</button>
              </nav>
           </div>
           <div>
              <h4 className="font-bold text-white mb-6 uppercase tracking-widest text-xs">Сілтемелер</h4>
              <nav className="flex flex-col gap-4">
                 <button onClick={onViewProgram} className="text-left hover:text-white transition-colors flex items-center gap-2">Бағдарлама <ExternalLink className="w-3 h-3"/></button>
                 <a href="#" className="hover:text-white transition-colors">Ережелер</a>
              </nav>
           </div>
           <div>
              <h4 className="font-bold text-white mb-6 uppercase tracking-widest text-xs">Support</h4>
              <p>Email: ask@magistracy.ai</p>
              <div className="flex gap-4 mt-6">
                 <div className="w-8 h-8 glass rounded-lg"></div>
                 <div className="w-8 h-8 glass rounded-lg"></div>
              </div>
           </div>
        </div>
        <div className="max-w-7xl mx-auto px-6 mt-20 pt-10 border-t border-white/5 text-[10px] uppercase font-bold tracking-[0.2em] text-slate-700">
           © 2026 MAGISTRACY AI. BUILT FOR EXCELLENCE.
        </div>
      </footer>
    </div>
  );
};

export default WelcomeScreen;