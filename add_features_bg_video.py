import re

with open('src/components/FeaturesSection.tsx', 'r') as f:
    code = f.read()

old_bg = """      {/* Fixed background */}
      <div className="fixed inset-0 w-full h-full -z-10 bg-[#0a0a0a]" />"""

new_bg = """      {/* Fixed video background */}
      <div 
        className="fixed inset-0 w-full h-full -z-20"
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
              <source src="/features-bg.mp4" type="video/mp4" />
            </video>
          `
        }}
      />
      {/* Dark overlay for readability */}
      <div className="fixed inset-0 bg-black/60 -z-10" />"""

code = code.replace(old_bg, new_bg)

with open('src/components/FeaturesSection.tsx', 'w') as f:
    f.write(code)
