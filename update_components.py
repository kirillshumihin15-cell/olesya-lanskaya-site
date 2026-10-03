import re

# 1. Navbar.tsx
with open('src/components/Navbar.tsx', 'r') as f:
    nav = f.read()
nav = nav.replace('href="#"', 'href="#method"', 1)
nav = nav.replace('href="#"', 'href="#about"', 1)
nav = nav.replace('href="#"', 'href="#reviews"', 1)
with open('src/components/Navbar.tsx', 'w') as f:
    f.write(nav)


# 2. AboutSection.tsx
with open('src/components/AboutSection.tsx', 'r') as f:
    about = f.read()
about = about.replace('<section className="', '<section id="about" className="')
with open('src/components/AboutSection.tsx', 'w') as f:
    f.write(about)


# 3. FeaturesSection.tsx
with open('src/components/FeaturesSection.tsx', 'r') as f:
    feat = f.read()
feat = feat.replace('<section className="', '<section id="method" className="')
# Expand method description
old_h2 = '<h2 className="text-2xl sm:text-3xl lg:text-[46px] leading-[1.2] font-normal text-white mb-12">\n              Почему марафоны не работают, а метод — работает\n            </h2>'
new_h2 = """<h2 className="text-2xl sm:text-3xl lg:text-[46px] leading-[1.2] font-normal text-white mb-6">
              Почему марафоны не работают, а метод — работает
            </h2>
            <p className="text-white/70 text-base leading-relaxed mb-12 max-w-md">
              В основе метода лежит интегративный подход. Мы не просто "визуализируем успех", мы работаем с нейронными связями, находим корневые установки и бережно их переписываем через аудио-сессии и рефлексию.
            </p>"""
feat = feat.replace(old_h2, new_h2)
with open('src/components/FeaturesSection.tsx', 'w') as f:
    f.write(feat)


# 4. App.tsx
with open('src/App.tsx', 'r') as f:
    app = f.read()

# Add imports
imports = """import Navbar from './components/Navbar';
import AboutSection from './components/AboutSection';
import FeaturesSection from './components/FeaturesSection';
import ReviewsSection from './components/ReviewsSection';
import CookieBanner from './components/CookieBanner';"""

app = re.sub(
    r'import Navbar.*FeaturesSection\';',
    imports,
    app,
    flags=re.DOTALL
)

# Add components
components = """
      <AboutSection />
      <FeaturesSection />
      <ReviewsSection />
      <CookieBanner />
    </div>
"""
app = re.sub(
    r'      <AboutSection />\s*<FeaturesSection />\s*</div>',
    components,
    app
)

with open('src/App.tsx', 'w') as f:
    f.write(app)
