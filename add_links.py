import re

link = "https://web.tribute.tg/s/16WO"
onclick_attr = f'onClick={{() => window.location.href="{link}"}}'

# 1. App.tsx
with open('src/App.tsx', 'r') as f:
    code = f.read()
code = code.replace(
    '<button className="bg-white text-black text-sm font-medium px-5 py-2.5 rounded-xl hover:bg-white/90 transition-colors whitespace-nowrap">',
    f'<button {onclick_attr} className="bg-white text-black text-sm font-medium px-5 py-2.5 rounded-xl hover:bg-white/90 transition-colors whitespace-nowrap">'
)
with open('src/App.tsx', 'w') as f:
    f.write(code)

# 2. AboutSection.tsx
with open('src/components/AboutSection.tsx', 'r') as f:
    code = f.read()
code = code.replace(
    '<button className="bg-[#321C04] text-[#FFF9F2] rounded-full flex items-center pr-6 pl-1.5 py-1.5 hover:bg-[#1F1003] transition-colors group">',
    f'<button {onclick_attr} className="bg-[#321C04] text-[#FFF9F2] rounded-full flex items-center pr-6 pl-1.5 py-1.5 hover:bg-[#1F1003] transition-colors group">'
)
with open('src/components/AboutSection.tsx', 'w') as f:
    f.write(code)

# 3. FeaturesSection.tsx
with open('src/components/FeaturesSection.tsx', 'r') as f:
    code = f.read()
code = code.replace(
    '<button className="bg-white text-black text-sm font-medium px-5 py-2.5 rounded-xl hover:bg-white/90 transition-colors whitespace-nowrap text-black">',
    f'<button {onclick_attr} className="bg-white text-black text-sm font-medium px-5 py-2.5 rounded-xl hover:bg-white/90 transition-colors whitespace-nowrap">'
)
with open('src/components/FeaturesSection.tsx', 'w') as f:
    f.write(code)
