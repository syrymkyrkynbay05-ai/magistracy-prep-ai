import React, { useState, useRef, useEffect } from 'react';
import { Play, Pause, AlertCircle } from 'lucide-react';

interface AudioPlayerProps {
  src: string;
  maxPlays?: number;
}

const AudioPlayer: React.FC<AudioPlayerProps> = ({ src, maxPlays = 2 }) => {
  const audioRef = useRef<HTMLAudioElement>(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [progress, setProgress] = useState(0);
  const [playCount, setPlayCount] = useState(0);
  const [duration, setDuration] = useState(0);

  useEffect(() => {
    // Reset state when source changes
    setIsPlaying(false);
    setProgress(0);
    setPlayCount(0);
    if (audioRef.current) {
      audioRef.current.load();
    }
  }, [src]);

  const togglePlay = () => {
    if (!audioRef.current) return;

    if (isPlaying) {
      audioRef.current.pause();
    } else {
      if (playCount >= maxPlays) return;
      
      const promise = audioRef.current.play();
      if (promise !== undefined) {
        promise.catch(error => {
          console.error("Audio playback error:", error);
        });
      }
    }
    setIsPlaying(!isPlaying);
  };

  const handleTimeUpdate = () => {
    if (audioRef.current) {
      const current = audioRef.current.currentTime;
      const total = audioRef.current.duration;
      setDuration(total);
      setProgress((current / total) * 100);
    }
  };

  const handleEnded = () => {
    setIsPlaying(false);
    setPlayCount(prev => prev + 1);
  };

  const formatTime = (time: number) => {
    if (isNaN(time)) return "0:00";
    const minutes = Math.floor(time / 60);
    const seconds = Math.floor(time % 60);
    return `${minutes}:${seconds.toString().padStart(2, '0')}`;
  };

  const isLimitReached = playCount >= maxPlays;

  return (
    <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-6">
      <div className="flex items-center justify-between mb-2">
        <h4 className="text-sm font-bold text-blue-800 flex items-center gap-2">
          <span className="bg-blue-600 text-white text-xs px-2 py-0.5 rounded">AUDIO</span>
          Тыңдалым тапсырмасы
        </h4>
        <div className="text-xs font-semibold text-blue-600">
          Тыңдалды: {playCount}/{maxPlays}
        </div>
      </div>

      <audio
        ref={audioRef}
        src={src}
        onTimeUpdate={handleTimeUpdate}
        onEnded={handleEnded}
        onLoadedMetadata={(e) => setDuration(e.currentTarget.duration)}
      />

      <div className="flex items-center gap-4">
        <button
          onClick={togglePlay}
          disabled={isLimitReached && !isPlaying}
          className={`
            w-10 h-10 rounded-full flex items-center justify-center transition-all
            ${isLimitReached && !isPlaying
              ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
              : 'bg-blue-600 text-white hover:bg-blue-700 shadow-md active:scale-95'}
          `}
        >
          {isPlaying ? <Pause className="w-5 h-5" /> : <Play className="w-5 h-5 ml-0.5" />}
        </button>

        <div className="flex-1">
          <div className="h-2 bg-blue-200 rounded-full overflow-hidden">
            <div 
              className="h-full bg-blue-600 transition-all duration-300 ease-linear"
              style={{ width: `${progress}%` }}
            />
          </div>
          <div className="flex justify-between mt-1 text-xs text-blue-500 font-medium">
            <span>{formatTime(audioRef.current?.currentTime || 0)}</span>
            <span>{formatTime(duration)}</span>
          </div>
        </div>
      </div>

      {isLimitReached && !isPlaying && (
        <div className="mt-3 flex items-start gap-2 text-xs text-amber-700 bg-amber-50 p-2 rounded border border-amber-200">
          <AlertCircle className="w-4 h-4 shrink-0" />
          <span>Сіз бұл аудионы тыңдау лимитінен асып кеттіңіз. Енді сұрақтарға жауап беруге көшіңіз.</span>
        </div>
      )}
    </div>
  );
};

export default AudioPlayer;
