with open('src/App.tsx', 'r') as f:
    app = f.read()

app = app.replace("import FeaturesSection from './components/FeaturesSection';", 
                  "import FeaturesSection from './components/FeaturesSection';\nimport InsideSection from './components/InsideSection';")

app = app.replace("<FeaturesSection />\n      <ReviewsSection />", 
                  "<FeaturesSection />\n      <InsideSection />\n      <ReviewsSection />")

with open('src/App.tsx', 'w') as f:
    f.write(app)

with open('src/components/Navbar.tsx', 'r') as f:
    nav = f.read()

inside_link = '<a href="#inside" className="px-6 py-3 text-black text-sm font-medium hover:bg-gray-50 transition-colors border-b border-gray-100">Формат</a>'
nav = nav.replace('href="#faq" className="px-6 py-3 text-black text-sm font-medium hover:bg-gray-50 transition-colors"', 
                  'href="#faq" className="px-6 py-3 text-black text-sm font-medium hover:bg-gray-50 transition-colors border-b border-gray-100"')
nav = nav.replace('href="#faq" className="px-6 py-3 text-black text-sm font-medium hover:bg-gray-50 transition-colors border-b border-gray-100">FAQ</a>', 
                  'href="#faq" className="px-6 py-3 text-black text-sm font-medium hover:bg-gray-50 transition-colors border-b border-gray-100">FAQ</a>\n              ' + inside_link)

with open('src/components/Navbar.tsx', 'w') as f:
    f.write(nav)
