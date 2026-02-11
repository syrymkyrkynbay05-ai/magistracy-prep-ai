import React, { useState, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  GraduationCap, Mail, Lock, User, Eye, EyeOff, 
  ArrowRight, ArrowLeft, Sparkles, Shield, AlertCircle, CheckCircle, KeyRound
} from 'lucide-react';
import { register, login, forgotPassword, resetPassword } from '../services/authService';

interface AuthScreenProps {
  onAuthSuccess: (user: { id: number; email: string; full_name: string }) => void;
}

type AuthMode = 'login' | 'register' | 'forgot' | 'otp' | 'newpass';

const AuthScreen: React.FC<AuthScreenProps> = ({ onAuthSuccess }) => {
  const [mode, setMode] = useState<AuthMode>('login');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [fullName, setFullName] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  
  // OTP State
  const [otpDigits, setOtpDigits] = useState(['', '', '', '', '', '']);
  const otpRefs = useRef<(HTMLInputElement | null)[]>([]);
  const [newPassword, setNewPassword] = useState('');
  const [countdown, setCountdown] = useState(0);

  // Countdown timer for resend
  useEffect(() => {
    if (countdown <= 0) return;
    const timer = setTimeout(() => setCountdown(c => c - 1), 1000);
    return () => clearTimeout(timer);
  }, [countdown]);

  const clearMessages = () => { setError(''); setSuccess(''); };

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    clearMessages();
    setIsLoading(true);
    try {
      const result = await login(email, password);
      onAuthSuccess(result.user);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    clearMessages();
    if (password.length < 6) { setError('Құпия сөз кемінде 6 таңбадан тұруы керек'); return; }
    setIsLoading(true);
    try {
      const result = await register(email, fullName, password);
      onAuthSuccess(result.user);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleForgotPassword = async (e: React.FormEvent) => {
    e.preventDefault();
    clearMessages();
    setIsLoading(true);
    try {
      await forgotPassword(email);
      setSuccess('Код email-ге жіберілді!');
      setCountdown(300); // 5 min
      setMode('otp');
      setOtpDigits(['', '', '', '', '', '']);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  // OTP input handler
  const handleOtpChange = (index: number, value: string) => {
    if (value.length > 1) value = value.slice(-1);
    if (value && !/^\d$/.test(value)) return;

    const newDigits = [...otpDigits];
    newDigits[index] = value;
    setOtpDigits(newDigits);

    // Auto-focus next
    if (value && index < 5) {
      otpRefs.current[index + 1]?.focus();
    }
  };

  const handleOtpKeyDown = (index: number, e: React.KeyboardEvent) => {
    if (e.key === 'Backspace' && !otpDigits[index] && index > 0) {
      otpRefs.current[index - 1]?.focus();
    }
  };

  const handleOtpPaste = (e: React.ClipboardEvent) => {
    e.preventDefault();
    const pasted = e.clipboardData.getData('text').replace(/\D/g, '').slice(0, 6);
    const newDigits = [...otpDigits];
    for (let i = 0; i < pasted.length; i++) {
      newDigits[i] = pasted[i];
    }
    setOtpDigits(newDigits);
    if (pasted.length === 6) {
      otpRefs.current[5]?.focus();
    }
  };

  const handleOtpSubmit = () => {
    const code = otpDigits.join('');
    if (code.length !== 6) { setError('6 санды код жазыңыз'); return; }
    clearMessages();
    setMode('newpass');
  };

  const handleResetPassword = async (e: React.FormEvent) => {
    e.preventDefault();
    clearMessages();
    if (newPassword.length < 6) { setError('Құпия сөз кемінде 6 таңбадан тұруы керек'); return; }
    setIsLoading(true);
    try {
      const otpCode = otpDigits.join('');
      const message = await resetPassword(email, otpCode, newPassword);
      setSuccess(message);
      setTimeout(() => { setMode('login'); clearMessages(); setNewPassword(''); }, 2000);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleResendOtp = async () => {
    if (countdown > 0) return;
    clearMessages();
    setIsLoading(true);
    try {
      await forgotPassword(email);
      setSuccess('Жаңа код жіберілді!');
      setCountdown(300);
      setOtpDigits(['', '', '', '', '', '']);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const formatTime = (seconds: number) => {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${m}:${s.toString().padStart(2, '0')}`;
  };

  const switchMode = (newMode: AuthMode) => {
    setMode(newMode);
    clearMessages();
  };

  // Shared input class
  const inputClass = "w-full pl-12 pr-4 py-4 bg-white/5 border border-white/10 rounded-xl outline-none focus:border-blue-500/50 transition-colors text-white placeholder-slate-600 font-bold";
  const inputClassPass = "w-full pl-12 pr-12 py-4 bg-white/5 border border-white/10 rounded-xl outline-none focus:border-blue-500/50 transition-colors text-white placeholder-slate-600 font-bold";
  const btnClass = "w-full py-4 gradient-brand rounded-xl font-black text-white flex items-center justify-center gap-3 hover:shadow-[0_0_30px_rgba(59,130,246,0.3)] transition-all active:scale-[0.98] disabled:opacity-50";

  return (
    <div className="min-h-screen bg-[#07090d] text-[#f8fafc] flex items-center justify-center px-4 py-8 relative overflow-hidden">
      {/* Background */}
      <div className="absolute w-[400px] h-[400px] bg-blue-600/10 rounded-full blur-[100px] top-[-100px] right-[-100px]" />
      <div className="absolute w-[300px] h-[300px] bg-purple-600/10 rounded-full blur-[80px] bottom-[-50px] left-[-50px]" />
      
      <motion.div
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5 }}
        className="w-full max-w-md relative z-10"
      >
        {/* Logo */}
        <div className="text-center mb-10">
          <div className="w-24 h-24 flex items-center justify-center mx-auto mb-4 relative">
             <div className="absolute inset-0 bg-blue-500/20 blur-2xl rounded-full" />
             <img src="/logo no bg, blue.svg" alt="MagisCore Logo" className="w-full h-full object-contain relative z-10" />
          </div>
          <h1 className="text-4xl font-extrabold tracking-tight uppercase">
            Magis<span className="text-blue-500">Core</span>
          </h1>
          <p className="text-slate-500 text-sm mt-2 font-medium">
            {mode === 'login' && 'Аккаунтқа кіру'}
            {mode === 'register' && 'Жаңа аккаунт құру'}
            {mode === 'forgot' && 'Парольді қалпына келтіру'}
            {mode === 'otp' && 'Кодты жазыңыз'}
            {mode === 'newpass' && 'Жаңа пароль орнату'}
          </p>
        </div>

        {/* Card */}
        <div className="glass-dark rounded-3xl p-8 border border-white/5 shadow-2xl">
          
          {/* Messages */}
          <AnimatePresence>
            {error && (
              <motion.div 
                initial={{ opacity: 0, height: 0 }} animate={{ opacity: 1, height: 'auto' }} exit={{ opacity: 0, height: 0 }}
                className="flex items-center gap-3 px-4 py-3 bg-red-500/10 border border-red-500/20 rounded-xl mb-6 text-red-400 text-sm font-bold"
              >
                <AlertCircle className="w-4 h-4 shrink-0" /> {error}
              </motion.div>
            )}
            {success && (
              <motion.div 
                initial={{ opacity: 0, height: 0 }} animate={{ opacity: 1, height: 'auto' }} exit={{ opacity: 0, height: 0 }}
                className="flex items-center gap-3 px-4 py-3 bg-green-500/10 border border-green-500/20 rounded-xl mb-6 text-green-400 text-sm font-bold"
              >
                <CheckCircle className="w-4 h-4 shrink-0" /> {success}
              </motion.div>
            )}
          </AnimatePresence>

          {/* ====== LOGIN ====== */}
          {mode === 'login' && (
            <form onSubmit={handleLogin} className="space-y-5">
              <div className="relative">
                <Mail className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-500" />
                <input type="email" value={email} onChange={e => setEmail(e.target.value)} required placeholder="Email" className={inputClass} />
              </div>
              <div className="relative">
                <Lock className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-500" />
                <input type={showPassword ? 'text' : 'password'} value={password} onChange={e => setPassword(e.target.value)} required placeholder="Құпия сөз" className={inputClassPass} />
                <button type="button" onClick={() => setShowPassword(!showPassword)} className="absolute right-4 top-1/2 -translate-y-1/2 text-slate-500 hover:text-white transition-colors">
                  {showPassword ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
                </button>
              </div>
              <div className="flex justify-end">
                <button type="button" onClick={() => switchMode('forgot')} className="text-xs font-bold text-blue-400 hover:text-blue-300 transition-colors">
                  Парольді ұмыттыңыз ба?
                </button>
              </div>
              <button type="submit" disabled={isLoading} className={btnClass}>
                {isLoading ? 'Жүктелуде...' : <><span>Кіру</span> <ArrowRight className="w-5 h-5" /></>}
              </button>
              <div className="text-center pt-4 border-t border-white/5">
                <span className="text-slate-500 text-sm font-medium">Аккаунтыңыз жоқ па? </span>
                <button type="button" onClick={() => switchMode('register')} className="text-sm font-black text-blue-400 hover:text-blue-300">Тіркелу</button>
              </div>
            </form>
          )}

          {/* ====== REGISTER ====== */}
          {mode === 'register' && (
            <form onSubmit={handleRegister} className="space-y-5">
              <div className="relative">
                <User className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-500" />
                <input type="text" value={fullName} onChange={e => setFullName(e.target.value)} required placeholder="Аты-жөніңіз" className={inputClass} />
              </div>
              <div className="relative">
                <Mail className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-500" />
                <input type="email" value={email} onChange={e => setEmail(e.target.value)} required placeholder="Email" className={inputClass} />
              </div>
              <div className="relative">
                <Lock className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-500" />
                <input type={showPassword ? 'text' : 'password'} value={password} onChange={e => setPassword(e.target.value)} required placeholder="Құпия сөз (кемінде 6 таңба)" className={inputClassPass} />
                <button type="button" onClick={() => setShowPassword(!showPassword)} className="absolute right-4 top-1/2 -translate-y-1/2 text-slate-500 hover:text-white transition-colors">
                  {showPassword ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
                </button>
              </div>
              <button type="submit" disabled={isLoading} className={btnClass}>
                {isLoading ? 'Жүктелуде...' : <><Sparkles className="w-5 h-5" /> <span>Тіркелу</span></>}
              </button>
              <div className="text-center pt-4 border-t border-white/5">
                <span className="text-slate-500 text-sm font-medium">Аккаунтыңыз бар ма? </span>
                <button type="button" onClick={() => switchMode('login')} className="text-sm font-black text-blue-400 hover:text-blue-300">Кіру</button>
              </div>
            </form>
          )}

          {/* ====== FORGOT PASSWORD (enter email) ====== */}
          {mode === 'forgot' && (
            <form onSubmit={handleForgotPassword} className="space-y-5">
              <p className="text-slate-400 text-sm font-medium mb-2">Email мекенжайыңызды жазыңыз. Біз сізге 6 санды код жібереміз.</p>
              <div className="relative">
                <Mail className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-500" />
                <input type="email" value={email} onChange={e => setEmail(e.target.value)} required placeholder="Email" className={inputClass} />
              </div>
              <button type="submit" disabled={isLoading} className={btnClass}>
                {isLoading ? 'Жіберілуде...' : <><Shield className="w-5 h-5" /> <span>Код жіберу</span></>}
              </button>
              <button type="button" onClick={() => switchMode('login')} className="w-full flex items-center justify-center gap-2 text-sm font-bold text-slate-400 hover:text-white transition-colors pt-2">
                <ArrowLeft className="w-4 h-4" /> Кіру бетіне қайту
              </button>
            </form>
          )}

          {/* ====== OTP INPUT ====== */}
          {mode === 'otp' && (
            <div className="space-y-6">
              <div className="text-center">
                <div className="w-14 h-14 bg-blue-500/10 rounded-2xl flex items-center justify-center mx-auto mb-4 border border-blue-500/20">
                  <KeyRound className="w-7 h-7 text-blue-400" />
                </div>
                <p className="text-slate-400 text-sm font-medium">
                  <span className="text-white font-bold">{email}</span> мекенжайына 6 санды код жіберілді
                </p>
              </div>

              {/* OTP Inputs */}
              <div className="flex justify-center gap-3" onPaste={handleOtpPaste}>
                {otpDigits.map((digit, i) => (
                  <input
                    key={i}
                    ref={el => { otpRefs.current[i] = el; }}
                    type="text"
                    inputMode="numeric"
                    maxLength={1}
                    value={digit}
                    onChange={e => handleOtpChange(i, e.target.value)}
                    onKeyDown={e => handleOtpKeyDown(i, e)}
                    className={`w-12 h-14 text-center text-2xl font-black rounded-xl border-2 outline-none transition-all bg-white/5
                      ${digit ? 'border-blue-500 text-white' : 'border-white/10 text-slate-400'}
                      focus:border-blue-400 focus:ring-2 focus:ring-blue-500/20`}
                  />
                ))}
              </div>

              {/* Timer & Resend */}
              <div className="text-center">
                {countdown > 0 ? (
                  <p className="text-slate-500 text-sm font-medium">
                    Қайта жіберу: <span className="text-blue-400 font-bold">{formatTime(countdown)}</span>
                  </p>
                ) : (
                  <button onClick={handleResendOtp} disabled={isLoading} className="text-sm font-bold text-blue-400 hover:text-blue-300 transition-colors">
                    Кодты қайта жіберу
                  </button>
                )}
              </div>

              <button onClick={handleOtpSubmit} className={btnClass}>
                <span>Растау</span> <ArrowRight className="w-5 h-5" />
              </button>
              
              <button type="button" onClick={() => switchMode('login')} className="w-full flex items-center justify-center gap-2 text-sm font-bold text-slate-400 hover:text-white transition-colors">
                <ArrowLeft className="w-4 h-4" /> Кіру бетіне қайту
              </button>
            </div>
          )}

          {/* ====== NEW PASSWORD ====== */}
          {mode === 'newpass' && (
            <form onSubmit={handleResetPassword} className="space-y-5">
              <div className="text-center mb-2">
                <CheckCircle className="w-10 h-10 text-green-400 mx-auto mb-3" />
                <p className="text-green-400 text-sm font-bold">Код расталды!</p>
                <p className="text-slate-400 text-sm font-medium mt-1">Жаңа құпия сөзіңізді жазыңыз</p>
              </div>
              <div className="relative">
                <Lock className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-500" />
                <input 
                  type={showPassword ? 'text' : 'password'} value={newPassword} onChange={e => setNewPassword(e.target.value)} required
                  placeholder="Жаңа құпия сөз (кемінде 6 таңба)" className={inputClassPass}
                />
                <button type="button" onClick={() => setShowPassword(!showPassword)} className="absolute right-4 top-1/2 -translate-y-1/2 text-slate-500 hover:text-white transition-colors">
                  {showPassword ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
                </button>
              </div>
              <button type="submit" disabled={isLoading} className={btnClass}>
                {isLoading ? 'Жаңартылуда...' : <><CheckCircle className="w-5 h-5" /> <span>Парольді жаңарту</span></>}
              </button>
            </form>
          )}
        </div>

        {/* Footer */}
        <p className="text-center text-[10px] text-slate-700 mt-10 font-bold tracking-[0.2em] uppercase">
          © 2026 MagisCore. Secure Auth.
        </p>
      </motion.div>
    </div>
  );
};

export default AuthScreen;
