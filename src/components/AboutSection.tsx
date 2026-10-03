import { Mail, Plus } from 'lucide-react';

export default function AboutSection() {
  return (
    <section id="about" className="bg-white/10 backdrop-blur-2xl border-t border-white/20 rounded-t-[25px] relative z-10 py-20 md:py-32 px-6">
      <div className="max-w-3xl mx-auto flex flex-col items-center">
        <p className="text-white text-base md:text-lg text-center leading-relaxed max-w-lg mb-10">
          Метод основан на 12 годах практики и разборе более 5000 сложных жизненных судеб.
        </p>
        
        <div className="flex flex-wrap justify-center gap-4 mb-20">
          <button onClick={() => window.location.href="https://web.tribute.tg/s/16WO"} className="bg-white text-black rounded-full flex items-center pr-6 pl-1.5 py-1.5 hover:bg-white/90 transition-colors group">
            <div className="w-8 h-8 rounded-full bg-black flex items-center justify-center mr-3 text-white">
              <Mail size={16} />
            </div>
            <span className="uppercase tracking-wide text-xs font-medium">Купить доступ</span>
          </button>
          
          <button className="bg-white/20 text-white rounded-full flex items-center pr-6 pl-1.5 py-1.5 hover:bg-[#CEBA9E] transition-colors group">
            <div className="w-8 h-8 rounded-full bg-black flex items-center justify-center mr-3 text-white">
              <Plus size={16} />
            </div>
            <span className="uppercase tracking-wide text-xs font-medium">Задать вопрос</span>
          </button>
        </div>
      </div>

      <div className="w-full flex items-center max-w-6xl mx-auto mb-20">
        <div className="w-2 h-2 rounded-full bg-white/20" />
        <div className="w-2 shrink-0" />
        <div className="flex-1 h-[2px] bg-white/20" />
        <div className="w-2 shrink-0" />
        <div className="w-2 h-2 rounded-full bg-white/20" />
      </div>

      <div className="max-w-6xl mx-auto flex flex-col md:flex-row gap-12 md:gap-20 items-start">
        <div className="flex flex-col items-start gap-4 flex-shrink-0">
          <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 256 256" fill="none">
            <path d="M 256 256 L 178 256 C 150.386 256 128 233.614 128 206 L 128 256 L 0 256 L 0 192 C 0 156.654 28.654 128 64 128 C 99.346 128 128 156.654 128 192 L 128 128 L 256 128 Z M 78 0 C 105.614 0 128 22.386 128 50 L 128 0 L 256 0 L 256 64 C 256 99.346 227.346 128 192 128 C 156.654 128 128 99.346 128 64 L 128 128 L 0 128 L 0 0 Z" fill="white" />
          </svg>
          <span className="text-xs uppercase tracking-widest font-semibold text-white whitespace-pre-line">
            {"Олеся /\nЛанская"}
          </span>
        </div>
        <p className="text-xl sm:text-2xl md:text-3xl lg:text-[36px] leading-[1.4] font-normal text-white">
          Я не даю волшебных таблеток и не обещаю, что вы станете счастливыми за три дня. Я даю холодный, отрезвляющий анализ ваших жизненных стратегий. Мы найдем вашу "слепую зону" и аккуратно перестроим ее, чтобы вы перестали наступать на одни и те же грабли.
        </p>
      </div>
    </section>
  );
}
