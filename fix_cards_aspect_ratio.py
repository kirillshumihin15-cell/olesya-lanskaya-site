import re

with open('src/components/FeaturesSection.tsx', 'r') as f:
    code = f.read()

# Change aspect-video to aspect-[9/16] to accommodate portrait videos
code = code.replace(
    'className="aspect-video w-full rounded-2xl overflow-hidden bg-black/30 relative"',
    'className="aspect-[9/16] w-full max-w-[360px] mx-auto sm:max-w-none sm:w-full rounded-2xl overflow-hidden bg-black/30 relative"'
)

# And reset object position so it just fits nicely (object-cover on 9:16 container with 9:16 video won't crop at all)
code = code.replace(
    'className="absolute inset-0 w-full h-full object-cover object-top md:object-center"',
    'className="absolute inset-0 w-full h-full object-cover"'
)

with open('src/components/FeaturesSection.tsx', 'w') as f:
    f.write(code)
