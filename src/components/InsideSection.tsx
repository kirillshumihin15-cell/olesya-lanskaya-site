import { Mic, ShieldCheck, Zap, MessageSquare } from 'lucide-react';

const items = [
  {
    title: 'Аудио-сессии',
    subtitle: '10-15 минут',
    desc: 'Никаких двухчасовых вебинаров. Только концентрат пользы, который удобно слушать по дороге на работу или за рулем.',
    icon: <Mic size={24} className="text-white" />
  },
  {
    title: 'Анонимные разборы',
    subtitle: 'Реальные ситуации',
    desc: 'Разбираю ваши истории без имен и контактов. На чужих примерах свои слепые зоны видны ярче всего.',
    icon: <MessageSquare size={24} className="text-white" />
  },
  {
    title: 'Нейро-практики',
    subtitle: 'Каждый день',
    desc: 'Простые задания, которые физически перестраивают нейронные связи и меняют автоматические реакции.',
    icon: <Zap size={24} className="text-white" />
  },
  {
    title: 'Безопасное поле',
    subtitle: 'Без осуждения',
    desc: 'Закрытое комьюнити. Никто не лезет с непрошеными советами, только поддержка и фокус на изменениях.',
    icon: <ShieldCheck size={24} className="text-white" />
  }
];

export default function InsideSection() {
  return (
    <section id="inside" className="bg-[#050505] py-24 md:py-32 px-6 text-white border-t border-white/10 relative z-10">
      <div className="max-w-6xl mx-auto">
        <div className="mb-16 md:mb-20 text-center">
          <h2 className="text-3xl sm:text-4xl lg:text-[42px] leading-[1.2] font-normal mb-6">
            Что внутри канала?
          </h2>
          <p className="text-white/60 text-lg max-w-2xl mx-auto font-medium">
            Мы не продаем доступ к чату. Мы продаем выжимку инструментов, которые экономят годы классической терапии.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-6">
          {items.map((item, idx) => (
            <div 
              key={idx}
              className="bg-white/5 backdrop-blur-sm border border-white/10 rounded-3xl p-8 hover:bg-white/10 transition-colors flex flex-col md:flex-row gap-6 group"
            >
              <div className="w-14 h-14 rounded-2xl bg-white/10 flex flex-shrink-0 items-center justify-center group-hover:scale-110 transition-transform duration-500">
                {item.icon}
              </div>
              <div>
                <div className="text-[11px] uppercase tracking-widest text-white/40 font-bold mb-2">
                  {item.subtitle}
                </div>
                <h3 className="text-2xl font-semibold mb-3">
                  {item.title}
                </h3>
                <p className="text-white/60 leading-relaxed text-sm md:text-base">
                  {item.desc}
                </p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
