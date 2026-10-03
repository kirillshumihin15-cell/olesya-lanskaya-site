import { useEffect, useRef, useState } from 'react';

const featuresData = [
  {
    id: "feature-1",
    title: "Разборы без купюр",
    description: "В канале вы услышите аудио-разборы реальных историй участниц. В 90% случаев вы узнаете в них себя. Это дает моментальный инсайт.",
    video: "./card1.mp4"
  },
  {
    id: "feature-2",
    title: "Перепрошивка мышления",
    description: "Психика не меняется за 3 дня марафона. Находясь в нашем поле регулярно, вы незаметно для себя меняете паттерны реакций и начинаете действовать иначе.",
    video: "./card2.mp4"
  },
  {
    id: "feature-3",
    title: "Полная безопасность",
    description: "Всё абсолютно анонимно. Ваши истории разбираются без имен. Никто из ваших знакомых никогда ничего не узнает, это приватное комьюнити.",
    video: "./card3.mp4"
  }
];

export default function FeaturesSection() {
  const [activeFeature, setActiveFeature] = useState(featuresData[0].id);
  const cardRefs = useRef<(HTMLDivElement | null)[]>([]);

  useEffect(() => {
    // Observer for active nav state
    const observerActive = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          setActiveFeature(entry.target.id);
        }
      });
    }, { threshold: 0.6, rootMargin: '-20% 0px -20% 0px' });

    // Observer for reveal animation
    const observerReveal = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.remove('opacity-0', 'translate-x-16');
          entry.target.classList.add('opacity-100', 'translate-x-0');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    cardRefs.current.forEach(card => {
      if (card) {
        observerActive.observe(card);
        observerReveal.observe(card);
      }
    });

    return () => {
      observerActive.disconnect();
      observerReveal.disconnect();
    };
  }, []);

  const scrollToFeature = (id: string) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  };

  return (
    <section id="method" className="relative min-h-screen z-0 px-5 md:px-10 lg:px-16 py-20 md:py-40 lg:py-48 text-white">
      {/* Fixed video background */}
      <div 
        className="fixed inset-0 w-full h-full -z-20"
        dangerouslySetInnerHTML={{
          __html: `
            <video
              autoplay
              loop
              muted
              playsinline
              class="w-full h-full object-cover"
              style="pointer-events: none;"
            >
              <source src="./features-bg.mp4" type="video/mp4" />
            </video>
          `
        }}
      />
      {/* Dark overlay for readability */}
      <div className="fixed inset-0 bg-black/60 -z-10" />

      <div className="max-w-[1440px] mx-auto lg:grid lg:grid-cols-[400px_1fr] xl:grid-cols-[460px_1fr] gap-24 xl:gap-48 items-start">
        
        {/* Left Column (Sticky on desktop) */}
        <div className="lg:sticky lg:top-0 lg:h-screen lg:flex lg:flex-col lg:justify-center lg:py-32 mb-16 lg:mb-0">
          <div className="lg:flex-1 lg:flex lg:flex-col lg:justify-center">
            <h2 className="text-2xl sm:text-3xl lg:text-[46px] leading-[1.2] font-normal text-white mb-6">
              Почему марафоны не работают, а метод — работает
            </h2>
            <p className="text-white/70 text-base leading-relaxed mb-12 max-w-md">
              В основе метода лежит интегративный подход. Мы не просто "визуализируем успех", мы работаем с нейронными связями, находим корневые установки и бережно их переписываем через аудио-сессии и рефлексию.
            </p>
            
            <div className="hidden lg:flex flex-col items-start gap-3">
              {featuresData.map(f => (
                <button
                  key={f.id}
                  onClick={() => scrollToFeature(f.id)}
                  className={`text-left px-5 py-3 rounded-xl text-base font-medium transition-all duration-300 ${activeFeature === f.id ? 'bg-black/20 text-white' : 'bg-black/0 text-white/40 hover:text-white/60'}`}
                >
                  {f.title}
                </button>
              ))}
            </div>
          </div>
          
          <div className="hidden lg:flex flex-col items-start mt-auto">
            <div className="bg-black/25 backdrop-blur-md rounded-xl flex flex-row items-center pl-6 pr-1 py-1 gap-6">
              <span className="text-white text-sm font-medium">
                Подписка 1 190 ₽/мес. Отмена в любой момент.
              </span>
              <button onClick={() => window.location.href="https://web.tribute.tg/s/16WO"} className="bg-white text-black text-sm font-medium px-5 py-2.5 rounded-xl hover:bg-white/90 transition-colors whitespace-nowrap">
                Оформить подписку
              </button>
            </div>
          </div>
        </div>

        {/* Right Column (Scrolling Cards) */}
        <div className="flex flex-col gap-12 lg:gap-32 lg:py-32">
          {featuresData.map((f, idx) => (
            <div 
              key={f.id}
              id={f.id}
              ref={el => { cardRefs.current[idx] = el; }}
              className="bg-black/20 backdrop-blur-sm rounded-3xl p-6 md:p-10 opacity-0 translate-x-16 transition-all duration-700 ease-out flex flex-col gap-6"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 256 256" fill="none">
                <path d="M 256 256 L 178 256 C 150.386 256 128 233.614 128 206 L 128 256 L 0 256 L 0 192 C 0 156.654 28.654 128 64 128 C 99.346 128 128 156.654 128 192 L 128 128 L 256 128 Z M 78 0 C 105.614 0 128 22.386 128 50 L 128 0 L 256 0 L 256 64 C 256 99.346 227.346 128 192 128 C 156.654 128 128 99.346 128 64 L 128 128 L 0 128 L 0 0 Z" fill="rgba(255,255,255,0.8)" />
              </svg>
              <h3 className="text-white text-xl md:text-2xl font-medium">{f.title}</h3>
              <div className="aspect-video w-full rounded-2xl overflow-hidden bg-black/30 relative">
                <video 
                  onCanPlay={(e) => e.currentTarget.play().catch(() => {})} 
                   
                  autoPlay 
                  muted 
                  loop 
                  playsInline 
                  className="absolute inset-0 w-full h-full object-cover object-[50%_20%]"
                  src={f.video}
                />
              </div>
              <p className="text-white/60 font-medium text-sm md:text-base leading-relaxed">
                {f.description}
              </p>
            </div>
          ))}
        </div>

      </div>
    </section>
  );
}
