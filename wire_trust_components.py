import re

# 1. Navbar.tsx
with open('src/components/Navbar.tsx', 'r') as f:
    nav = f.read()

# Add FAQ link to Navbar
faq_link = '<a href="#faq" className="px-6 py-3 text-black text-sm font-medium hover:bg-gray-50 transition-colors">FAQ</a>'
nav = nav.replace('href="#reviews" className="px-6 py-3 text-black text-sm font-medium hover:bg-gray-50 transition-colors"', 'href="#reviews" className="px-6 py-3 text-black text-sm font-medium hover:bg-gray-50 transition-colors border-b border-gray-100"')
nav = nav.replace('href="#reviews" className="px-6 py-3 text-black text-sm font-medium hover:bg-gray-50 transition-colors border-b border-gray-100">Отзывы</a>', 'href="#reviews" className="px-6 py-3 text-black text-sm font-medium hover:bg-gray-50 transition-colors border-b border-gray-100">Отзывы</a>\n              ' + faq_link)

with open('src/components/Navbar.tsx', 'w') as f:
    f.write(nav)


# 2. App.tsx
with open('src/App.tsx', 'r') as f:
    app = f.read()

# Add imports
app = app.replace("import CookieBanner from './components/CookieBanner';", "import CookieBanner from './components/CookieBanner';\nimport FAQSection from './components/FAQSection';\nimport Footer from './components/Footer';")

# Add components
app = app.replace("<ReviewsSection />\n      <CookieBanner />", "<ReviewsSection />\n      <FAQSection />\n      <Footer />\n      <CookieBanner />")

with open('src/App.tsx', 'w') as f:
    f.write(app)
