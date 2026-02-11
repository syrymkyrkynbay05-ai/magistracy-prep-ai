import React from 'react';

interface BarChartProps {
  data: number[];
  labels: string[];
  colors?: string[];
  title?: string;
}

interface PieChartProps {
  data: number[];
  labels: string[];
  colors?: string[];
}

interface LineChartProps {
  data: number[];
  labels: string[];
  color?: string;
}

interface TableChartProps {
  headers: string[];
  rows: (string | number)[][];
}

interface ComparisonTableProps {
  title?: string;
  columnA: { header: string; content: string };
  columnB: { header: string; content: string };
  question?: string;
}

interface CircleProps {
  radius: number;
  label?: string;
  showCenter?: boolean;
}

interface MathExpressionProps {
  expressions: { label: string; value: string }[];
  question?: string;
}

type ChartData = 
  | { type: 'bar'; data: number[]; labels: string[]; colors?: string[]; title?: string }
  | { type: 'pie'; data: number[]; labels: string[]; colors?: string[] }
  | { type: 'line'; data: number[]; labels: string[]; color?: string }
  | { type: 'table'; headers: string[]; rows: (string | number)[][] }
  | { type: 'comparison'; columnA: string; columnB: string }
  | { type: 'comparison_table'; title?: string; columnA: { header: string; content: string }; columnB: { header: string; content: string }; question?: string }
  | { type: 'circle'; radius: number; label?: string; showCenter?: boolean }
  | { type: 'math'; expressions: { label: string; value: string }[]; question?: string };

interface ChartRendererProps {
  chartData: ChartData;
}

const DEFAULT_COLORS = [
  '#3b82f6', // blue
  '#ef4444', // red
  '#f59e0b', // amber
  '#10b981', // green
  '#8b5cf6', // violet
  '#ec4899', // pink
  '#06b6d4', // cyan
  '#f97316', // orange
];

// Bar Chart Component
const BarChart: React.FC<BarChartProps> = ({ data, labels, colors = DEFAULT_COLORS, title }) => {
  const maxValue = Math.max(...data);
  
  return (
    <div className="bg-white rounded-xl p-6 shadow-sm border border-slate-200">
      {title && <h4 className="text-sm font-semibold text-slate-600 mb-4 text-center">{title}</h4>}
      <div className="flex items-end justify-center gap-4 h-48">
        {data.map((value, index) => (
          <div key={index} className="flex flex-col items-center gap-2">
            <span className="text-sm font-bold text-slate-700">{value}</span>
            <div 
              className="w-12 md:w-16 rounded-t-lg transition-all duration-500"
              style={{ 
                height: `${(value / maxValue) * 150}px`,
                backgroundColor: colors[index % colors.length]
              }}
            />
            <span className="text-xs font-medium text-slate-600 text-center max-w-16 truncate">
              {labels[index]}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};

// Pie Chart Component
const PieChart: React.FC<PieChartProps> = ({ data, labels, colors = DEFAULT_COLORS }) => {
  const total = data.reduce((a, b) => a + b, 0);
  let cumulativePercent = 0;
  
  const slices = data.map((value, index) => {
    const percent = (value / total) * 100;
    const startAngle = cumulativePercent * 3.6;
    cumulativePercent += percent;
    return { value, percent, startAngle, color: colors[index % colors.length], label: labels[index] };
  });

  // Create conic gradient
  let gradientStops = '';
  let currentDeg = 0;
  slices.forEach((slice, i) => {
    const endDeg = currentDeg + (slice.percent * 3.6);
    gradientStops += `${slice.color} ${currentDeg}deg ${endDeg}deg${i < slices.length - 1 ? ', ' : ''}`;
    currentDeg = endDeg;
  });

  return (
    <div className="bg-white rounded-xl p-6 shadow-sm border border-slate-200">
      <div className="flex flex-col md:flex-row items-center gap-6">
        <div 
          className="w-32 h-32 rounded-full shadow-inner"
          style={{ background: `conic-gradient(${gradientStops})` }}
        />
        <div className="flex flex-col gap-2">
          {slices.map((slice, index) => (
            <div key={index} className="flex items-center gap-2">
              <div 
                className="w-4 h-4 rounded-sm"
                style={{ backgroundColor: slice.color }}
              />
              <span className="text-sm text-slate-700">
                <strong>{slice.label}:</strong> {slice.value} ({slice.percent.toFixed(0)}%)
              </span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

// Line Chart Component
const LineChart: React.FC<LineChartProps> = ({ data, labels, color = '#3b82f6' }) => {
  const maxValue = Math.max(...data);
  const minValue = Math.min(...data);
  const range = maxValue - minValue || 1;
  
  const points = data.map((value, index) => {
    const x = (index / (data.length - 1)) * 280 + 20;
    const y = 130 - ((value - minValue) / range) * 110;
    return { x, y, value };
  });

  const pathD = points.map((p, i) => `${i === 0 ? 'M' : 'L'} ${p.x} ${p.y}`).join(' ');

  return (
    <div className="bg-white rounded-xl p-6 shadow-sm border border-slate-200">
      <svg viewBox="0 0 320 160" className="w-full h-40">
        {/* Grid lines */}
        {[0, 1, 2, 3, 4].map(i => (
          <line key={i} x1="20" y1={20 + i * 27.5} x2="300" y2={20 + i * 27.5} stroke="#e2e8f0" strokeWidth="1" />
        ))}
        
        {/* Line */}
        <path d={pathD} fill="none" stroke={color} strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" />
        
        {/* Points */}
        {points.map((p, i) => (
          <g key={i}>
            <circle cx={p.x} cy={p.y} r="5" fill={color} />
            <text x={p.x} y={p.y - 10} textAnchor="middle" className="text-xs fill-slate-600 font-medium">{p.value}</text>
            <text x={p.x} y="155" textAnchor="middle" className="text-xs fill-slate-500">{labels[i]}</text>
          </g>
        ))}
      </svg>
    </div>
  );
};

// Table Chart Component
const TableChart: React.FC<TableChartProps> = ({ headers, rows }) => {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
      <table className="w-full text-sm">
        <thead>
          <tr className="bg-slate-100">
            {headers.map((header, i) => (
              <th key={i} className="px-4 py-3 text-left font-semibold text-slate-700 border-b border-slate-200">
                {header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, i) => (
            <tr key={i} className="hover:bg-slate-50">
              {row.map((cell, j) => (
                <td key={j} className="px-4 py-3 text-slate-600 border-b border-slate-100">
                  {cell}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

// Simple Comparison Box Component
const ComparisonBox: React.FC<{ columnA: string; columnB: string }> = ({ columnA, columnB }) => {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
      <div className="grid grid-cols-2">
        <div className="p-4 bg-blue-50 border-r border-slate-200">
          <div className="text-xs font-bold text-blue-600 uppercase tracking-wider mb-2">А шамасы</div>
          <div className="text-sm text-slate-700 font-medium">{columnA}</div>
        </div>
        <div className="p-4 bg-amber-50">
          <div className="text-xs font-bold text-amber-600 uppercase tracking-wider mb-2">В шамасы</div>
          <div className="text-sm text-slate-700 font-medium">{columnB}</div>
        </div>
      </div>
    </div>
  );
};

// NEW: Advanced Comparison Table (like HPV example)
const ComparisonTable: React.FC<ComparisonTableProps> = ({ title, columnA, columnB, question }) => {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
      {title && (
        <div className="bg-slate-50 px-4 py-3 border-b border-slate-200">
          <p className="text-sm text-slate-700 leading-relaxed">{title}</p>
        </div>
      )}
      <table className="w-full text-sm">
        <thead>
          <tr className="bg-slate-100">
            <th className="px-4 py-3 text-center font-bold text-blue-700 border-b border-r border-slate-200 w-1/2">
              {columnA.header}
            </th>
            <th className="px-4 py-3 text-center font-bold text-amber-700 border-b border-slate-200 w-1/2">
              {columnB.header}
            </th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td className="px-4 py-4 text-slate-700 border-r border-slate-200 align-top">
              <div className="whitespace-pre-line leading-relaxed">{columnA.content}</div>
            </td>
            <td className="px-4 py-4 text-slate-700 align-top">
              <div className="whitespace-pre-line leading-relaxed">{columnB.content}</div>
            </td>
          </tr>
        </tbody>
      </table>
      {question && (
        <div className="bg-blue-50 px-4 py-3 border-t border-slate-200">
          <p className="text-sm font-semibold text-blue-800">{question}</p>
        </div>
      )}
    </div>
  );
};

// NEW: Circle/Geometry Component
const CircleDiagram: React.FC<CircleProps> = ({ radius, label, showCenter = true }) => {
  const size = 180;
  const cx = size / 2;
  const cy = size / 2;
  const r = 70;
  
  return (
    <div className="bg-white rounded-xl p-6 shadow-sm border border-slate-200">
      <svg viewBox={`0 0 ${size} ${size}`} className="w-48 h-48 mx-auto">
        {/* Circle */}
        <circle 
          cx={cx} 
          cy={cy} 
          r={r} 
          fill="none" 
          stroke="#3b82f6" 
          strokeWidth="2"
        />
        
        {/* Center point */}
        {showCenter && (
          <>
            <circle cx={cx} cy={cy} r="3" fill="#3b82f6" />
            <text x={cx - 8} y={cy + 4} className="text-xs fill-slate-600 font-medium">O</text>
          </>
        )}
        
        {/* Radius line */}
        <line 
          x1={cx} 
          y1={cy} 
          x2={cx + r} 
          y2={cy} 
          stroke="#3b82f6" 
          strokeWidth="2"
        />
        
        {/* Radius label */}
        <text 
          x={cx + r/2} 
          y={cy - 8} 
          textAnchor="middle" 
          className="text-sm fill-slate-700 font-semibold"
        >
          R = {radius} см
        </text>
        
        {/* Optional label */}
        {label && (
          <text 
            x={cx} 
            y={size - 10} 
            textAnchor="middle" 
            className="text-xs fill-slate-500"
          >
            {label}
          </text>
        )}
      </svg>
    </div>
  );
};

// NEW: Math Expression Component
const MathExpression: React.FC<MathExpressionProps> = ({ expressions, question }) => {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
      {question && (
        <div className="bg-slate-50 px-4 py-3 border-b border-slate-200">
          <p className="text-sm text-slate-700 font-medium">{question}</p>
        </div>
      )}
      <table className="w-full text-sm">
        <thead>
          <tr className="bg-slate-100">
            {expressions.map((expr, i) => (
              <th key={i} className={`px-4 py-3 text-center font-bold border-b border-slate-200 ${i === 0 ? 'text-blue-700 border-r' : 'text-amber-700'}`}>
                {expr.label}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          <tr>
            {expressions.map((expr, i) => (
              <td key={i} className={`px-4 py-6 text-center align-middle ${i === 0 ? 'border-r border-slate-200' : ''}`}>
                <span className="text-xl font-serif text-slate-800 font-medium italic">
                  {expr.value}
                </span>
              </td>
            ))}
          </tr>
        </tbody>
      </table>
    </div>
  );
};

// Main ChartRenderer Component
const ChartRenderer: React.FC<ChartRendererProps> = ({ chartData }) => {
  switch (chartData.type) {
    case 'bar':
      return <BarChart data={chartData.data} labels={chartData.labels} colors={chartData.colors} title={chartData.title} />;
    case 'pie':
      return <PieChart data={chartData.data} labels={chartData.labels} colors={chartData.colors} />;
    case 'line':
      return <LineChart data={chartData.data} labels={chartData.labels} color={chartData.color} />;
    case 'table':
      return <TableChart headers={chartData.headers} rows={chartData.rows} />;
    case 'comparison':
      return <ComparisonBox columnA={chartData.columnA} columnB={chartData.columnB} />;
    case 'comparison_table':
      return <ComparisonTable title={chartData.title} columnA={chartData.columnA} columnB={chartData.columnB} question={chartData.question} />;
    case 'circle':
      return <CircleDiagram radius={chartData.radius} label={chartData.label} showCenter={chartData.showCenter} />;
    case 'math':
      return <MathExpression expressions={chartData.expressions} question={chartData.question} />;
    default:
      return null;
  }
};

export default ChartRenderer;
export type { ChartData };
