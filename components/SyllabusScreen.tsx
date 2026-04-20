import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { ChevronLeft, Book, Globe, Brain, Database, Info, Loader2, Sparkles, BookOpen } from 'lucide-react';
import { getSyllabus } from '../services/apiService';

interface SyllabusScreenProps {
  onBack: () => void;
}

const SyllabusScreen: React.FC<SyllabusScreenProps> = ({ onBack }) => {
  const { subjectId } = useParams<{ subjectId: string }>();
  const navigate = useNavigate();
  const currentSubject = subjectId || 'english';

  const [content, setContent] = useState<string>('');
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const fetchSyllabus = async () => {
      setIsLoading(true);
      const data = await getSyllabus(currentSubject);
      setContent(data);
      setIsLoading(false);
    };
    fetchSyllabus();
  }, [currentSubject]);

  const subjects = [
    { id: 'english', name: 'Ағылшын тілі', icon: Globe, color: 'text-blue-500', bg: 'bg-blue-100', activeBg: 'bg-gradient-to-br from-blue-500 to-indigo-600', shadow: 'shadow-blue-500/30' },
    { id: 'tgo', name: 'ОДАТ (Логика)', icon: Brain, color: 'text-purple-500', bg: 'bg-purple-100', activeBg: 'bg-gradient-to-br from-purple-500 to-fuchsia-600', shadow: 'shadow-purple-500/30' },
    { id: 'algo', name: 'Алгоритмдер', icon: BookOpen, color: 'text-rose-500', bg: 'bg-rose-100', activeBg: 'bg-gradient-to-br from-rose-500 to-red-600', shadow: 'shadow-rose-500/30' },
    { id: 'db', name: 'Дерекқорлар', icon: Database, color: 'text-amber-500', bg: 'bg-amber-100', activeBg: 'bg-gradient-to-br from-amber-500 to-orange-600', shadow: 'shadow-amber-500/30' },
    { id: 'info', name: 'Жалпы ақпарат', icon: Info, color: 'text-emerald-500', bg: 'bg-emerald-100', activeBg: 'bg-gradient-to-br from-emerald-500 to-teal-600', shadow: 'shadow-emerald-500/30' },
  ];

  // Enhanced Markdown-to-HTML parser with premium typography styling
  const renderMarkdown = (text: string) => {
    const formatInline = (str: string) => {
      if (!str.includes('**') && !str.includes('*') && !str.includes('`')) return str;

      // A simple regex approach to inline styling
      let html = str;
      // Bold
      html = html.replace(/\*\*([^*]+)\*\*/g, '<strong class="font-extrabold text-slate-800">$1</strong>');
      // Italic (if used with single *)
      html = html.replace(/(?<!\w)\*([^*]+)\*(?!\w)/g, '<em class="italic text-slate-700">$1</em>');
      // Code
      html = html.replace(/`([^`]+)`/g, '<code class="bg-slate-100 text-pink-600 px-1.5 py-0.5 rounded font-mono text-[0.9em]">$1</code>');

      return <span dangerouslySetInnerHTML={{ __html: html }} />;
    };

    return text.split('\n').map((line, index) => {
      const trimmed = line.trim();

      if (trimmed.startsWith('# '))
        return (
          <h1 key={index} className="text-3xl md:text-4xl font-extrabold text-slate-900 mt-6 mb-6 pb-4 border-b border-slate-200 tracking-tight">
            {formatInline(trimmed.replace('# ', ''))}
          </h1>
        );
      if (trimmed.startsWith('## '))
        return <h2 key={index} className="text-2xl font-bold text-slate-800 mt-10 mb-4 tracking-tight">{formatInline(trimmed.replace('## ', ''))}</h2>;
      if (trimmed.startsWith('### '))
        return <h3 key={index} className="text-xl font-bold text-slate-800 mt-8 mb-3">{formatInline(trimmed.replace('### ', ''))}</h3>;
      if (trimmed.startsWith('* ') || trimmed.startsWith('- '))
        return (
          <li key={index} className="ml-5 pl-1 text-slate-600 mb-2.5 leading-relaxed list-disc">
            {formatInline(trimmed.replace(/^[* -] /, ''))}
          </li>
        );
      if (/^\d+\.\s/.test(trimmed))
        return (
          <li key={index} className="ml-2 pl-2 text-slate-700 font-medium mb-3 mt-2 leading-relaxed flex items-start">
            <span className="text-indigo-600 font-black mr-2 select-none">{trimmed.match(/^\d+/)?.[0]}.</span>
            <span className="flex-1">{formatInline(trimmed.replace(/^\d+\.\s/, ''))}</span>
          </li>
        );
      if (trimmed === '---')
        return <div key={index} className="w-full h-px bg-gradient-to-r from-transparent via-slate-200 to-transparent my-8" />;
      if (trimmed.startsWith('> '))
        return (
          <blockquote key={index} className="relative border-l-4 border-indigo-500 bg-gradient-to-r from-indigo-50/80 to-white p-5 my-6 rounded-r-2xl text-slate-700 italic shadow-sm hover:shadow-md transition-shadow">
            <div className="absolute top-2 right-4 text-4xl text-indigo-100 font-serif select-none">"</div>
            {formatInline(trimmed.replace(/^>\s*/, ''))}
          </blockquote>
        );
      if (trimmed.startsWith('|')) {
        // Very basic table row render
        const cells = trimmed.split('|').filter(c => c.trim() !== '');
        const isHeader = trimmed.includes('---');
        if (isHeader) return null; // Skip table separator lines
        return (
          <div key={index} className="flex border-b border-slate-100 py-3 hover:bg-slate-50 transition-colors px-2">
            {cells.map((c, i) => (
              <div key={i} className={`flex-1 ${i === 0 ? 'font-semibold text-slate-800' : 'text-slate-600'}`}>{formatInline(c.trim())}</div>
            ))}
          </div>
        );
      }
      if (trimmed === '')
        return <div key={index} className="h-4"></div>;

      return <p key={index} className="text-slate-600 text-lg leading-relaxed mb-4">{formatInline(trimmed)}</p>;
    });
  };

  return (
    <div className="min-h-screen bg-[#F1F5F9] font-sans flex flex-col relative overflow-hidden">
      {/* Decorative Background Elements */}
      <div className="absolute top-0 left-0 w-full h-[300px] bg-gradient-to-b from-indigo-100/50 to-transparent pointer-events-none" />
      <div className="absolute -top-40 -right-40 w-96 h-96 bg-blue-200/40 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute top-40 -left-20 w-72 h-72 bg-purple-200/40 rounded-full blur-3xl pointer-events-none" />

      {/* Header */}
      <header className="bg-white/70 backdrop-blur-xl border-b border-white/50 sticky top-0 z-20 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 md:px-6 h-16 flex items-center justify-between">
          <button
            onClick={onBack}
            className="group flex items-center px-3 py-1.5 rounded-full bg-slate-100 hover:bg-white hover:shadow-md text-slate-600 hover:text-indigo-600 transition-all font-medium border border-transparent hover:border-slate-200"
          >
            <ChevronLeft className="w-5 h-5 mr-1 group-hover:-translate-x-1 transition-transform" />
            Артқа
          </button>
          <div className="flex items-center gap-2">
            <Book className="w-6 h-6 text-indigo-600" />
            <h1 className="text-xl font-black bg-clip-text text-transparent bg-gradient-to-r from-slate-900 to-indigo-900 tracking-tight">
              Оқу Бағдарламасы
            </h1>
          </div>
          <div className="w-24"></div> {/* Spacer to center title */}
        </div>
      </header>

      <div className="max-w-7xl mx-auto flex-1 w-full flex flex-col lg:flex-row gap-6 p-4 md:p-8 lg:px-6 relative z-10">

        {/* Sidebar Tabs */}
        <aside className="w-full lg:w-72 shrink-0 space-y-3">
          {subjects.map((sub) => {
            const isActive = currentSubject === sub.id;
            return (
              <button
                key={sub.id}
                onClick={() => navigate(`/program/${sub.id}`)}
                className={`
                  w-full flex items-center p-3 rounded-2xl transition-all duration-300 transform outline-none
                  ${isActive
                    ? `${sub.activeBg} text-white shadow-xl ${sub.shadow} scale-[1.02]`
                    : 'bg-white/80 backdrop-blur-md text-slate-700 hover:bg-white hover:shadow-lg border border-white hover:scale-[1.01]'}
                `}
              >
                <div className={`p-2.5 rounded-xl mr-4 transition-colors duration-300 ${isActive ? 'bg-white/20 shadow-inner' : sub.bg + ' ' + sub.color}`}>
                  <sub.icon className="w-6 h-6" />
                </div>
                <span className={`text-[15px] ${isActive ? 'font-black tracking-wide' : 'font-bold'}`}>{sub.name}</span>

                {/* Active Indicator Chevron */}
                {isActive && (
                  <div className="ml-auto bg-white/20 rounded-full p-1">
                    <ChevronLeft className="w-4 h-4 rotate-180" />
                  </div>
                )}
              </button>
            );
          })}

          <div className="mt-6 p-6 bg-gradient-to-br from-indigo-900 via-slate-900 to-[#07090D] rounded-3xl text-white shadow-2xl relative overflow-hidden group border border-white/10">
            <div className="absolute -top-10 -right-10 w-40 h-40 bg-blue-500/20 rounded-full blur-3xl group-hover:scale-150 transition-transform duration-700 ease-in-out" />
            <div className="absolute -bottom-10 -left-10 w-32 h-32 bg-purple-500/20 rounded-full blur-3xl" />

            <h4 className="font-black text-base mb-3 flex items-center uppercase tracking-widest text-transparent bg-clip-text bg-gradient-to-r from-blue-300 to-indigo-300 relative z-10">
              Сынаққа <br /> дайындық
            </h4>

            <p className="text-slate-300 text-[13px] font-medium mb-6 leading-relaxed relative z-10 text-justify">
              Теориялық материалды толық меңгерген болсаңыз, нақты емтихан форматында күшіңізді сынап, алған біліміңізді бекітуге шақырамыз. Жетістікке жету жолында сәттілік тілейміз!
            </p>

            <button
              onClick={onBack}
              className="w-full py-3.5 bg-blue-600 hover:bg-blue-500 text-white font-bold rounded-xl transition-all active:scale-95 shadow-[0_0_20px_rgba(37,99,235,0.4)] relative z-10 flex items-center justify-center gap-2 uppercase text-xs tracking-widest"
            >
              <Brain className="w-4 h-4" /> Тестілеуге өту
            </button>
          </div>
        </aside>

        {/* Content Area */}
        <main className="flex-1 bg-white/90 backdrop-blur-xl rounded-[2rem] shadow-xl border border-white overflow-hidden flex flex-col min-h-[600px] relative">

          {isLoading ? (
            <div className="flex-1 flex flex-col items-center justify-center text-slate-400">
              <Loader2 className="w-12 h-12 animate-spin mb-4 text-indigo-500" />
              <p className="font-medium text-lg animate-pulse text-indigo-900/50">Мәліметтер жүктелуде...</p>
            </div>
          ) : (
            <div className="flex-1 overflow-y-auto p-6 md:p-12 scrollbar-hide">
              <div className="max-w-4xl mx-auto animate-fade-in-up">
                {renderMarkdown(content)}
              </div>
            </div>
          )}
        </main>
      </div>
    </div>
  );
};

export default SyllabusScreen;
