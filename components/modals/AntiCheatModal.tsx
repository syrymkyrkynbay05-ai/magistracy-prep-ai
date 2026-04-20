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
      // Shortened to 2.5 seconds
      const timer = setTimeout(() => setShowWarning(false), 2500);
      return () => clearTimeout(timer);
    }
    if (warningsCount >= 5) {
      onAutoFinish();
    }
  }, [warningsCount, onAutoFinish]);

  // Fullscreen enforcement removed per request

  // Temporary Warning Toast - Refined and Smaller
  if (showWarning) {
    return (
      <div className="fixed top-12 left-1/2 -translate-x-1/2 z-[1000] animate-slide-down px-4 w-full max-w-[320px]">
        <div className="bg-red-600/95 backdrop-blur-md text-white px-4 py-3 rounded-2xl shadow-2xl flex items-center gap-3 border border-white/20">
          <div className="bg-white/20 p-2 rounded-xl">
            <AlertTriangle className="w-5 h-5 text-white animate-pulse" />
          </div>
          <div className="flex-1">
            <div className="font-extrabold uppercase tracking-tighter text-[11px] leading-tight">
              Ескерту ({warningsCount}/5)
            </div>
            <div className="text-[10px] font-bold opacity-90 leading-tight">
              Беттен шығуға болмайды!
            </div>
          </div>
        </div>
      </div>
    );
  }

  return null;
};

export default AntiCheatModal;
