import re

with open('src/components/FeaturesSection.tsx', 'r') as f:
    code = f.read()

# Make the portrait video container have a reasonable max-width so it's not giant on desktop
code = code.replace(
    'className="aspect-[9/16] w-full max-w-[360px] mx-auto sm:max-w-none sm:w-full rounded-2xl overflow-hidden bg-black/30 relative"',
    'className="aspect-[9/16] w-full max-w-sm rounded-2xl overflow-hidden bg-black/30 relative"'
)

with open('src/components/FeaturesSection.tsx', 'w') as f:
    f.write(code)
