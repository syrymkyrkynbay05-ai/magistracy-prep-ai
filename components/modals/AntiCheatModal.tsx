import React, { useEffect, useState } from 'react';
import { AlertTriangle } from 'lucide-react';

interface AntiCheatModalProps {
  warningsCount: number;
  isFullscreen: boolean;
  onEnterFullscreen: () => void;
  onAutoFinish: () => void;
}

const AntiCheatModal: React.FC<AntiCheatModalProps> = ({ 
  warningsCount, 
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

  // Fullscreen enforcement removed per request

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
