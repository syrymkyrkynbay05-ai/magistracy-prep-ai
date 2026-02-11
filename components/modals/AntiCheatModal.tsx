import React, { useEffect, useState } from 'react';
import { ShieldAlert, Maximize, AlertTriangle, XCircle } from 'lucide-react';

interface AntiCheatModalProps {
  warningsCount: number;
  isFullscreen: boolean;
  onEnterFullscreen: () => void;
  onAutoFinish: () => void;
}

const AntiCheatModal: React.FC<AntiCheatModalProps> = ({ 
  warningsCount, 
  isFullscreen, 
  onEnterFullscreen,
  onAutoFinish
}) => {
  const [showWarning, setShowWarning] = useState(false);

  useEffect(() => {
    if (warningsCount > 0 && warningsCount < 5) {
      setShowWarning(true);
      const timer = setTimeout(() => setShowWarning(false), 5000);
      return () => clearTimeout(timer);
    }
    if (warningsCount >= 5) {
      onAutoFinish();
    }
  }, [warningsCount, onAutoFinish]);

  // If not fullscreen - force overlay
  if (!isFullscreen) {
    return (
      <div className="fixed inset-0 bg-slate-900/95 backdrop-blur-md z-[999] flex items-center justify-center p-6 text-center">
        <div className="max-w-md w-full bg-white rounded-[32px] p-10 shadow-2xl animate-bounce-subtle">
          <div className="w-20 h-20 bg-blue-500/10 rounded-full flex items-center justify-center mx-auto mb-8 border border-blue-500/20">
            <Maximize className="w-10 h-10 text-blue-500" />
          </div>
          <h2 className="text-3xl font-black text-slate-900 mb-4 uppercase tracking-tighter italic">Толық экран режимі</h2>
          <p className="text-slate-500 font-medium mb-10 leading-relaxed">
            Тест тапсыру үшін толық экран режиміне өтуіңіз керек. Басқа терезелерге ауысуға тыйым салынады.
          </p>
          <button 
            onClick={onEnterFullscreen}
            className="w-full py-4 gradient-brand text-white font-black rounded-2xl shadow-[0_20px_40px_rgba(59,130,246,0.3)] hover:scale-[1.02] transition-all active:scale-95 uppercase tracking-widest"
          >
            Экранды ашу (F11)
          </button>
        </div>
      </div>
    );
  }

  // Temporary Warning Toast
  if (showWarning) {
    return (
      <div className="fixed top-20 left-1/2 -translate-x-1/2 z-[1000] animate-slide-down">
        <div className="bg-red-600 text-white px-8 py-4 rounded-2xl shadow-2xl flex items-center gap-4 border-2 border-white/20">
          <AlertTriangle className="w-8 h-8 animate-pulse" />
          <div>
            <div className="font-black uppercase tracking-widest text-sm">Ескерту! ({warningsCount}/5)</div>
            <div className="text-xs font-bold opacity-90">Сайттан басқа бетке өтуге тыйым салынған!</div>
          </div>
        </div>
      </div>
    );
  }

  return null;
};

export default AntiCheatModal;
