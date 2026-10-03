with open('src/components/AboutSection.tsx', 'r') as f:
    about = f.read()

# Fix the Mail icon container for "Купить доступ" (make icon text black)
about = about.replace('<div className="w-8 h-8 rounded-full bg-white flex items-center justify-center mr-3 text-white">', 
                      '<div className="w-8 h-8 rounded-full bg-black flex items-center justify-center mr-3 text-white">')

# Fix the "Задать вопрос" button
old_btn = """<button className="bg-white/20 text-white rounded-full flex items-center pr-6 pl-1.5 py-1.5 hover:bg-[#CEBA9E] transition-colors group">
            <div className="w-8 h-8 rounded-full bg-white flex items-center justify-center mr-3 text-white">
              <Plus size={16} />
            </div>
            <span className="uppercase tracking-wide text-xs font-medium">Задать вопрос</span>
          </button>"""

new_btn = """<button onClick={() => window.open('https://t.me/LanskayaO1esy', '_blank')} className="bg-white/10 text-white rounded-full flex items-center pr-6 pl-1.5 py-1.5 hover:bg-white/20 border border-white/20 transition-colors group">
            <div className="w-8 h-8 rounded-full bg-white flex items-center justify-center mr-3 text-black">
              <Plus size={16} />
            </div>
            <span className="uppercase tracking-wide text-xs font-medium">Задать вопрос</span>
          </button>"""

about = about.replace(old_btn, new_btn)

with open('src/components/AboutSection.tsx', 'w') as f:
    f.write(about)

# 2. Fix Footer.tsx
with open('src/components/Footer.tsx', 'r') as f:
    footer = f.read()

footer = footer.replace('href="https://t.me/lanskaya_support"', 'href="https://t.me/LanskayaO1esy"')
footer = footer.replace('@lanskaya_support', '@LanskayaO1esy')

with open('src/components/Footer.tsx', 'w') as f:
    f.write(footer)
