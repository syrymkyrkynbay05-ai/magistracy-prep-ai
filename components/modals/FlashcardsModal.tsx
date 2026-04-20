import React, { useState, useEffect } from 'react';
import { X, ChevronLeft, ChevronRight, RotateCw, Sparkles } from 'lucide-react';

interface Flashcard {
  id: string;
  front: string;
  back: string;
}

interface FlashcardsModalProps {
  isOpen: boolean;
  onClose: () => void;
  subjectId?: string; // Kept for compatibility, but we will shuffle all cards for now
}

// 20 high-quality flashcards for Magistracy Exam (TGO + IT)
const allFlashcards: Flashcard[] = [
  { id: '1', front: 'Дедукция дегеніміз не?', back: 'Жалпыдан жалқыға қарай ой қорыту тәсілі.' },
  { id: '2', front: 'Индукция дегеніміз не?', back: 'Жеке фактілерден немесе бақылаулардан жалпы қорытындыға келу.' },
  { id: '3', front: 'Силлогизм', back: 'Екі алғышарттан және бір қорытындыдан тұратын дедуктивті логикалық ой қорыту.' },
  { id: '4', front: 'Аналогия', back: 'Ұқсастық бойынша екі нысанның немесе құбылыстың бірдей қасиеттерін салыстыру.' },
  { id: '5', front: 'Абстракция', back: 'Нысанның елеусіз қасиеттерін ескермей, тек маңызды белгілерін бөліп көрсету.' },
  { id: '6', front: 'Факт пен пікірдің (Opinion) айырмашылығы', back: 'Факт - объективті түрде дәлелденген шындық. Пікір - жеке адамның көзқарасы немесе субъективті бағасы.' },
  { id: '7', front: 'Гипотеза', back: 'Дәлелдеуді немесе тексеруді қажет ететін ғылыми болжам.' },
  { id: '8', front: 'Тәуелсіз айнымалы (Independent variable)', back: 'Тәжірибе барысында зерттеуші өзгертетін қасиет немесе фактор.' },
  { id: '9', front: 'Тәуелді айнымалы (Dependent variable)', back: 'Тәуелсіз айнымалының өзгеруіне байланысты өзгеретін нәтиже немесе шама.' },
  { id: '10', front: 'Алгоритм деген не?', back: 'Белгілі бір есепті шешуге бағытталған нақты қадамдар мен ережелер тізбегі.' },
  { id: '11', front: 'O(1) алгоритмдік күрделілігі', back: 'Тұрақты уақыт. Деректер көлемі (n) қанша болса да, алгоритм бірдей уақытта орындалады.' },
  { id: '12', front: 'O(log n) алгоритмдік күрделілігі', back: 'Логарифмдік уақыт. Деректерді үнемі екіге бөліп отыру процесі (Мысалы: Екілік іздеу - Binary Search).' },
  { id: '13', front: 'Реляциондық деректер базасы (RDBMS)', back: 'Деректерді кесте (жолдар мен бағандар) түрінде сақтайтын жүйе (мысалы, PostgreSQL, MySQL).' },
  { id: '14', front: 'Primary Key (Бастапқы кілт)', back: 'Кестедегі әрбір жазбаны (қатарды) бірегей түрде анықтайтын баған. Қайталанбайды және null бола алмайды.' },
  { id: '15', front: 'Foreign Key (Сыртқы кілт)', back: 'Екі кесте арасында байланыс орнату үшін қолданылатын, басқа кестенің Primary Key-іне сілтейтін баған.' },
  { id: '16', front: 'Нормализация (Дерекқорда)', back: 'Дерекқордағы артық қайталануларды (redundancy) азайту және тұтастықты сақтау үшін кестелерді құрылымдау процесі.' },
  { id: '17', front: 'Полиморфизм (Polymorphism ООП)', back: 'Әртүрлі кластардың бірдей әдіс (method) атауын ортақ интерфейс арқылы әртүрлі мақсатта қолдану мүмкіндігі.' },
  { id: '18', front: 'Инкапсуляция (Encapsulation)', back: 'Деректерді және олармен жұмыс істейтін әдістерді бір класс ішіне жасырып, сырттан тікелей қол жеткізуді шектеу.' },
  { id: '19', front: 'Абстрактілі класс (Abstract class)', back: 'Тікелей объект (instance) жасауға болмайтын, тек басқа кластарға мұрагерлік (inheritance) беру үшін ғана қолданылатын класс.' },
  { id: '20', front: 'Сорттаудың ең жылдам алгоритмдері (Sorting)', back: 'Quick Sort (Жылдам сұрыптау) және Merge Sort (Біріктіріп сұрыптау). Олардың орташа күрделілігі O(n log n).' },
];

const FlashcardsModal: React.FC<FlashcardsModalProps> = ({ isOpen, onClose }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const [cards, setCards] = useState<Flashcard[]>([]);

  // Shuffle function
  const shuffleArray = (array: Flashcard[]) => {
    let shuffled = [...array];
    for (let i = shuffled.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
  };

  useEffect(() => {
    if (isOpen) {
      // Whenever modal opens, randomly shuffle the 20 cards!
      setCards(shuffleArray(allFlashcards));
      setCurrentIndex(0);
      setIsFlipped(false);
    }
  }, [isOpen]);

  if (!isOpen) return null;

  if (!cards || cards.length === 0) return null;

  const currentCard = cards[currentIndex];

  const handleNext = () => {
    setIsFlipped(false);
    setTimeout(() => {
      setCurrentIndex((prev) => (prev < cards.length - 1 ? prev + 1 : 0));
    }, 150);
  };

  const handlePrev = () => {
    setIsFlipped(false);
    setTimeout(() => {
        setCurrentIndex((prev) => (prev > 0 ? prev - 1 : cards.length - 1));
    }, 150);
  };

  const handleFlip = () => {
    setIsFlipped(!isFlipped);
  };

  return (
    <div className="fixed inset-0 z-[150] flex items-center justify-center bg-[#07090D]/80 backdrop-blur-xl p-4 animate-in fade-in duration-200">
      <div className="bg-[#0f172a] rounded-3xl w-full max-w-2xl shadow-2xl overflow-hidden flex flex-col h-[85vh] max-h-[800px] min-h-[550px] border border-white/10 relative">
        
        {/* Header */}
        <div className="px-6 py-5 border-b border-white/5 flex items-center justify-between shrink-0 bg-white/5">
          <div className="flex items-center gap-3">
            <div className="p-2 bg-gradient-to-tr from-blue-500 to-indigo-600 rounded-lg">
               <Sparkles className="w-5 h-5 text-white" />
            </div>
            <span className="text-white font-bold tracking-widest uppercase">Жаттау Карточкалары</span>
          </div>
          <button 
            onClick={onClose}
            className="p-2 text-slate-400 hover:text-white rounded-full hover:bg-white/10 transition-colors"
          >
            <X className="w-6 h-6" />
          </button>
        </div>

        {/* Content */}
        <div className="flex-1 p-6 md:p-10 flex flex-col items-center relative overflow-hidden bg-gradient-to-b from-[#0f172a] to-[#0b1120]">
            
            {/* Progress indicator */}
            <div className="mt-2 mb-6 z-10 shrink-0">
                <span className="bg-white/10 backdrop-blur-md px-8 py-3 rounded-full text-blue-300 font-black text-lg border border-white/20 shadow-xl tracking-widest">
                    {currentIndex + 1} / {cards.length}
                </span>
            </div>

            {/* Flashcard 3D Container */}
            <div 
                className="w-full max-w-md md:max-w-xl flex-1 mb-8 cursor-pointer group"
                onClick={handleFlip}
                style={{ perspective: '1000px' }}
            >
                <div 
                    className={`relative w-full h-full`}
                    style={{ 
                        transformStyle: 'preserve-3d', 
                        transition: 'transform 0.6s cubic-bezier(0.4, 0, 0.2, 1)',
                        transform: isFlipped ? 'rotateY(180deg)' : 'rotateY(0deg)'
                    }}
                >
                    {/* Front: Question */}
                    <div 
                        className="absolute inset-0 w-full h-full bg-slate-800 rounded-[2rem] shadow-2xl border border-white/10 flex flex-col items-center justify-center p-8 md:p-10 text-center group-hover:border-blue-500/50 transition-colors"
                        style={{ backfaceVisibility: 'hidden', WebkitBackfaceVisibility: 'hidden', transform: 'rotateY(0deg)' }}
                    >
                        <span className="absolute top-8 text-xs font-black text-slate-500 tracking-[0.2em] uppercase">Сұрақ / Термин</span>
                        <h2 className="text-2xl md:text-3xl font-extrabold text-white leading-tight">
                            {currentCard?.front}
                        </h2>
                        <div className="absolute bottom-8 text-blue-400 text-sm flex items-center gap-2 animate-bounce">
                            <RotateCw className="w-4 h-4" /> Аудару үшін басыңыз
                        </div>
                    </div>

                    {/* Back: Answer */}
                    <div 
                        className="absolute inset-0 w-full h-full bg-gradient-to-br from-blue-600 to-indigo-700 rounded-[2rem] shadow-[0_0_50px_rgba(59,130,246,0.3)] border border-blue-400/50 flex flex-col items-center justify-center p-8 md:p-10 text-center"
                        style={{ backfaceVisibility: 'hidden', WebkitBackfaceVisibility: 'hidden', transform: 'rotateY(180deg)' }}
                    >
                        <span className="absolute top-8 text-xs font-black text-blue-200 tracking-[0.2em] uppercase">Жауап / Анықтама</span>
                        <p className="text-xl md:text-2xl font-bold text-white leading-relaxed">
                            {currentCard?.back}
                        </p>
                    </div>
                </div>
            </div>

        </div>

        {/* Footer Navigation */}
        <div className="border-t border-white/5 p-6 shrink-0 flex items-center justify-center gap-12 bg-white/5">
            <button 
                onClick={handlePrev}
                className="w-14 h-14 flex items-center justify-center bg-white/5 hover:bg-white/20 text-slate-300 hover:text-white rounded-full transition-all hover:scale-110 active:scale-95 shadow-lg border border-white/10"
            >
                <ChevronLeft className="w-8 h-8 -ml-1" />
            </button>
            <div className="text-slate-400 font-bold tracking-widest text-sm uppercase select-none w-32 text-center">
                {isFlipped ? 'Сұраққа қайту' : 'Келесі'}
            </div>
            <button 
                onClick={handleNext}
                className="w-14 h-14 flex items-center justify-center bg-blue-500 hover:bg-blue-400 text-white rounded-full transition-all hover:scale-110 active:scale-95 shadow-[0_0_20px_rgba(59,130,246,0.4)] border border-blue-400/50"
            >
                <ChevronRight className="w-8 h-8 -mr-1" />
            </button>
        </div>

      </div>
    </div>
  );
};

export default FlashcardsModal;
