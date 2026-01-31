import React, { useState } from 'react';
import { X, Calculator, Delete } from 'lucide-react';

interface CalculatorModalProps {
  isOpen: boolean;
  onClose: () => void;
}

const CalculatorModal: React.FC<CalculatorModalProps> = ({ isOpen, onClose }) => {
  const [display, setDisplay] = useState('0');
  const [equation, setEquation] = useState('');
  const [hasResult, setHasResult] = useState(false);

  if (!isOpen) return null;

  const handleNumber = (num: string) => {
    if (hasResult) {
      setDisplay(num);
      setEquation('');
      setHasResult(false);
    } else if (display === '0' && num !== '.') {
      setDisplay(num);
    } else if (num === '.' && display.includes('.')) {
      return;
    } else {
      setDisplay(display + num);
    }
  };

  const handleOperator = (op: string) => {
    setEquation(display + ' ' + op + ' ');
    setDisplay('0');
    setHasResult(false);
  };

  const handleEquals = () => {
    try {
      const fullEquation = equation + display;
      // Replace × with * and ÷ with /
      const sanitized = fullEquation.replace(/×/g, '*').replace(/÷/g, '/');
      const result = eval(sanitized);
      setDisplay(String(result));
      setEquation('');
      setHasResult(true);
    } catch {
      setDisplay('Қате');
      setHasResult(true);
    }
  };

  const handleClear = () => {
    setDisplay('0');
    setEquation('');
    setHasResult(false);
  };

  const handleBackspace = () => {
    if (display.length > 1) {
      setDisplay(display.slice(0, -1));
    } else {
      setDisplay('0');
    }
  };

  const buttons = [
    ['C', '⌫', '%', '÷'],
    ['7', '8', '9', '×'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['±', '0', '.', '='],
  ];

  const handleButton = (btn: string) => {
    switch (btn) {
      case 'C':
        handleClear();
        break;
      case '⌫':
        handleBackspace();
        break;
      case '±':
        setDisplay(String(parseFloat(display) * -1));
        break;
      case '%':
        setDisplay(String(parseFloat(display) / 100));
        break;
      case '=':
        handleEquals();
        break;
      case '+':
      case '-':
      case '×':
      case '÷':
        handleOperator(btn);
        break;
      default:
        handleNumber(btn);
    }
  };

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-[100]" onClick={onClose}>
      <div 
        className="bg-gray-900 rounded-2xl shadow-2xl w-[320px] overflow-hidden animate-fade-in"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="bg-gray-800 text-white px-4 py-3 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Calculator className="w-5 h-5 text-gray-400" />
            <h2 className="text-sm font-semibold text-gray-300">Калькулятор</h2>
          </div>
          <button onClick={onClose} className="hover:bg-white/10 p-1 rounded transition">
            <X className="w-4 h-4 text-gray-400" />
          </button>
        </div>

        {/* Display */}
        <div className="bg-gray-900 px-6 py-4 text-right">
          <div className="text-gray-500 text-sm h-5 overflow-hidden">{equation}</div>
          <div className="text-white text-4xl font-light tracking-wider overflow-hidden text-ellipsis">
            {display}
          </div>
        </div>

        {/* Buttons */}
        <div className="p-3 grid grid-cols-4 gap-2">
          {buttons.flat().map((btn, idx) => {
            const isOperator = ['+', '-', '×', '÷', '='].includes(btn);
            const isFunction = ['C', '⌫', '%', '±'].includes(btn);
            
            return (
              <button
                key={idx}
                onClick={() => handleButton(btn)}
                className={`
                  h-14 rounded-full text-xl font-medium transition-all active:scale-95
                  ${btn === '=' 
                    ? 'bg-orange-500 text-white hover:bg-orange-400' 
                    : isOperator 
                      ? 'bg-orange-500 text-white hover:bg-orange-400'
                      : isFunction 
                        ? 'bg-gray-600 text-white hover:bg-gray-500' 
                        : 'bg-gray-700 text-white hover:bg-gray-600'}
                `}
              >
                {btn}
              </button>
            );
          })}
        </div>
      </div>
    </div>
  );
};

export default CalculatorModal;
