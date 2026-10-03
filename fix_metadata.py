import re

with open('index.html', 'r') as f:
    html = f.read()

# Replace title
html = re.sub(r'<title>.*?</title>', '<title>Закрытый канал Олеси Ланской | Психология</title>', html)

# Add meta description and OpenGraph for Telegram/WhatsApp sharing
meta_tags = """
    <meta name="description" content="Практический метод, который перестроит ваши реакции и вернет контроль над жизнью. Без марафонов, только глубокий психологический разбор." />
    <meta property="og:title" content="Закрытый канал Олеси Ланской" />
    <meta property="og:description" content="Практический метод, который перестроит ваши реакции. Выйди из сценария без надрыва." />
    <meta property="og:type" content="website" />
"""

if 'name="description"' not in html:
    html = html.replace('</head>', meta_tags + '</head>')

with open('index.html', 'w') as f:
    f.write(html)
