import React, { useState } from 'react';
import { X, Atom, Search } from 'lucide-react';

interface PeriodicTableModalProps {
  isOpen: boolean;
  onClose: () => void;
}

// Periodic table data (simplified)
const elements = [
  // Period 1
  { symbol: 'H', name: 'Сутегі', number: 1, mass: 1.008, category: 'nonmetal', row: 1, col: 1 },
  { symbol: 'He', name: 'Гелий', number: 2, mass: 4.003, category: 'noble', row: 1, col: 18 },
  // Period 2
  { symbol: 'Li', name: 'Литий', number: 3, mass: 6.94, category: 'alkali', row: 2, col: 1 },
  { symbol: 'Be', name: 'Берилий', number: 4, mass: 9.012, category: 'alkaline', row: 2, col: 2 },
  { symbol: 'B', name: 'Бор', number: 5, mass: 10.81, category: 'metalloid', row: 2, col: 13 },
  { symbol: 'C', name: 'Көміртек', number: 6, mass: 12.01, category: 'nonmetal', row: 2, col: 14 },
  { symbol: 'N', name: 'Азот', number: 7, mass: 14.01, category: 'nonmetal', row: 2, col: 15 },
  { symbol: 'O', name: 'Оттегі', number: 8, mass: 16.00, category: 'nonmetal', row: 2, col: 16 },
  { symbol: 'F', name: 'Фтор', number: 9, mass: 19.00, category: 'halogen', row: 2, col: 17 },
  { symbol: 'Ne', name: 'Неон', number: 10, mass: 20.18, category: 'noble', row: 2, col: 18 },
  // Period 3
  { symbol: 'Na', name: 'Натрий', number: 11, mass: 22.99, category: 'alkali', row: 3, col: 1 },
  { symbol: 'Mg', name: 'Магний', number: 12, mass: 24.31, category: 'alkaline', row: 3, col: 2 },
  { symbol: 'Al', name: 'Алюминий', number: 13, mass: 26.98, category: 'post-transition', row: 3, col: 13 },
  { symbol: 'Si', name: 'Кремний', number: 14, mass: 28.09, category: 'metalloid', row: 3, col: 14 },
  { symbol: 'P', name: 'Фосфор', number: 15, mass: 30.97, category: 'nonmetal', row: 3, col: 15 },
  { symbol: 'S', name: 'Күкірт', number: 16, mass: 32.07, category: 'nonmetal', row: 3, col: 16 },
  { symbol: 'Cl', name: 'Хлор', number: 17, mass: 35.45, category: 'halogen', row: 3, col: 17 },
  { symbol: 'Ar', name: 'Аргон', number: 18, mass: 39.95, category: 'noble', row: 3, col: 18 },
  // Period 4
  { symbol: 'K', name: 'Калий', number: 19, mass: 39.10, category: 'alkali', row: 4, col: 1 },
  { symbol: 'Ca', name: 'Кальций', number: 20, mass: 40.08, category: 'alkaline', row: 4, col: 2 },
  { symbol: 'Fe', name: 'Темір', number: 26, mass: 55.85, category: 'transition', row: 4, col: 8 },
  { symbol: 'Cu', name: 'Мыс', number: 29, mass: 63.55, category: 'transition', row: 4, col: 11 },
  { symbol: 'Zn', name: 'Мырыш', number: 30, mass: 65.38, category: 'transition', row: 4, col: 12 },
  { symbol: 'Br', name: 'Бром', number: 35, mass: 79.90, category: 'halogen', row: 4, col: 17 },
  { symbol: 'Kr', name: 'Криптон', number: 36, mass: 83.80, category: 'noble', row: 4, col: 18 },
  // Period 5
  { symbol: 'Ag', name: 'Күміс', number: 47, mass: 107.87, category: 'transition', row: 5, col: 11 },
  { symbol: 'I', name: 'Йод', number: 53, mass: 126.90, category: 'halogen', row: 5, col: 17 },
  // Period 6
  { symbol: 'Au', name: 'Алтын', number: 79, mass: 196.97, category: 'transition', row: 6, col: 11 },
  { symbol: 'Hg', name: 'Сынап', number: 80, mass: 200.59, category: 'transition', row: 6, col: 12 },
  { symbol: 'Pb', name: 'Қорғасын', number: 82, mass: 207.2, category: 'post-transition', row: 6, col: 14 },
];

const categoryColors: Record<string, string> = {
  'alkali': 'bg-red-400',
  'alkaline': 'bg-orange-400',
  'transition': 'bg-yellow-400',
  'post-transition': 'bg-green-400',
  'metalloid': 'bg-teal-400',
  'nonmetal': 'bg-blue-400',
  'halogen': 'bg-indigo-400',
  'noble': 'bg-purple-400',
};

const PeriodicTableModal: React.FC<PeriodicTableModalProps> = ({ isOpen, onClose }) => {
  const [selectedElement, setSelectedElement] = useState<typeof elements[0] | null>(null);
  const [searchTerm, setSearchTerm] = useState('');

  if (!isOpen) return null;

  const filteredElements = searchTerm 
    ? elements.filter(el => 
        el.symbol.toLowerCase().includes(searchTerm.toLowerCase()) ||
        el.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        el.number.toString().includes(searchTerm)
      )
    : elements;

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-[100]" onClick={onClose}>
      <div 
        className="bg-white rounded-lg shadow-2xl w-[95%] max-w-4xl max-h-[90vh] overflow-hidden animate-fade-in"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="bg-gradient-to-r from-purple-600 to-indigo-600 text-white px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Atom className="w-6 h-6" />
            <h2 className="text-lg font-bold">Менделеев кестесі</h2>
          </div>
          <button onClick={onClose} className="hover:bg-white/20 p-1 rounded transition">
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Search */}
        <div className="px-6 py-3 bg-gray-50 border-b">
          <div className="relative">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
            <input
              type="text"
              placeholder="Элементті іздеу..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-10 pr-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
            />
          </div>
        </div>

        {/* Legend */}
        <div className="px-6 py-2 bg-gray-50 flex flex-wrap gap-3 text-xs border-b">
          <div className="flex items-center gap-1"><div className="w-3 h-3 bg-red-400 rounded"></div> Сілтілік металдар</div>
          <div className="flex items-center gap-1"><div className="w-3 h-3 bg-orange-400 rounded"></div> Сілтілік-жер</div>
          <div className="flex items-center gap-1"><div className="w-3 h-3 bg-yellow-400 rounded"></div> Өтпелі металдар</div>
          <div className="flex items-center gap-1"><div className="w-3 h-3 bg-blue-400 rounded"></div> Бейметалдар</div>
          <div className="flex items-center gap-1"><div className="w-3 h-3 bg-indigo-400 rounded"></div> Галогендер</div>
          <div className="flex items-center gap-1"><div className="w-3 h-3 bg-purple-400 rounded"></div> Инертті газдар</div>
        </div>

        {/* Content */}
        <div className="p-4 overflow-auto max-h-[50vh]">
          <div className="grid grid-cols-6 sm:grid-cols-9 md:grid-cols-12 gap-1">
            {filteredElements.map((el) => (
              <div
                key={el.symbol}
                onClick={() => setSelectedElement(el)}
                className={`
                  ${categoryColors[el.category]} 
                  p-2 rounded cursor-pointer hover:scale-110 transition-all text-center shadow-sm
                  ${selectedElement?.symbol === el.symbol ? 'ring-2 ring-black scale-110' : ''}
                `}
              >
                <div className="text-[10px] text-white/80">{el.number}</div>
                <div className="text-lg font-bold text-white">{el.symbol}</div>
                <div className="text-[9px] text-white/70 truncate">{el.mass}</div>
              </div>
            ))}
          </div>
        </div>

        {/* Selected Element Info */}
        {selectedElement && (
          <div className="px-6 py-4 bg-gray-100 border-t">
            <div className="flex items-center gap-4">
              <div className={`${categoryColors[selectedElement.category]} w-16 h-16 rounded-lg flex flex-col items-center justify-center text-white shadow-lg`}>
                <span className="text-xs">{selectedElement.number}</span>
                <span className="text-2xl font-bold">{selectedElement.symbol}</span>
              </div>
              <div>
                <div className="text-xl font-bold text-gray-800">{selectedElement.name}</div>
                <div className="text-gray-600">Атомдық масса: {selectedElement.mass}</div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default PeriodicTableModal;
