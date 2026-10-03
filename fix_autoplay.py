import re

with open('src/App.tsx', 'r') as f:
    app_code = f.read()

# Add imports if not present
if "useRef" not in app_code:
    app_code = "import { useEffect, useRef } from 'react';\n" + app_code

# Add ref inside App component
ref_logic = """
function App() {
  const videoRef = useRef<HTMLVideoElement>(null);
  
  useEffect(() => {
    if (videoRef.current) {
      videoRef.current.play().catch(console.error);
    }
  }, []);
"""
app_code = app_code.replace("function App() {", ref_logic)

# Add ref to video tag
app_code = app_code.replace(
    '<video',
    '<video ref={videoRef} defaultMuted={true}'
)

with open('src/App.tsx', 'w') as f:
    f.write(app_code)


with open('src/components/FeaturesSection.tsx', 'r') as f:
    feat_code = f.read()

# The videos in FeaturesSection are mapped. We can use a trick: onLoadedMetadata to play.
feat_code = feat_code.replace(
    '<video \n                  autoPlay',
    '<video \n                  onCanPlay={(e) => e.currentTarget.play().catch(() => {})} \n                  defaultMuted={true} \n                  autoPlay'
)

with open('src/components/FeaturesSection.tsx', 'w') as f:
    f.write(feat_code)
