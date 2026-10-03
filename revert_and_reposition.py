import re

with open('src/components/FeaturesSection.tsx', 'r') as f:
    code = f.read()

# Revert to horizontal
code = code.replace(
    'className="aspect-[9/16] w-full max-w-sm rounded-2xl overflow-hidden bg-black/30 relative"',
    'className="aspect-video w-full rounded-2xl overflow-hidden bg-black/30 relative"'
)

# Apply specific vertical cropping (focus on the top 20% where the face is)
code = code.replace(
    'className="absolute inset-0 w-full h-full object-cover"',
    'className="absolute inset-0 w-full h-full object-cover object-[50%_20%]"'
)

with open('src/components/FeaturesSection.tsx', 'w') as f:
    f.write(code)
