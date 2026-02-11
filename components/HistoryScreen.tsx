import React, { useEffect, useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  History, 
  Trash2, 
  ChevronRight, 
  Calendar, 
  Award, 
  CheckCircle2, 
  Loader2,
  ArrowLeft,
  Search
} from 'lucide-react';
import { getHistory, deleteHistoryItem, HistoryItem } from '../services/authService';

interface HistoryScreenProps {
  onBack: () => void;
}

const HistoryScreen: React.FC<HistoryScreenProps> = ({ onBack }) => {
  const [history, setHistory] = useState<HistoryItem[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState('');
  const [searchQuery, setSearchQuery] = useState('');

  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    try {
      setIsLoading(true);
      const data = await getHistory();
      setHistory(data);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleDelete = async (id: number) => {
    if (!window.confirm('Бұл нәтижені өшіргіңіз келе ме?')) return;
    try {
      await deleteHistoryItem(id);
      setHistory(prev => prev.filter(item => item.id !== id));
    } catch (err: any) {
      alert(err.message);
    }
  };

  const formatDate = (dateStr: string) => {
    const date = new Date(dateStr);
    return date.toLocaleDateString('kk-KZ', {
      day: 'numeric',
      month: 'long',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const filteredHistory = history.filter(item => {
    const dateStr = formatDate(item.created_at).toLowerCase();
    return dateStr.includes(searchQuery.toLowerCase());
  });

  return (
    <div className="min-h-screen bg-[#0a0c10] text-slate-200 p-4 md:p-8">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="flex flex-col md:flex-row md:items-center justify-between mb-8 gap-4">
          <div className="flex items-center gap-4">
            <button 
              onClick={onBack}
              className="p-2 hover:bg-slate-800/50 rounded-full transition-colors border border-slate-800"
            >
              <ArrowLeft className="w-5 h-5" />
            </button>
            <div>
              <h1 className="text-2xl font-bold flex items-center gap-2">
                <History className="w-6 h-6 text-blue-500" />
                Менің нәтижелерім
              </h1>
              <p className="text-slate-400 text-sm">Барлық тапсырылған тесттер тарихы</p>
            </div>
          </div>

          <div className="relative group">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-500 group-focus-within:text-blue-500 transition-colors" />
            <input 
              type="text"
              placeholder="Күн бойынша іздеу..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="bg-slate-900/50 border border-slate-800 rounded-xl py-2 pl-10 pr-4 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500/50 transition-all w-full md:w-64"
            />
          </div>
        </div>

        {/* Content */}
        {isLoading ? (
          <div className="flex flex-col items-center justify-center py-20 gap-4">
            <Loader2 className="w-10 h-10 text-blue-500 animate-spin" />
            <p className="text-slate-400">Тарих жүктелуде...</p>
          </div>
        ) : error ? (
          <div className="bg-red-500/10 border border-red-500/20 text-red-400 p-4 rounded-xl text-center">
            {error}
            <button onClick={fetchHistory} className="block mx-auto mt-2 text-sm underline">Қайталау</button>
          </div>
        ) : filteredHistory.length === 0 ? (
          <div className="text-center py-20 bg-slate-900/20 border border-dashed border-slate-800 rounded-2xl">
            <History className="w-16 h-16 text-slate-800 mx-auto mb-4" />
            <h3 className="text-lg font-medium text-slate-300">Тарих бос</h3>
            <p className="text-slate-500 max-w-xs mx-auto mt-2">
              Сіз әлі тест тапсырмағансыз. Тест тапсырған соң нәтижелер осында көрінеді.
            </p>
          </div>
        ) : (
          <div className="grid gap-4">
            <AnimatePresence mode='popLayout'>
              {filteredHistory.map((item, index) => (
                <motion.div
                  key={item.id}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, scale: 0.95 }}
                  transition={{ delay: index * 0.05 }}
                  className="group relative bg-slate-900/40 border border-slate-800 hover:border-slate-700 rounded-2xl p-4 md:p-6 transition-all"
                >
                  <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                    <div className="flex items-start gap-4">
                      <div className={`p-3 rounded-xl ${
                        item.total_score / item.max_score >= 0.7 
                          ? 'bg-emerald-500/10 text-emerald-500' 
                          : 'bg-blue-500/10 text-blue-500'
                      }`}>
                        <Award className="w-6 h-6" />
                      </div>
                      <div>
                        <div className="flex items-center gap-2 mb-1">
                          <Calendar className="w-3.5 h-3.5 text-slate-500" />
                          <span className="text-sm font-medium text-slate-300">
                            {formatDate(item.created_at)}
                          </span>
                        </div>
                        <h3 className="text-xl font-bold text-white">
                          Score: {item.total_score} / {item.max_score}
                        </h3>
                        <div className="flex items-center gap-4 mt-2">
                          <span className="flex items-center gap-1.5 text-xs text-slate-400">
                            <CheckCircle2 className="w-3.5 h-3.5 text-slate-500" />
                            {item.correct_count} дұрыс жауап
                          </span>
                          <span className="text-xs text-slate-600">|</span>
                          <span className="text-xs text-slate-400">
                            {item.total_questions} сұрақ барлығы
                          </span>
                        </div>
                      </div>
                    </div>

                    <div className="flex items-center gap-3">
                      <div className="text-right hidden md:block mr-4">
                        <div className="text-2xl font-black text-blue-500/50">
                          {Math.round((item.total_score / item.max_score) * 100)}%
                        </div>
                        <div className="text-[10px] uppercase tracking-wider text-slate-600 font-bold">Табыстылық</div>
                      </div>
                      <button
                        onClick={() => handleDelete(item.id)}
                        className="p-2.5 text-slate-500 hover:text-red-500 hover:bg-red-500/10 rounded-xl transition-all border border-transparent hover:border-red-500/20"
                        title="Өшіру"
                      >
                        <Trash2 className="w-5 h-5" />
                      </button>
                      <button className="p-2.5 text-slate-500 hover:text-white rounded-xl transition-all border border-slate-800 hover:border-slate-600">
                        <ChevronRight className="w-5 h-5" />
                      </button>
                    </div>
                  </div>
                  
                  {/* Progress Bar (Decorative) */}
                  <div className="absolute bottom-0 left-6 right-6 h-0.5 bg-slate-800/50 rounded-full overflow-hidden">
                    <motion.div 
                      initial={{ width: 0 }}
                      animate={{ width: `${(item.total_score / item.max_score) * 100}%` }}
                      className={`h-full ${
                         item.total_score / item.max_score >= 0.7 ? 'bg-emerald-500' : 'bg-blue-500'
                      }`}
                    />
                  </div>
                </motion.div>
              ))}
            </AnimatePresence>
          </div>
        )}
      </div>
    </div>
  );
};

export default HistoryScreen;
