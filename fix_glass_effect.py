import re

# 1. Update App.tsx to use a sticky background for the Hero + About sections
with open('src/App.tsx', 'r') as f:
    app = f.read()

# We need to extract the HeroVideo component (which is fine) and modify the App component layout.
new_app = """
function App() {
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
                <source src="/olesya-bg.mp4" type="video/mp4" />
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
            <button onClick={() => window.location.href="https://web.tribute.tg/s/16WO"} className="bg-white text-black text-sm font-medium px-5 py-2.5 rounded-xl hover:bg-white/90 transition-colors whitespace-nowrap">
              Вступить в канал
            </button>
          </div>
        </section>

        <AboutSection />
      </div>

      <FeaturesSection />
      <ReviewsSection />
      <CookieBanner />
    </div>
  );
}
"""

# Replace the whole App function
app = re.sub(r'function App\(\) \{.*', new_app.strip(), app, flags=re.DOTALL)
with open('src/App.tsx', 'w') as f:
    f.write(app)


# 2. Update AboutSection.tsx for Glassmorphism
with open('src/components/AboutSection.tsx', 'r') as f:
    about = f.read()

# Background and overall style
about = about.replace('bg-[#F6E4CF]', 'bg-white/10 backdrop-blur-2xl border-t border-white/20')
# Texts
about = about.replace('text-[#321C04]', 'text-white')
# Divider
about = about.replace('bg-[#D9C4AA]', 'bg-white/20')
# Buttons
about = about.replace(
    'bg-[#321C04] text-[#FFF9F2] rounded-full flex items-center pr-6 pl-1.5 py-1.5 hover:bg-[#1F1003] transition-colors group',
    'bg-white text-black rounded-full flex items-center pr-6 pl-1.5 py-1.5 hover:bg-white/90 transition-colors group'
)
about = about.replace(
    'bg-[#D9C4AA] text-[#321C04] rounded-full flex items-center pr-6 pl-1.5 py-1.5 hover:bg-[#CEBA9E] transition-colors group',
    'bg-white/10 text-white border border-white/20 rounded-full flex items-center pr-6 pl-1.5 py-1.5 hover:bg-white/20 transition-colors group'
)
# Button Icons
about = about.replace(
    '<div className="w-8 h-8 rounded-full bg-white flex items-center justify-center mr-3 text-[#321C04]">',
    '<div className="w-8 h-8 rounded-full bg-black/10 flex items-center justify-center mr-3 text-current">'
)
# SVG Logo
about = about.replace('fill="#321C04"', 'fill="white"')

with open('src/components/AboutSection.tsx', 'w') as f:
    f.write(about)
