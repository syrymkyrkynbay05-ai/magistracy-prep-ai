import React, { useState, useRef, useEffect } from 'react';
import { X, Minus, Square, Menu, RotateCcw, MonitorUp, Delete } from 'lucide-react';

interface CalculatorModalProps {
  isOpen: boolean;
  onClose: () => void;
}

const CalculatorModal: React.FC<CalculatorModalProps> = ({ isOpen, onClose }) => {
  const [display, setDisplay] = useState('0');
  const [equation, setEquation] = useState('');
  const [hasResult, setHasResult] = useState(false);
  const [position, setPosition] = useState({ x: 100, y: 100 });
  const [isDragging, setIsDragging] = useState(false);
  const dragStartPos = useRef({ x: 0, y: 0 });

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
      const sanitized = fullEquation.replace(/×/g, '*').replace(/÷/g, '/');
      const result = eval(sanitized);
      // Format result to avoid very long decimals
      const formattedResult = Number.isInteger(result) ? result : parseFloat(result.toFixed(8));
      setDisplay(String(formattedResult));
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

  const handleClearEntry = () => {
    setDisplay('0');
  };

  const handleBackspace = () => {
    if (display.length > 1) {
      setDisplay(display.slice(0, -1));
    } else {
      setDisplay('0');
    }
  };

  const handleMathFunc = (type: string) => {
    const val = parseFloat(display);
    let res = 0;
    switch(type) {
      case '1/x': res = 1 / val; break;
      case 'x²': res = val * val; break;
      case '√': res = Math.sqrt(val); break;
      case '%': res = val / 100; break;
      case '±': res = -val; break;
    }
    setDisplay(String(Number.isInteger(res) ? res : parseFloat(res.toFixed(8))));
    setHasResult(true);
  };

  const rows = [
    ['%', 'CE', 'C', '⌫'],
    ['1/x', 'x²', '√', '÷'],
    ['7', '8', '9', '×'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['±', '0', '.', '='],
  ];

  const handleButton = (btn: string) => {
    if (!isNaN(parseInt(btn))) handleNumber(btn);
    else {
      switch (btn) {
        case '.': handleNumber('.'); break;
        case 'C': handleClear(); break;
        case 'CE': handleClearEntry(); break;
        case '⌫': handleBackspace(); break;
        case '=': handleEquals(); break;
        case '+': case '-': case '×': case '÷': handleOperator(btn); break;
        default: handleMathFunc(btn); break;
      }
    }
  };

  // Manual Drag Logic
  const handleMouseDown = (e: React.MouseEvent) => {
    setIsDragging(true);
    dragStartPos.current = {
      x: e.clientX - position.x,
      y: e.clientY - position.y
    };
  };

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      if (!isDragging) return;
      setPosition({
        x: e.clientX - dragStartPos.current.x,
        y: e.clientY - dragStartPos.current.y
      });
    };
    const handleMouseUp = () => setIsDragging(false);

    if (isDragging) {
      window.addEventListener('mousemove', handleMouseMove);
      window.addEventListener('mouseup', handleMouseUp);
    }
    return () => {
      window.removeEventListener('mousemove', handleMouseMove);
      window.removeEventListener('mouseup', handleMouseUp);
    };
  }, [isDragging]);

  return (
    <div className="fixed inset-0 pointer-events-none z-[100]">
      <div 
        style={{ left: position.x, top: position.y }}
        className="pointer-events-auto bg-[#1f1f1f] rounded-lg shadow-2xl w-[320px] overflow-hidden border border-white/10 absolute cursor-default flex flex-col"
      >
        {/* Windows 11 Style Title Bar */}
        <div 
          onMouseDown={handleMouseDown}
          className="bg-[#1f1f1f] text-white px-3 py-2 flex items-center justify-between cursor-grab active:cursor-grabbing"
        >
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-blue-500 rounded-sm flex items-center justify-center">
               <div className="w-2.5 h-0.5 bg-white mb-[1px]" />
               <div className="w-2.5 h-0.5 bg-white" />
            </div>
            <span className="text-[11px] font-medium text-gray-300">Есептегіш</span>
          </div>
          <div className="flex items-center">
             <button className="p-2 hover:bg-white/10 transition-colors"><Minus className="w-3 h-3 text-gray-400" /></button>
             <button className="p-2 hover:bg-white/10 transition-colors"><Square className="w-2.5 h-2.5 text-gray-400" /></button>
             <button onClick={onClose} className="p-2 hover:bg-[#e81123] transition-colors group">
               <X className="w-3.5 h-3.5 text-gray-400 group-hover:text-white" />
             </button>
          </div>
        </div>

        {/* Standard Menu Row */}
        <div className="flex items-center justify-between px-4 py-1">
           <div className="flex items-center gap-4">
             <button className="p-2 hover:bg-white/5 rounded transition-colors"><Menu className="w-5 h-5 text-white" /></button>
             <h2 className="text-xl font-bold text-white">Стандартты</h2>
             <button className="p-1 hover:bg-white/5 rounded transition-colors"><MonitorUp className="w-4 h-4 text-gray-400" /></button>
           </div>
           <button className="p-2 hover:bg-white/5 rounded transition-colors"><RotateCcw className="w-5 h-5 text-white" /></button>
        </div>

        {/* Display Area */}
        <div className="px-4 py-8 text-right select-none min-h-[120px] flex flex-col justify-end">
          <div className="text-gray-500 text-sm h-5 overflow-hidden mb-1 font-normal">{equation}</div>
          <div className="text-white text-6xl font-semibold tracking-tighter overflow-hidden text-ellipsis">
            {display}
          </div>
        </div>

        {/* Memory Row */}
        <div className="flex justify-around px-2 py-2 text-[11px] font-bold text-gray-400 opacity-60">
           <span>MC</span><span>MR</span><span>M+</span><span>M-</span><span>MS</span><span>Mv</span>
        </div>

        {/* Buttons Grid */}
        <div className="p-[2px] grid grid-cols-4 gap-[2px] bg-[#1f1f1f]">
          {rows.flat().map((btn, idx) => {
            const isNumber = !isNaN(parseInt(btn)) || btn === '.';
            const isEquals = btn === '=';
            
            return (
              <button
                key={idx}
                onClick={() => handleButton(btn)}
                className={`
                  h-12 rounded-[4px] text-sm font-medium transition-colors
                  ${isEquals 
                    ? 'bg-[#60cdff] text-black hover:bg-[#60cdff]/90 font-bold' 
                    : isNumber 
                      ? 'bg-[#3b3b3b] text-white hover:bg-[#404040]'
                      : 'bg-[#323232] text-white hover:bg-[#3b3b3b]'}
                `}
              >
                {btn === '⌫' ? <Delete className="w-4 h-4 mx-auto" /> : btn}
              </button>
            );
          })}
        </div>
      </div>
    </div>
  );
};

export default CalculatorModal;
