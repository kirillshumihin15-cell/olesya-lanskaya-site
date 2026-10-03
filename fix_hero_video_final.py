import re

with open('src/App.tsx', 'r') as f:
    app_code = f.read()

hero_component = """
import { useEffect, useRef } from 'react';

function HeroVideo() {
  const videoRef = useRef<HTMLVideoElement>(null);
  useEffect(() => {
    const v = videoRef.current;
    if (v) {
      v.muted = true;
      v.defaultMuted = true;
      v.play().catch(() => {
        const playOnInteract = () => {
          v.play().catch(() => {});
          window.removeEventListener('click', playOnInteract);
          window.removeEventListener('scroll', playOnInteract);
          window.removeEventListener('touchstart', playOnInteract);
        };
        window.addEventListener('click', playOnInteract);
        window.addEventListener('scroll', playOnInteract);
        window.addEventListener('touchstart', playOnInteract);
      });
    }
  }, []);
  return (
    <video 
      ref={videoRef} 
      autoPlay 
      loop 
      muted 
      playsInline 
      className="absolute inset-0 w-full h-full object-cover"
    >
      <source src="/olesya-bg-hero.mp4" type="video/mp4" />
    </video>
  );
}
"""

# Insert the component before App()
if "function HeroVideo" not in app_code:
    app_code = app_code.replace("function App() {", hero_component + "\nfunction App() {")

# Replace the dangerouslySetInnerHTML block with <HeroVideo />
app_code = re.sub(
    r'<div\s+className="absolute inset-0 w-full h-full"\s+dangerouslySetInnerHTML=\{\{\s*__html: `.*?`\s*\}\}\s*/>',
    '<HeroVideo />',
    app_code,
    flags=re.DOTALL
)

with open('src/App.tsx', 'w') as f:
    f.write(app_code)
