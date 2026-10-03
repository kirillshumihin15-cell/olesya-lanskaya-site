import { useEffect } from 'react';
import Navbar from './components/Navbar';
import AboutSection from './components/AboutSection';
import FeaturesSection from './components/FeaturesSection';
import InsideSection from './components/InsideSection';
import ReviewsSection from './components/ReviewsSection';
import CookieBanner from './components/CookieBanner';
import FAQSection from './components/FAQSection';
import Footer from './components/Footer';

function App() {
  useEffect(() => {
    const quizDone = localStorage.getItem('quizCompleted');
    if (!quizDone) {
      window.location.href = './quiz.html';
    }
  }, []);

  return (
    <div className="relative w-full bg-black">
      {/* Sticky Hero Video Background */}
      <div className="sticky top-0 w-full h-screen overflow-hidden">
        <div 
          className="absolute inset-0 w-full h-full"
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
                <source src="./olesya-bg.mp4" type="video/mp4" />
              </video>
            `
          }}
        />
        <div className="absolute inset-0 bg-black/20 pointer-events-none" />
      </div>

      {/* Scrolling Content over the video */}
      <div className="relative -mt-[100vh] z-10 flex flex-col">
        <Navbar />

        <section className="h-screen w-full flex flex-col justify-end pb-12 md:pb-16 px-4 pointer-events-none">
          <h1 className="text-center text-white text-5xl sm:text-7xl md:text-8xl lg:text-[96px] font-normal leading-[1.1] tracking-tight mb-4">
            Выйди из сценария <br />
            без <em className="not-italic" style={{ fontFamily: "'Instrument Serif', serif", fontStyle: 'italic' }}>надрыва</em>
          </h1>
          <p className="text-white/80 text-sm md:text-base font-medium max-w-[420px] mx-auto text-center mb-8">
            Закрытый канал Олеси Ланской. Практический метод, который перестроит ваши реакции и вернет контроль над жизнью.
          </p>
          
          <div className="mx-auto bg-black/40 backdrop-blur-md border border-white/10 rounded-xl flex flex-row items-center pl-6 pr-1 py-1 gap-6 pointer-events-auto">
            <span className="text-white text-sm font-medium hidden md:block">
              Без воды. Без марафонов. Только глубокий психологический разбор.
            </span>
            <span className="text-white text-sm font-medium block md:hidden">
              Без марафонов. Только суть.
            </span>
            <button onClick={() => window.location.href="https://web.tribute.tg/s/17h5"} className="bg-white text-black text-sm font-medium px-5 py-2.5 rounded-xl hover:bg-white/90 transition-colors whitespace-nowrap">
              Вступить в канал
            </button>
          </div>
        </section>

        <AboutSection />
      </div>

      <FeaturesSection />
      <InsideSection />
      <ReviewsSection />
      <FAQSection />
      <Footer />
      <CookieBanner />
    </div>
  );
}
export default App;
