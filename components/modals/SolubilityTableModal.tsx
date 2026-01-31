import React from 'react';
import { X, Grid3X3 } from 'lucide-react';

interface SolubilityTableModalProps {
  isOpen: boolean;
  onClose: () => void;
}

// Solubility data: 'Р' = растворимое (soluble), 'М' = мало растворимое, 'Н' = не растворимое, '-' = не существует
const anions = ['OH⁻', 'F⁻', 'Cl⁻', 'Br⁻', 'I⁻', 'S²⁻', 'SO₄²⁻', 'NO₃⁻', 'CO₃²⁻', 'PO₄³⁻', 'SiO₃²⁻'];
const cations = ['H⁺', 'Li⁺', 'Na⁺', 'K⁺', 'NH₄⁺', 'Ba²⁺', 'Ca²⁺', 'Mg²⁺', 'Fe²⁺', 'Fe³⁺', 'Cu²⁺', 'Zn²⁺', 'Ag⁺', 'Pb²⁺', 'Al³⁺'];

// Solubility matrix [cation index][anion index]
const solubilityData: string[][] = [
  // H⁺
  ['Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'Н'],
  // Li⁺
  ['Р', 'М', 'Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'М', 'Р'],
  // Na⁺
  ['Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'Р'],
  // K⁺
  ['Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'Р'],
  // NH₄⁺
  ['Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'Р', 'Р', '-'],
  // Ba²⁺
  ['Р', 'М', 'Р', 'Р', 'Р', 'Р', 'Н', 'Р', 'Н', 'Н', 'Н'],
  // Ca²⁺
  ['М', 'Н', 'Р', 'Р', 'Р', 'Р', 'М', 'Р', 'Н', 'Н', 'Н'],
  // Mg²⁺
  ['Н', 'Н', 'Р', 'Р', 'Р', '-', 'Р', 'Р', 'Н', 'Н', 'Н'],
  // Fe²⁺
  ['Н', 'М', 'Р', 'Р', 'Р', 'Н', 'Р', 'Р', 'Н', 'Н', 'Н'],
  // Fe³⁺
  ['Н', 'Н', 'Р', 'Р', '-', 'Н', 'Р', 'Р', '-', 'Н', 'Н'],
  // Cu²⁺
  ['Н', 'Р', 'Р', 'Р', '-', 'Н', 'Р', 'Р', '-', 'Н', '-'],
  // Zn²⁺
  ['Н', 'Р', 'Р', 'Р', 'Р', 'Н', 'Р', 'Р', 'Н', 'Н', 'Н'],
  // Ag⁺
  ['-', 'Р', 'Н', 'Н', 'Н', 'Н', 'М', 'Р', 'Н', 'Н', '-'],
  // Pb²⁺
  ['Н', 'Н', 'М', 'М', 'Н', 'Н', 'Н', 'Р', 'Н', 'Н', 'Н'],
  // Al³⁺
  ['Н', 'М', 'Р', 'Р', 'Р', '-', 'Р', 'Р', '-', 'Н', 'Н'],
];

const getCellColor = (value: string) => {
  switch (value) {
    case 'Р': return 'bg-green-100 text-green-700';
    case 'М': return 'bg-yellow-100 text-yellow-700';
    case 'Н': return 'bg-red-100 text-red-700';
    case '-': return 'bg-gray-200 text-gray-400';
    default: return 'bg-white';
  }
};

const SolubilityTableModal: React.FC<SolubilityTableModalProps> = ({ isOpen, onClose }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-[100]" onClick={onClose}>
      <div 
        className="bg-white rounded-lg shadow-2xl w-[95%] max-w-5xl max-h-[90vh] overflow-hidden animate-fade-in"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="bg-gradient-to-r from-teal-600 to-cyan-600 text-white px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Grid3X3 className="w-6 h-6" />
            <h2 className="text-lg font-bold">Ерігіштік кестесі</h2>
          </div>
          <button onClick={onClose} className="hover:bg-white/20 p-1 rounded transition">
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Legend */}
        <div className="px-6 py-3 bg-gray-50 border-b flex items-center gap-6 text-sm">
          <div className="flex items-center gap-2">
            <div className="w-6 h-6 bg-green-100 text-green-700 rounded flex items-center justify-center font-bold text-xs">Р</div>
            <span>Ериді</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-6 h-6 bg-yellow-100 text-yellow-700 rounded flex items-center justify-center font-bold text-xs">М</div>
            <span>Аз ериді</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-6 h-6 bg-red-100 text-red-700 rounded flex items-center justify-center font-bold text-xs">Н</div>
            <span>Ерімейді</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-6 h-6 bg-gray-200 text-gray-400 rounded flex items-center justify-center font-bold text-xs">−</div>
            <span>Жоқ</span>
          </div>
        </div>

        {/* Table */}
        <div className="p-4 overflow-auto max-h-[65vh]">
          <table className="w-full border-collapse text-sm">
            <thead>
              <tr>
                <th className="sticky left-0 top-0 z-20 bg-gray-800 text-white p-2 border border-gray-700 min-w-[60px]">
                  Катион / Анион
                </th>
                {anions.map((anion, idx) => (
                  <th key={idx} className="sticky top-0 z-10 bg-gray-700 text-white p-2 border border-gray-600 min-w-[50px] text-xs">
                    {anion}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {cations.map((cation, cIdx) => (
                <tr key={cIdx}>
                  <td className="sticky left-0 bg-gray-700 text-white p-2 border border-gray-600 font-medium text-xs">
                    {cation}
                  </td>
                  {anions.map((_, aIdx) => {
                    const value = solubilityData[cIdx]?.[aIdx] || '-';
                    return (
                      <td 
                        key={aIdx} 
                        className={`p-2 border border-gray-300 text-center font-bold text-sm ${getCellColor(value)}`}
                      >
                        {value}
                      </td>
                    );
                  })}
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* Footer */}
        <div className="px-6 py-3 bg-gray-50 border-t text-center text-xs text-gray-500">
          Қышқыл ортасындағы тұздардың ерігіштігі (25°C)
        </div>
      </div>
    </div>
  );
};

export default SolubilityTableModal;
