import { useState, useEffect } from 'react';

export default function CookieBanner() {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const accepted = localStorage.getItem('cookiesAccepted');
    if (!accepted) {
      // Small delay to not aggressive prompt instantly
      setTimeout(() => setIsVisible(true), 1500);
    }
  }, []);

  if (!isVisible) return null;

  return (
    <div className="fixed bottom-4 left-4 right-4 md:left-auto md:right-8 md:bottom-8 md:max-w-sm bg-white/90 backdrop-blur-md text-[#321C04] p-5 rounded-2xl shadow-2xl z-[100] border border-white/20">
      <p className="text-sm font-medium leading-relaxed mb-4">
        Мы используем файлы cookie, чтобы сайт работал лучше. Оставаясь здесь, вы соглашаетесь с нашей политикой.
      </p>
      <div className="flex gap-3">
        <button 
          onClick={() => {
            localStorage.setItem('cookiesAccepted', 'true');
            setIsVisible(false);
          }}
          className="flex-1 bg-[#321C04] text-[#FFF9F2] text-sm font-medium px-4 py-2 rounded-xl hover:bg-[#1F1003] transition-colors"
        >
          Принять
        </button>
      </div>
    </div>
  );
}
