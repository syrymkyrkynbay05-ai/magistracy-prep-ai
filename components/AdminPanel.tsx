import React, { useState, useEffect } from 'react';
import { 
  Users, BarChart2, Calendar, ChevronRight, 
  Search, ArrowLeft, Award, Clock, Mail,
  CheckCircle, XCircle, Shield, Download, RefreshCw
} from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import { getAdminStats, getAdminUsers, getUserResultsAdmin } from '../services/apiService';

interface AdminPanelProps {
  onBack: () => void;
}

const AdminPanel: React.FC<AdminPanelProps> = ({ onBack }) => {
  const [stats, setStats] = useState<any>(null);
  const [users, setUsers] = useState<any[]>([]);
  const [selectedUser, setSelectedUser] = useState<any>(null);
  const [userResults, setUserResults] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');

  const fetchData = async () => {
    setLoading(true);
    try {
      const [s, u] = await Promise.all([getAdminStats(), getAdminUsers()]);
      setStats(s);
      setUsers(u);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleViewUser = async (user: any) => {
    setSelectedUser(user);
    try {
      const results = await getUserResultsAdmin(user.id);
      setUserResults(results);
    } catch (error) {
      console.error(error);
    }
  };

  const filteredUsers = users.filter(u => 
    u.full_name.toLowerCase().includes(search.toLowerCase()) || 
    u.email.toLowerCase().includes(search.toLowerCase())
  );

  if (loading && !stats) {
    return (
      <div className="min-h-screen bg-[#07090d] flex items-center justify-center">
        <RefreshCw className="w-8 h-8 text-blue-500 animate-spin" />
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-[#07090d] text-[#f8fafc] p-6 md:p-12">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-6 mb-12">
          <div>
            <button 
              onClick={selectedUser ? () => setSelectedUser(null) : onBack}
              className="flex items-center gap-2 text-slate-400 hover:text-white transition-colors mb-4 group"
            >
              <ArrowLeft className="w-4 h-4 group-hover:-translate-x-1 transition-transform" />
              {selectedUser ? 'Тізімге қайту' : 'Басты бетке'}
            </button>
            <h1 className="text-4xl font-black italic uppercase tracking-tighter">
              {selectedUser ? 'Пайдаланушы Мәліметі' : 'Админ Панель'}
            </h1>
          </div>

          {!selectedUser && (
            <div className="relative w-full md:w-80">
              <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-500" />
              <input 
                type="text" 
                placeholder="Қолданушыны іздеу..." 
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                className="w-full pl-12 pr-4 py-3 glass border-white/5 rounded-xl outline-none focus:border-blue-500/50 transition-colors"
              />
            </div>
          )}
        </div>

        {/* Stats Grid */}
        {!selectedUser && (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
            {[
              { label: 'Жалпы Қолданушылар', value: stats?.totalUsers || 0, icon: Users, color: 'text-blue-400' },
              { label: 'Тест тапсыру саны', value: stats?.totalTests || 0, icon: BarChart2, color: 'text-purple-400' },
              { label: 'Орташа балл', value: `${stats?.averageScore || 0}%`, icon: Award, color: 'text-emerald-400' },
            ].map((s, i) => (
              <motion.div 
                key={i}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: i * 0.1 }}
                className="glass p-8 rounded-3xl border-white/5 relative overflow-hidden group"
              >
                <div className="absolute top-0 right-0 p-8 opacity-5 group-hover:opacity-10 transition-opacity">
                  <s.icon className="w-24 h-24" />
                </div>
                <div className={`w-12 h-12 rounded-2xl bg-white/5 flex items-center justify-center mb-6 ${s.color}`}>
                  <s.icon className="w-6 h-6" />
                </div>
                <div className="text-3xl font-black mb-1">{s.value}</div>
                <div className="text-xs font-black text-slate-500 uppercase tracking-widest">{s.label}</div>
              </motion.div>
            ))}
          </div>
        )}

        {/* User Table or User Details */}
        <AnimatePresence mode="wait">
          {!selectedUser ? (
            <motion.div 
              key="list"
              initial={{ opacity: 0 }} 
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="glass rounded-3xl border-white/5 overflow-hidden"
            >
              <div className="overflow-x-auto">
                <table className="w-full text-left border-collapse">
                  <thead>
                    <tr className="border-b border-white/5 bg-white/5">
                      <th className="px-8 py-6 text-[10px] font-black text-slate-500 uppercase tracking-[0.2em]">Пайдаланушы</th>
                      <th className="px-8 py-6 text-[10px] font-black text-slate-500 uppercase tracking-[0.2em]">Тест саны</th>
                      <th className="px-8 py-6 text-[10px] font-black text-slate-500 uppercase tracking-[0.2em]">Макс. балл</th>
                      <th className="px-8 py-6 text-[10px] font-black text-slate-500 uppercase tracking-[0.2em]">Орташа</th>
                      <th className="px-8 py-6 text-[10px] font-black text-slate-500 uppercase tracking-[0.2em]">Тіркелген күні</th>
                      <th className="px-8 py-6 text-[10px] font-black text-slate-500 uppercase tracking-[0.2em]">Әрекет</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-white/5">
                    {filteredUsers.map((u, i) => (
                      <tr key={u.id} className="hover:bg-white/[0.02] transition-colors group">
                        <td className="px-8 py-6">
                          <div className="flex items-center gap-4">
                            <div className="w-10 h-10 rounded-full bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center font-black text-sm">
                              {u.full_name[0]}
                            </div>
                            <div>
                              <div className="font-bold text-sm flex items-center gap-2">
                                {u.full_name}
                                {u.is_admin && <Shield className="w-3 h-3 text-blue-400" />}
                              </div>
                              <div className="text-xs text-slate-500">{u.email}</div>
                            </div>
                          </div>
                        </td>
                        <td className="px-8 py-6 font-bold">{u.test_count}</td>
                        <td className="px-8 py-6 font-bold text-emerald-400">{u.max_score}</td>
                        <td className="px-8 py-6 font-bold">{u.avg_score}%</td>
                        <td className="px-8 py-6 text-xs text-slate-500">
                          {new Date(u.created_at).toLocaleDateString()}
                        </td>
                        <td className="px-8 py-6">
                          <button 
                            onClick={() => handleViewUser(u)}
                            className="p-2 hover:bg-white/10 rounded-lg transition-colors group-hover:translate-x-1"
                          >
                            <ChevronRight className="w-5 h-5" />
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </motion.div>
          ) : (
            <motion.div 
              key="details"
              initial={{ opacity: 0, x: 20 }} 
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -20 }}
              className="grid grid-cols-1 lg:grid-cols-12 gap-8"
            >
              {/* User Summary Sidebar */}
              <div className="lg:col-span-4 space-y-6">
                <div className="glass p-8 rounded-3xl border-white/5 text-center">
                  <div className="w-24 h-24 rounded-full bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center font-black text-3xl mx-auto mb-6 shadow-2xl">
                    {selectedUser.full_name[0]}
                  </div>
                  <h2 className="text-2xl font-black mb-2">{selectedUser.full_name}</h2>
                  <p className="text-slate-500 text-sm mb-8">{selectedUser.email}</p>
                  
                  <div className="grid grid-cols-2 gap-4 text-left">
                    <div className="bg-white/5 p-4 rounded-2xl">
                      <div className="text-xs font-black text-slate-500 uppercase mb-1">Статус</div>
                      <div className="flex items-center gap-2 text-sm font-bold">
                        {selectedUser.is_active ? <CheckCircle className="w-3 h-3 text-emerald-400" /> : <XCircle className="w-3 h-3 text-red-400" />}
                        {selectedUser.is_active ? 'Белсенді' : 'Блокталған'}
                      </div>
                    </div>
                    <div className="bg-white/5 p-4 rounded-2xl">
                      <div className="text-xs font-black text-slate-500 uppercase mb-1">Тіркелу</div>
                      <div className="text-sm font-bold">{new Date(selectedUser.created_at).toLocaleDateString()}</div>
                    </div>
                  </div>
                </div>

                <div className="glass p-8 rounded-3xl border-white/5">
                  <h3 className="text-xs font-black text-slate-500 uppercase tracking-widest mb-6">Байланыс мәліметтері</h3>
                  <div className="space-y-4">
                    <div className="flex items-center gap-4 text-sm">
                      <Mail className="w-4 h-4 text-blue-400" />
                      <span className="font-bold">{selectedUser.email}</span>
                    </div>
                    <div className="flex items-center gap-4 text-sm">
                      <Clock className="w-4 h-4 text-blue-400" />
                      <span className="font-bold">Соңғы активтілік: {new Date().toLocaleDateString()}</span>
                    </div>
                  </div>
                </div>
              </div>

              {/* User Test History */}
              <div className="lg:col-span-8">
                <div className="glass rounded-3xl border-white/5 overflow-hidden">
                  <div className="p-8 border-b border-white/5 flex justify-between items-center">
                    <h3 className="text-lg font-black uppercase tracking-tight">Тест Тарихы</h3>
                    <button className="text-xs font-black text-blue-400 uppercase tracking-widest flex items-center gap-2 hover:opacity-70">
                      <Download className="w-3 h-3" /> Экспорт (CSV)
                    </button>
                  </div>
                  <div className="divide-y divide-white/5">
                    {userResults.length > 0 ? userResults.map((r, i) => (
                      <div key={r.id} className="p-8 hover:bg-white/[0.02] transition-colors">
                        <div className="flex justify-between items-start mb-6">
                          <div>
                            <div className="text-xl font-black mb-1">{r.total_score} <span className="text-slate-500 text-sm">/ {r.max_score} балл</span></div>
                            <div className="text-[10px] font-black text-slate-500 uppercase tracking-widest">
                              {new Date(r.created_at).toLocaleString()}
                            </div>
                          </div>
                          <div className={`px-4 py-1.5 rounded-full text-[10px] font-black uppercase tracking-widest ${r.total_score > (r.max_score * 0.7) ? 'bg-emerald-500/20 text-emerald-400' : 'bg-orange-500/20 text-orange-400'}`}>
                            {r.total_score > (r.max_score * 0.7) ? 'Жоғары нәтиже' : 'Орташа нәтиже'}
                          </div>
                        </div>
                        
                        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                          {Object.entries(r.subject_scores).map(([sid, sdata]: [any, any]) => (
                            <div key={sid} className="bg-white/5 p-3 rounded-xl">
                              <div className="text-[9px] font-black text-slate-600 uppercase mb-1 truncate">{sid}</div>
                              <div className="text-xs font-black">{sdata.score} / {sdata.max}</div>
                            </div>
                          ))}
                        </div>
                      </div>
                    )) : (
                      <div className="p-20 text-center text-slate-500 italic">Тест тапсырылмаған</div>
                    )}
                  </div>
                </div>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
};

export default AdminPanel;
