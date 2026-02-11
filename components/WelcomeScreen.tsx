import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  BookOpen, Brain, Clock, Database, Globe, ArrowRight, 
  Award, Zap, Target, GraduationCap, TrendingUp, Shield, 
  Menu, X, Sparkles, ChevronRight, Play, ExternalLink,
  MessageSquare, Star, Users, CheckCircle, LogOut, History
} from 'lucide-react';
import { SUBJECTS } from '../constants';
import { SubjectId } from '../types';

interface WelcomeScreenProps {
  onStart: (name: string) => void;
  isLoading: boolean;
  onViewProgram: () => void;
  onViewHistory: () => void;
  userName?: string;
  onLogout?: () => void;
}

const WelcomeScreen: React.FC<WelcomeScreenProps> = ({ onStart, isLoading, onViewProgram, onViewHistory, userName, onLogout }) => {
  const [name, setName] = useState(userName || '');
  const [error, setError] = useState(false);
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 20);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleStart = () => {
    if (!name.trim()) {
      setError(true);
      return;
    }
    onStart(name.trim());
  };

  const fadeInUp = {
    initial: { opacity: 0, y: 20 },
    animate: { opacity: 1, y: 0 },
    transition: { duration: 0.6, ease: [0.22, 1, 0.36, 1] }
  };

  const staggerContainer = {
    animate: { transition: { staggerChildren: 0.1 } }
  };

  return (
    <div className="min-h-screen bg-[#07090d] text-[#f8fafc] selection:bg-blue-500/30 overflow-x-hidden w-full max-w-[100vw] relative">
      
      {/* Background blobs */}
      <div className="absolute overflow-hidden inset-0 pointer-events-none">
        <div className="blob w-[500px] h-[500px] bg-blue-600/10 top-[-100px] -right-[100px]" />
        <div className="blob w-[400px] h-[400px] bg-purple-600/10 bottom-[20%] -left-[100px]" />
        <div className="blob w-[300px] h-[300px] bg-emerald-500/5 top-[40%] right-[10%]" />
      </div>

      {/* Navigation */}
      <nav className={`fixed top-0 w-full z-50 transition-all duration-500 ${scrolled ? 'py-4 glass-dark border-b border-white/5 shadow-2xl backdrop-blur-2xl' : 'py-8'}`}>
        <div className="max-w-7xl mx-auto px-6 flex items-center justify-between">
          <motion.div 
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            className="flex items-center gap-3 group cursor-pointer"
          >
            <div className="w-10 h-10 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform duration-500">
              <img src="/logo no bg, blue.svg" alt="MagisCore Logo" className="w-full h-full object-contain" />
            </div>
            <span className="text-xl font-extrabold tracking-tight uppercase whitespace-nowrap">Magis<span className="text-blue-500">Core</span></span>
          </motion.div>

          <div className="hidden md:flex items-center gap-10">
            <button onClick={onViewProgram} className="text-sm font-bold text-slate-400 hover:text-white transition-colors tracking-widest uppercase">Бағдарлама</button>
            <button onClick={onViewHistory} className="text-sm font-bold text-slate-400 hover:text-white transition-colors tracking-widest uppercase">Тарих</button>
            <a href="#subjects" className="text-sm font-bold text-slate-400 hover:text-white transition-colors tracking-widest uppercase">Пәндер</a>
            {userName && (
              <div className="flex items-center gap-4 border-l border-white/5 pl-10">
                <span className="text-sm font-bold text-slate-300">{userName}</span>
                <button
                  onClick={onLogout}
                  className="p-3 glass border-white/10 text-red-500 rounded-xl hover:bg-red-500/10 transition-all active:scale-95"
                  title="Шығу"
                >
                  <LogOut className="w-4 h-4" />
                </button>
              </div>
            )}
          </div>

          <button className="md:hidden glass p-2 rounded-lg" onClick={() => setIsMenuOpen(!isMenuOpen)}>
            {isMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>

        {/* Mobile Menu */}
        <AnimatePresence>
          {isMenuOpen && (
            <motion.div
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: 'auto' }}
              exit={{ opacity: 0, height: 0 }}
              className="md:hidden glass-dark border-t border-white/5 overflow-hidden"
            >
              <div className="flex flex-col p-6 gap-6">
                <button 
                  onClick={() => { onViewProgram(); setIsMenuOpen(false); }} 
                  className="text-left text-sm font-bold text-slate-400 hover:text-white transition-colors tracking-[0.2em] uppercase flex items-center gap-3"
                >
                  <BookOpen className="w-4 h-4" /> Бағдарлама
                </button>
                <button 
                  onClick={() => { onViewHistory(); setIsMenuOpen(false); }} 
                  className="text-left text-sm font-bold text-slate-400 hover:text-white transition-colors tracking-[0.2em] uppercase flex items-center gap-3"
                >
                  <History className="w-4 h-4" /> Тарих
                </button>
                <a 
                  href="#subjects" 
                  onClick={() => setIsMenuOpen(false)}
                  className="text-sm font-bold text-slate-400 hover:text-white transition-colors tracking-[0.2em] uppercase flex items-center gap-3"
                >
                  <Brain className="w-4 h-4" /> Пәндер
                </a>
                
                {userName && (
                  <div className="pt-6 border-t border-white/5 flex flex-col gap-6">
                    <div className="flex items-center justify-between">
                      <span className="text-sm font-bold text-slate-300">{userName}</span>
                      <button
                        onClick={onLogout}
                        className="flex items-center gap-2 text-red-500 text-sm font-bold uppercase tracking-widest"
                      >
                        <LogOut className="w-4 h-4" /> Шығу
                      </button>
                    </div>
                  </div>
                )}
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </nav>

      {/* Hero Section */}
      <section className="relative pt-44 pb-32">
        <div className="max-w-7xl mx-auto px-6">
          <div className="flex flex-col items-center text-center max-w-4xl mx-auto">
            <motion.div 
              {...fadeInUp}
              className="inline-flex items-center gap-2 px-4 py-1.5 bg-blue-500/10 border border-blue-500/20 rounded-full mb-10"
            >
              <Sparkles className="w-4 h-4 text-blue-400" />
              <span className="text-[10px] font-black uppercase tracking-[0.2em] text-blue-400">2026 ЖЫЛҒЫ РЕСМИ БАҒДАРЛАМА</span>
            </motion.div>
            
            <motion.h1 
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.8, ease: [0.22, 1, 0.36, 1] }}
              className="text-6xl md:text-8xl font-black mb-10 leading-[0.95] tracking-tighter italic uppercase"
            >
              Болашағыңды <br />
              <span className="gradient-text drop-shadow-[0_0_30px_rgba(255,255,255,0.1)]">Бүгін Анықта.</span>
            </motion.h1>
            
            <motion.p 
              {...fadeInUp}
              transition={{ delay: 0.1 }}
              className="text-lg md:text-xl text-slate-400 mb-14 max-w-2xl leading-relaxed"
            >
              Магистратураға дайындықтың кәсіби деңгейі. 
              800-ден астам кәсіби сұрақтар жинағы, 
              Listening аудиолары және терең аналитика.
            </motion.p>

            <motion.div 
              {...fadeInUp}
              transition={{ delay: 0.2 }}
              className="relative w-full max-w-md group"
            >
               <div className="absolute -inset-1 bg-gradient-to-r from-blue-600 to-indigo-600 rounded-2xl blur opacity-25 group-hover:opacity-40 transition duration-1000 group-hover:duration-200"></div>
               <div className="relative p-1 glass-dark rounded-2xl flex flex-col md:flex-row gap-2 shadow-2xl border-white/5">
                 <input 
                   type="text" 
                   value={name}
                   onChange={(e) => { setName(e.target.value); if(error) setError(false); }}
                   placeholder="Аты-жөніңізді жазыңыз"
                   className={`flex-1 px-6 py-4 bg-transparent outline-none text-white placeholder-slate-600 font-bold tracking-wide ${error ? 'bg-red-500/5' : ''}`}
                 />
                 <button 
                   onClick={handleStart}
                   disabled={isLoading}
                   className="px-10 py-4 gradient-brand text-white font-black rounded-xl hover:shadow-[0_0_30px_rgba(59,130,246,0.3)] transition-all active:scale-95 flex items-center justify-center gap-3 disabled:opacity-50"
                 >
                   {isLoading ? 'Жүктелуде...' : <>Тестіні Бастау <ChevronRight className="w-5 h-5"/></>}
                 </button>
               </div>
               <AnimatePresence>
                 {error && (
                   <motion.p 
                     initial={{ opacity: 0, y: -10 }}
                     animate={{ opacity: 1, y: 0 }}
                     exit={{ opacity: 0 }}
                     className="text-red-400 text-xs font-black mt-4 uppercase tracking-widest flex items-center justify-center gap-2"
                   >
                     <Shield className="w-3 h-3" /> Аты-жөніңізді жазуды ұмытпаңыз
                   </motion.p>
                 )}
               </AnimatePresence>
            </motion.div>

            <motion.div 
              {...fadeInUp}
              transition={{ delay: 0.3 }}
              className="mt-20 flex flex-wrap items-center justify-center gap-x-12 gap-y-6 opacity-30 grayscale contrast-[0.2] brightness-200"
            >
               <span className="text-sm font-black tracking-[0.3em] uppercase">СЕНІМДІ ДАЙЫНДЫҚ</span>
               <div className="h-4 w-px bg-white/20 hidden md:block"></div>
               <span className="text-sm font-black tracking-[0.3em] uppercase">МЫҢДАҒАН СТУДЕНТТЕР</span>
               <div className="h-4 w-px bg-white/20 hidden md:block"></div>
               <span className="text-sm font-black tracking-[0.3em] uppercase">РЕСМИ СПЕЦИФИКАЦИЯ</span>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Bento Grid Features */}
      <section className="py-24" id="subjects">
        <div className="max-w-7xl mx-auto px-6">
          <div className="grid grid-cols-1 md:grid-cols-12 gap-6 h-auto md:h-[600px]">
            {/* Master Card - English */}
            <motion.div 
              whileHover={{ scale: 1.01 }}
              className="md:col-span-8 bento-item group flex flex-col justify-between"
            >
              <div className="glow-overlay" />
              <div className="relative z-10">
                <div className="flex justify-between items-start mb-12">
                  <div className="w-16 h-16 bg-blue-500/10 rounded-2xl flex items-center justify-center border border-blue-500/20">
                    <Globe className="w-8 h-8 text-blue-400" />
                  </div>
                  <span className="px-4 py-1.5 bg-blue-500/20 text-blue-300 text-[10px] font-black uppercase tracking-widest rounded-full">Аудио Мәтіндер</span>
                </div>
                <h3 className="text-4xl md:text-5xl font-black mb-4 uppercase italic">Ағылшын Тілі</h3>
                <p className="text-slate-400 text-lg max-w-md font-medium">80+ аудио мәтіндер және кешенді грамматикалық сұрақтар жинағы.</p>
              </div>
              <div className="relative z-10 mt-12 flex items-center justify-between">
                <span className="text-[10px] font-black text-slate-500 uppercase tracking-[0.3em]">{SUBJECTS[SubjectId.ENGLISH].totalQuestions} сұрақ</span>
                <button className="w-12 h-12 rounded-full border border-white/10 flex items-center justify-center group-hover:bg-white group-hover:text-black transition-all">
                  <ArrowRight className="w-5 h-5" />
                </button>
              </div>
            </motion.div>

            {/* Small Card - TGO */}
            <motion.div 
              whileHover={{ scale: 1.01 }}
              className="md:col-span-4 bento-item group flex flex-col justify-between bg-purple-600/5 border-purple-500/20"
            >
              <div className="glow-overlay" style={{ background: 'radial-gradient(circle at 50% 50%, rgba(168, 85, 247, 0.15) 0%, transparent 80%)' }} />
              <div className="relative z-10">
                <div className="w-12 h-12 bg-purple-500/10 rounded-xl flex items-center justify-center mb-10 border border-purple-500/20">
                  <Brain className="w-6 h-6 text-purple-400" />
                </div>
                <h3 className="text-2xl font-black mb-3 uppercase">Оқу Сауаттылығы</h3>
                <p className="text-slate-500 text-sm font-medium">Сыни ойлау және мәтінмен жұмыс.</p>
              </div>
              <div className="relative z-10 flex items-center justify-between mt-8">
                <span className="text-[10px] font-black text-slate-500 uppercase tracking-[0.3em]">{SUBJECTS[SubjectId.TGO].totalQuestions} сұрақ</span>
                <ArrowRight className="w-4 h-4 text-slate-500 group-hover:text-purple-400 group-hover:translate-x-1 transition-all" />
              </div>
            </motion.div>

            {/* Small Card - Logic/Algo */}
            <motion.div 
              whileHover={{ scale: 1.01 }}
              className="md:col-span-4 bento-item group flex flex-col justify-between bg-emerald-500/5 border-emerald-500/20"
            >
              <div className="glow-overlay" style={{ background: 'radial-gradient(circle at 50% 50%, rgba(16, 185, 129, 0.1) 0%, transparent 80%)' }} />
              <div className="relative z-10">
                <div className="w-12 h-12 bg-emerald-500/10 rounded-xl flex items-center justify-center mb-10 border border-emerald-500/20">
                  <Zap className="w-6 h-6 text-emerald-400" />
                </div>
                <h3 className="text-2xl font-black mb-3 uppercase">Информатика</h3>
                <p className="text-slate-500 text-sm font-medium">C++, Data Structures & Logic.</p>
              </div>
              <div className="relative z-10 flex items-center justify-between mt-8">
                <span className="text-[10px] font-black text-slate-500 uppercase tracking-[0.3em]">{SUBJECTS[SubjectId.ALGO].totalQuestions} сұрақ</span>
                <ArrowRight className="w-4 h-4 text-slate-500 group-hover:text-emerald-400 group-hover:translate-x-1 transition-all" />
              </div>
            </motion.div>

            {/* Stats Card */}
            <motion.div 
              whileHover={{ scale: 1.01 }}
              className="md:col-span-4 bento-item flex flex-col items-center justify-center text-center border-white/10"
            >
              <div className="text-6xl font-black mb-2 gradient-text">80%</div>
              <div className="text-[10px] font-black text-slate-500 uppercase tracking-[0.3em]">Жоғары Көрсеткіш</div>
              <p className="text-xs text-slate-500 mt-6 max-w-[200px]">Бізбен дайындалған студенттердің грантқа түсу көрсеткіші.</p>
            </motion.div>

            {/* Small Card - DB */}
            <motion.div 
              whileHover={{ scale: 1.01 }}
              className="md:col-span-4 bento-item group flex flex-col justify-between bg-blue-500/5 border-blue-500/20"
            >
              <div className="glow-overlay" />
              <div className="relative z-10">
                <div className="w-12 h-12 bg-blue-400/10 rounded-xl flex items-center justify-center mb-10 border border-blue-400/20">
                  <Database className="w-6 h-6 text-blue-400" />
                </div>
                <h3 className="text-2xl font-black mb-3 uppercase">Деректер Қоры</h3>
                <p className="text-slate-500 text-sm font-medium">SQL, ER-models and Logic.</p>
              </div>
              <div className="relative z-10 flex items-center justify-between mt-8">
                <span className="text-[10px] font-black text-slate-500 uppercase tracking-[0.3em]">{SUBJECTS[SubjectId.DB].totalQuestions} сұрақ</span>
                <ArrowRight className="w-4 h-4 text-slate-500 group-hover:text-blue-400 group-hover:translate-x-1 transition-all" />
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Why Us Section */}
      <section className="py-32 relative overflow-hidden">
        <div className="max-w-7xl mx-auto px-6">
          <div className="text-center mb-24">
            <h2 className="text-4xl md:text-6xl font-black mb-6 uppercase italic tracking-tighter italic">Неге бізді таңдайды?</h2>
            <div className="h-1 w-20 gradient-brand mx-auto rounded-full" />
          </div>

          <div className="grid md:grid-cols-3 gap-12">
            {[
              { icon: Zap, title: "Жедел Аналитика", desc: "Тест соңында әр пән бойынша терең талдау және пайыздық көрсеткішті алыңыз." },
              { icon: Shield, title: "Ресми Формат", desc: "2026 жылғы жаңа спецификацияға толық сәйкес келетін сұрақтар жинағы." },
              { icon: MessageSquare, title: "Түсіндірмелер", desc: "Қиын сұрақтар бойынша арнайы түсіндірмелер мен кеңестер." },
            ].map((feature, i) => (
              <motion.div 
                key={i}
                whileHover={{ y: -10 }}
                className="p-10 glass rounded-[40px] border-white/5 relative group overflow-hidden"
              >
                <div className="absolute inset-0 bg-blue-500/5 opacity-0 group-hover:opacity-100 transition-opacity" />
                <div className="w-16 h-16 bg-white/5 rounded-2xl flex items-center justify-center mb-8 border border-white/10">
                  <feature.icon className="w-8 h-8 text-blue-400" />
                </div>
                <h3 className="text-2xl font-black mb-4 uppercase tracking-tight">{feature.title}</h3>
                <p className="text-slate-400 leading-relaxed font-medium">{feature.desc}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Social Proof */}
      <section className="py-24 border-y border-white/5">
        <div className="max-w-7xl mx-auto px-6 flex flex-col md:flex-row items-center justify-around gap-12 text-center">
            <div>
              <div className="text-5xl font-black mb-2 tracking-tighter">800+</div>
              <div className="text-[10px] font-black text-slate-500 uppercase tracking-[0.3em]">Шешілген Сұрақтар</div>
            </div>
            <div className="h-12 w-px bg-white/5 hidden md:block"></div>
            <div>
              <div className="text-5xl font-black mb-2 tracking-tighter">80+</div>
              <div className="text-[10px] font-black text-slate-500 uppercase tracking-[0.3em]">Аудио Сабақтар</div>
            </div>
            <div className="h-12 w-px bg-white/5 hidden md:block"></div>
            <div>
              <div className="text-5xl font-black mb-2 tracking-tighter">4.9/5</div>
              <div className="text-[10px] font-black text-slate-500 uppercase tracking-[0.3em]">Пайдаланушы Рейтингі</div>
            </div>
        </div>
      </section>

      {/* CTA Bottom */}
      <section className="py-40 relative">
        <div className="max-w-4xl mx-auto px-6 text-center relative z-10">
           <motion.div 
             initial={{ scale: 0.8, opacity: 0 }}
             whileInView={{ scale: 1, opacity: 1 }}
             className="w-24 h-24 bg-blue-500/10 rounded-full flex items-center justify-center mx-auto mb-12 border border-blue-500/20"
           >
              <Award className="text-blue-400 w-10 h-10" />
           </motion.div>
           <h2 className="text-5xl md:text-8xl font-black mb-10 tracking-tighter italic uppercase leading-[0.9]">Грантқа бір <br/> қадам қалды.</h2>
           <p className="text-slate-500 text-xl mb-16 font-medium">Өз мүмкіндігіңді бүгін сынап көр.</p>
           <button 
             onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
             className="px-16 py-6 gradient-brand rounded-full font-black text-2xl shadow-[0_20px_50px_rgba(59,130,246,0.3)] hover:scale-105 transition-all active:scale-95 uppercase tracking-tighter"
           >
             Тегін бастау
           </button>
        </div>
        <div className="absolute bottom-0 left-0 w-full h-[500px] bg-gradient-to-t from-blue-600/10 to-transparent pointer-events-none" />
      </section>

      {/* Footer */}
      <footer className="py-32 border-t border-white/5 relative z-10">
        <div className="max-w-7xl mx-auto px-6">
           <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-20 mb-32">
              <div className="lg:col-span-1">
                 <div className="flex items-center gap-3 mb-8">
                   <div className="w-10 h-10 gradient-brand rounded-xl flex items-center justify-center">
                     <GraduationCap className="text-white w-6 h-6" />
                   </div>
                   <span className="text-xl font-black tracking-tighter uppercase whitespace-nowrap">Magis<span className="text-blue-500">Core</span></span>
                 </div>
                 <p className="text-slate-500 leading-relaxed font-medium">Біз сізге армандаған оқу орныңызға түсуге көмектесеміз. Ең озық технологиялар мен тиімді дайындық методикасы.</p>
              </div>

              <div>
                 <h4 className="font-black text-white mb-10 uppercase tracking-[0.2em] text-[10px]">Платформа</h4>
                 <nav className="flex flex-col gap-6 font-bold text-slate-500 text-sm">
                    <button className="text-left hover:text-white transition-colors">Ағылшын тілі</button>
                    <button className="text-left hover:text-white transition-colors">Оқу сауаттылығы</button>
                    <button className="text-left hover:text-white transition-colors">Информатика</button>
                 </nav>
              </div>

              <div>
                 <h4 className="font-black text-white mb-10 uppercase tracking-[0.2em] text-[10px]">Ресурстар</h4>
                 <nav className="flex flex-col gap-6 font-bold text-slate-500 text-sm">
                    <button onClick={onViewProgram} className="text-left hover:text-white transition-colors flex items-center gap-2">Спецификация <ExternalLink className="w-3 h-3"/></button>
                    <button className="text-left hover:text-white transition-colors">Статистика</button>
                    <button className="text-left hover:text-white transition-colors">Сұрақ-жауап</button>
                 </nav>
              </div>

              <div>
                 <h4 className="font-black text-white mb-10 uppercase tracking-[0.2em] text-[10px]">Байланыс</h4>
                 <p className="font-black text-white text-lg mb-8 tracking-tight">help@magiscore.kz</p>
                 <div className="flex gap-4">
                    {[1,2,3].map(i => (
                      <div key={i} className="w-10 h-10 glass rounded-xl flex items-center justify-center border-white/5 hover:border-white/20 transition-colors cursor-pointer">
                        <Star className="w-4 h-4 text-slate-500" />
                      </div>
                    ))}
                 </div>
              </div>
           </div>

           <div className="flex flex-col md:flex-row items-center justify-between pt-12 border-t border-white/5 gap-8">
              <div className="text-[10px] uppercase font-black tracking-[0.3em] text-slate-700">
                                   © 2026 MAGISCORE. PROUDLY DEVELOPED IN KZ.

              </div>
              <div className="flex gap-10">
                 <a href="#" className="text-[10px] font-black text-slate-700 hover:text-white transition-colors uppercase tracking-widest">Privacy Policy</a>
                 <a href="#" className="text-[10px] font-black text-slate-700 hover:text-white transition-colors uppercase tracking-widest">Terms of Use</a>
              </div>
           </div>
        </div>
      </footer>
    </div>
  );
};

export default WelcomeScreen;