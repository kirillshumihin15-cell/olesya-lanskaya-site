import { useRef } from 'react';
import { ChevronLeft, ChevronRight } from 'lucide-react';

const reviews = [
  {
    name: "Ольга, 34 года",
    text: "Год ходила к психологам, отдала кучу денег, но мы всё топтались на месте. А тут Олеся за один аудио-разбор чужой (!) ситуации буквально вскрыла мою главную 'слепую зону'. Я проплакала полчаса, а потом наконец-то ушла из разрушающих отношений.",
    pain: "Скептицизм / Долгий результат"
  },
  {
    name: "Анонимный участник",
    text: "Очень боялась писать свою историю, так как ситуация супер-деликатная. Но здесь железная анонимность. Олеся разобрала мой случай без имен, очень бережно, но так отрезвляюще, что розовые очки разбились навсегда.",
    pain: "Страх осуждения / Анонимность"
  },
  {
    name: "Марина",
    text: "Я мама двоих детей и работаю фултайм. Искала что-то, что не требует сидеть с тетрадкой по вечерам и делать 'домашки'. Формат подкастов по 10-15 минут — просто спасение. Слушаю в машине, и инсайты догоняют весь день.",
    pain: "Нет времени / Сложные задания"
  },
  {
    name: "Елена Т.",
    text: "Устала от марафонов желаний, где льют воду про успешный успех. Здесь за 1190 рублей я получаю концентрат реальной терапии. Никакой эзотерики, только работа с нейронными связями и жесткая (в хорошем смысле) правда.",
    pain: "Усталость от прогревов и марафонов"
  },
  {
    name: "Виктория",
    text: "Всю жизнь выбирала эмоционально холодных мужчин. Только в этом канале поняла механизм, почему мой мозг считает это 'безопасной' зоной. Сейчас впервые за долгие годы строю нормальные, спокойные отношения без надрыва.",
    pain: "Повторяющиеся сценарии"
  }
];

export default function ReviewsSection() {
  const scrollRef = useRef<HTMLDivElement>(null);

  const scroll = (direction: 'left' | 'right') => {
    if (scrollRef.current) {
      const { scrollLeft, clientWidth } = scrollRef.current;
      const scrollTo = direction === 'left' ? scrollLeft - clientWidth * 0.8 : scrollLeft + clientWidth * 0.8;
      scrollRef.current.scrollTo({ left: scrollTo, behavior: 'smooth' });
    }
  };

  return (
    <section id="reviews" className="bg-[#0a0a0a] py-24 md:py-32 px-6 text-white border-t border-white/10 relative z-10 overflow-hidden">
      <div className="max-w-7xl mx-auto">
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-12 md:mb-16 gap-6">
          <h2 className="text-3xl sm:text-4xl lg:text-[42px] leading-[1.2] font-normal text-left">
            Что говорят участницы <br className="hidden md:block" /> закрытого канала
          </h2>
          
          <div className="flex gap-4">
            <button 
              onClick={() => scroll('left')}
              className="w-12 h-12 rounded-full border border-white/20 flex items-center justify-center hover:bg-white/10 transition-colors"
            >
              <ChevronLeft size={24} />
            </button>
            <button 
              onClick={() => scroll('right')}
              className="w-12 h-12 rounded-full border border-white/20 flex items-center justify-center hover:bg-white/10 transition-colors"
            >
              <ChevronRight size={24} />
            </button>
          </div>
        </div>
        
        {/* Carousel Container */}
        <div 
          ref={scrollRef}
          className="flex gap-6 overflow-x-auto snap-x snap-mandatory pb-8 -mx-6 px-6 md:mx-0 md:px-0"
          style={{ scrollbarWidth: 'none', msOverflowStyle: 'none' }}
        >
          {/* Hide Webkit Scrollbar */}
          <style>{`
            div::-webkit-scrollbar { display: none; }
          `}</style>
          
          {reviews.map((rev, i) => (
            <div 
              key={i} 
              className="snap-center shrink-0 w-[85vw] md:w-[400px] bg-white/5 backdrop-blur-sm border border-white/10 rounded-3xl p-8 flex flex-col gap-6 hover:bg-white/10 transition-colors group"
            >
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center text-sm font-bold text-white/80 group-hover:bg-white/20 transition-colors">
                    {rev.name[0]}
                  </div>
                  <span className="font-medium text-lg">{rev.name}</span>
                </div>
              </div>
              <p className="text-white/70 text-base leading-relaxed flex-1">
                "{rev.text}"
              </p>
              <div className="pt-4 border-t border-white/10">
                <span className="text-xs uppercase tracking-wider text-white/40 font-medium">
                  Решенная боль: {rev.pain}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
