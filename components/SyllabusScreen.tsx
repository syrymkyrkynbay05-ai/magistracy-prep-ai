import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { ChevronLeft, Book, Globe, Brain, Database, Info, Loader2 } from 'lucide-react';
import { SubjectId } from '../types';
import { SUBJECTS } from '../constants';
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
    { id: 'english', name: 'Ағылшын тілі', icon: Globe, color: 'text-indigo-600', bg: 'bg-indigo-50' },
    { id: 'tgo', name: 'ОДАТ (Логика)', icon: Brain, color: 'text-violet-600', bg: 'bg-violet-50' },
    { id: 'algo', name: 'Алгоритмдер', icon: Book, color: 'text-rose-600', bg: 'bg-rose-50' },
    { id: 'db', name: 'Дерекқорлар', icon: Database, color: 'text-amber-600', bg: 'bg-amber-50' },
    { id: 'info', name: 'Жалпы ақпарат', icon: Info, color: 'text-slate-600', bg: 'bg-slate-50' },
  ];

  // Simple Markdown-to-HTML parser (basic headers and lists)
  const renderMarkdown = (text: string) => {
    return text.split('\n').map((line, index) => {
      if (line.startsWith('# ')) return <h1 key={index} className="text-3xl font-bold text-slate-900 mt-8 mb-4">{line.replace('# ', '')}</h1>;
      if (line.startsWith('## ')) return <h2 key={index} className="text-2xl font-bold text-slate-800 mt-6 mb-3 border-b pb-2">{line.replace('## ', '')}</h2>;
      if (line.startsWith('### ')) return <h3 key={index} className="text-xl font-bold text-slate-800 mt-5 mb-2">{line.replace('### ', '')}</h3>;
      if (line.startsWith('* ') || line.startsWith('- ')) return <li key={index} className="ml-6 text-slate-600 list-disc mb-1">{line.replace(/^[* -] /, '')}</li>;
      if (line.trim() === '---') return <hr key={index} className="my-6 border-slate-200" />;
      if (line.startsWith('> ')) return <blockquote key={index} className="border-l-4 border-blue-200 bg-blue-50/50 p-4 my-4 text-slate-700 italic">{line.replace('> ', '')}</blockquote>;
      if (line.trim() === '') return <div key={index} className="h-2"></div>;
      
      // Inline formatting (very basic)
      let formattedLine: any = line;
      if (line.includes('**')) {
        const parts = line.split('**');
        formattedLine = parts.map((part, i) => i % 2 === 1 ? <strong key={i}>{part}</strong> : part);
      }

      return <p key={index} className="text-slate-600 leading-relaxed mb-2">{formattedLine}</p>;
    });
  };

  return (
    <div className="min-h-screen bg-[#F8F9FB] flex flex-col">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-md border-b border-slate-200 sticky top-0 z-10">
        <div className="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
          <button 
            onClick={onBack}
            className="flex items-center text-slate-600 hover:text-blue-600 transition-colors font-medium"
          >
            <ChevronLeft className="w-5 h-5 mr-1" />
            Артқа
          </button>
          <h1 className="text-lg font-bold text-slate-900">Оқу Бағдарламасы</h1>
          <div className="w-20"></div> {/* Spacer */}
        </div>
      </header>

      <div className="max-w-6xl mx-auto flex-1 w-full flex flex-col md:flex-row gap-6 p-4 md:p-6">
        {/* Sidebar Tabs */}
        <aside className="w-full md:w-64 space-y-2">
          {subjects.map((sub) => (
            <button
              key={sub.id}
              onClick={() => navigate(`/program/${sub.id}`)}
              className={`
                w-full flex items-center p-3 rounded-xl transition-all duration-200
                ${currentSubject === sub.id 
                  ? 'bg-blue-600 text-white shadow-lg shadow-blue-200' 
                  : 'bg-white text-slate-600 hover:bg-white hover:shadow-md border border-slate-100'}
              `}
            >
              <div className={`p-2 rounded-lg mr-3 ${currentSubject === sub.id ? 'bg-white/20' : sub.bg + ' ' + sub.color}`}>
                <sub.icon className="w-5 h-5" />
              </div>
              <span className="font-semibold">{sub.name}</span>
            </button>
          ))}
        </aside>

        {/* Content Area */}
        <main className="flex-1 bg-white rounded-3xl shadow-sm border border-slate-100 overflow-hidden flex flex-col min-h-[500px]">
          {isLoading ? (
            <div className="flex-1 flex flex-col items-center justify-center text-slate-400">
              <Loader2 className="w-10 h-10 animate-spin mb-4" />
              <p>Жүктелуде...</p>
            </div>
          ) : (
            <div className="flex-1 overflow-y-auto p-6 md:p-10 scrollbar-hide">
              <div className="max-w-3xl mx-auto">
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
