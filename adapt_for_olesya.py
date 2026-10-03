import re

# 1. Update App.tsx
with open('src/App.tsx', 'r') as f:
    app_code = f.read()

# Replace video src
app_code = re.sub(
    r'src="https://[^"]+"',
    'src="/olesya-bg.mp4"',
    app_code
)

# Replace Headline
app_code = app_code.replace(
    'Own your time <br />\n            without <em className="not-italic" style={{ fontFamily: "\'Instrument Serif\', serif", fontStyle: \'italic\' }}>the stress</em>',
    'Выйди из сценария <br />\n            без <em className="not-italic" style={{ fontFamily: "\'Instrument Serif\', serif", fontStyle: \'italic\' }}>надрыва</em>'
)

# Replace Subtitle
app_code = app_code.replace(
    'Drift is a calm, ADHD-friendly planner that turns scattered ideas into a clear path',
    'Закрытый канал Олеси Ланской. Практический метод, который перестроит ваши реакции и вернет контроль над жизнью.'
)

# Replace CTA texts
app_code = app_code.replace(
    'No noise. No complicated systems. Just your day, gently sorted.',
    'Без воды. Без марафонов. Только глубокий психологический разбор.'
)
app_code = app_code.replace(
    'No noise. Just your day, gently sorted.',
    'Без марафонов. Только суть.'
)
app_code = app_code.replace(
    'Start for free',
    'Вступить в канал'
)

with open('src/App.tsx', 'w') as f:
    f.write(app_code)


# 2. Update Navbar.tsx
with open('src/components/Navbar.tsx', 'r') as f:
    nav_code = f.read()
nav_code = nav_code.replace('Drift.', 'Lanskaya.')
nav_code = nav_code.replace('Features', 'Метод')
nav_code = nav_code.replace('Drift AI', 'Обо мне')
nav_code = nav_code.replace('FAQ', 'Отзывы')
with open('src/components/Navbar.tsx', 'w') as f:
    f.write(nav_code)


# 3. Update AboutSection.tsx
with open('src/components/AboutSection.tsx', 'r') as f:
    about_code = f.read()

about_code = about_code.replace(
    'We craft tools that move with your rhythm, not over it. Designed for ease, presence, and flow.',
    'Метод основан на 12 годах практики и разборе более 5000 сложных жизненных судеб.'
)
about_code = about_code.replace('Say hello', 'Купить доступ')
about_code = about_code.replace('Stay informed', 'Задать вопрос')
about_code = about_code.replace('Calm /\\nAmplified', 'Олеся /\\nЛанская')
about_code = about_code.replace(
    'We make AI tools and assistants. But, most importantly, we help you remember what gentle productivity looks like when software moves with you, not over you. We create systems that carry the cognitive weight, so you can attend to what truly counts.',
    'Я не даю волшебных таблеток и не обещаю, что вы станете счастливыми за три дня. Я даю холодный, отрезвляющий анализ ваших жизненных стратегий. Мы найдем вашу "слепую зону" и аккуратно перестроим ее, чтобы вы перестали наступать на одни и те же грабли.'
)
# Make text a bit smaller since Russian text is long
about_code = about_code.replace(
    'text-2xl sm:text-3xl md:text-4xl lg:text-[42px] leading-[1.3]',
    'text-xl sm:text-2xl md:text-3xl lg:text-[36px] leading-[1.4]'
)
with open('src/components/AboutSection.tsx', 'w') as f:
    f.write(about_code)


# 4. Update FeaturesSection.tsx
with open('src/components/FeaturesSection.tsx', 'r') as f:
    feat_code = f.read()

# Replace the data array completely
new_data = """const featuresData = [
  {
    id: "feature-1",
    title: "Разборы без купюр",
    description: "В канале вы услышите аудио-разборы реальных историй участниц. В 90% случаев вы узнаете в них себя. Это дает моментальный инсайт.",
    video: "/olesya-bg.mp4"
  },
  {
    id: "feature-2",
    title: "Перепрошивка мышления",
    description: "Психика не меняется за 3 дня марафона. Находясь в нашем поле регулярно, вы незаметно для себя меняете паттерны реакций и начинаете действовать иначе.",
    video: "/olesya-bg.mp4"
  },
  {
    id: "feature-3",
    title: "Полная безопасность",
    description: "Всё абсолютно анонимно. Ваши истории разбираются без имен. Никто из ваших знакомых никогда ничего не узнает, это приватное комьюнити.",
    video: "/olesya-bg.mp4"
  }
];"""
feat_code = re.sub(r'const featuresData = \[.*?\];', new_data, feat_code, flags=re.DOTALL)

# Replace titles and text
feat_code = feat_code.replace('Software that flows with your mind, not over it', 'Почему марафоны не работают, а метод — работает')
feat_code = feat_code.replace('No noise. No complicated systems. Just your day, gently sorted.', 'Подписка 1 190 ₽/мес. Отмена в любой момент.')
feat_code = feat_code.replace('Start for free', 'Оформить подписку')
feat_code = feat_code.replace('text-black', 'text-black') # Keep text black for button

# Replace fixed bg image to Olesya's background image (darkened)
feat_code = re.sub(
    r'backgroundImage: \'url\("https://[^"]+"\)\'',
    'backgroundImage: \'url("/bg.jpg")\'',
    feat_code
)

with open('src/components/FeaturesSection.tsx', 'w') as f:
    f.write(feat_code)

