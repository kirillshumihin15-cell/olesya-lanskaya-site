import re

with open('public/quiz.html', 'r') as f:
    html = f.read()

# CSS Fixes
html = html.replace('background-color: #F8F9FA;', 'background-color: #000000; background-image: radial-gradient(circle at 50% 0%, #1a1a1a 0%, #000 70%);')
html = html.replace('color: #111;', 'color: #ffffff;')

html = html.replace('background: #FFFFFF;', 'background: rgba(255,255,255,0.05); backdrop-filter: blur(10px);')
html = html.replace('border: 1px solid rgba(0,0,0,0.06);', 'border: 1px solid rgba(255,255,255,0.1);')
html = html.replace('color: #111;', 'color: #ffffff;') # btn-amie color

html = html.replace('border-color: rgba(0,0,0,0.12);', 'border-color: rgba(255,255,255,0.3);')
html = html.replace('box-shadow: 0 4px 12px rgba(0,0,0,0.02);', 'box-shadow: 0 4px 12px rgba(0,0,0,0.2);')
html = html.replace('box-shadow: 0 12px 24px rgba(0,0,0,0.06);', 'box-shadow: 0 12px 24px rgba(0,0,0,0.4);')

html = html.replace('background: #111; color: #fff;', 'background: #ffffff; color: #000000;')

# Container fixes
html = html.replace('background: #FFFFFF;', 'background: rgba(255,255,255,0.05); backdrop-filter: blur(16px);')
html = html.replace('box-shadow: 0 20px 60px rgba(0,0,0,0.08);', 'box-shadow: 0 20px 60px rgba(0,0,0,0.5);')

# Tailwind utility class fixes inside the JS script
html = html.replace('text-black', 'text-white')
html = html.replace('bg-white', 'bg-white/10')
html = html.replace('bg-gray-100', 'bg-white/5')
html = html.replace('bg-gray-50/80', 'bg-white/5')
html = html.replace('bg-gray-50', 'bg-white/5')
html = html.replace('border-black/5', 'border-white/10')
html = html.replace('border-black/10', 'border-white/20')

# Card gradient
html = html.replace('background: linear-gradient(180deg, #FFFFFF 0%, #F9F9F9 100%)', 'background: rgba(255,255,255,0.03)')

# We need to make sure the app container itself looks dark
# Currently it's `.card-amie`
html = html.replace('border: 1px solid rgba(0,0,0,0.04);', 'border: 1px solid rgba(255,255,255,0.1);')
html = html.replace('background: #FFFFFF;', 'background: rgba(20,20,20,0.6); backdrop-filter: blur(20px);')

with open('public/quiz.html', 'w') as f:
    f.write(html)
