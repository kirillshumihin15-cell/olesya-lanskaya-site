import { useState } from 'react';
import { Plus, Minus } from 'lucide-react';

const faqs = [
  {
    q: "Как отменить подписку?",
    a: "В любой момент через официального бота Tribute в Telegram. Отписка происходит в один клик, никаких скрытых условий и удержаний."
  },
  {
    q: "А если мне не подойдет формат?",
    a: "Вы можете зайти на один месяц, чтобы примерить формат на себя. Если поймете, что метод вам не близок — легко отпишетесь. Но 92% участников продлевают подписку на второй месяц."
  },
  {
    q: "Анонимно ли участие в канале?",
    a: "Абсолютно. Вы можете использовать любой псевдоним в Telegram, а ваши личные истории разбираются без указания имен и контактов. Безопасность — наш главный приоритет."
  },
  {
    q: "У меня нет времени слушать долгие лекции",
    a: "Вам и не придется. Формат канала — это емкие аудио-сессии и разборы по 10-15 минут. Только концентрат пользы, который удобно слушать за рулем или во время прогулки."
  }
];

export default function FAQSection() {
  const [openIdx, setOpenIdx] = useState<number | null>(null);

  return (
    <section id="faq" className="bg-[#0a0a0a] py-24 md:py-32 px-6 text-white border-t border-white/10 relative z-10">
      <div className="max-w-3xl mx-auto">
        <h2 className="text-3xl sm:text-4xl lg:text-[42px] leading-[1.2] font-normal mb-16 text-center">
          Частые вопросы
        </h2>
        
        <div className="flex flex-col gap-4">
          {faqs.map((faq, idx) => {
            const isOpen = openIdx === idx;
            return (
              <div 
                key={idx} 
                className="bg-white/5 border border-white/10 rounded-2xl overflow-hidden transition-all duration-300"
              >
                <button 
                  onClick={() => setOpenIdx(isOpen ? null : idx)}
                  className="w-full flex items-center justify-between p-6 text-left hover:bg-white/5 transition-colors"
                >
                  <span className="font-medium text-lg pr-8">{faq.q}</span>
                  <span className="flex-shrink-0 text-white/50">
                    {isOpen ? <Minus size={20} /> : <Plus size={20} />}
                  </span>
                </button>
                <div 
                  className={`px-6 overflow-hidden transition-all duration-500 ease-in-out ${isOpen ? 'max-h-40 pb-6 opacity-100' : 'max-h-0 opacity-0'}`}
                >
                  <p className="text-white/60 leading-relaxed">
                    {faq.a}
                  </p>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
