import re

with open('src/components/FeaturesSection.tsx', 'r') as f:
    code = f.read()

bg_div = """      {/* Fixed background image */}
      <div 
        className="fixed inset-0 w-full h-full object-cover -z-10 bg-black"
        style={{
          backgroundImage: 'url("/bg.jpg")',
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          backgroundRepeat: 'no-repeat'
        }}
      />
      {/* Overlay to ensure text readability if needed */}
      <div className="fixed inset-0 bg-black/40 -z-10" />"""

# We'll just replace it with a plain black background
new_bg = """      {/* Fixed background */}
      <div className="fixed inset-0 w-full h-full -z-10 bg-[#0a0a0a]" />"""

code = code.replace(bg_div, new_bg)

with open('src/components/FeaturesSection.tsx', 'w') as f:
    f.write(code)
