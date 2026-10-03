import re

# 1. Update App.tsx (Hero video)
with open('src/App.tsx', 'r') as f:
    app_code = f.read()
# Replace object-cover with object-cover object-[50%_20%] (horizontally centered, vertically slightly top-aligned)
app_code = app_code.replace('object-cover"', 'object-cover object-top md:object-center"')
with open('src/App.tsx', 'w') as f:
    f.write(app_code)

# 2. Update FeaturesSection.tsx (Cards videos)
with open('src/components/FeaturesSection.tsx', 'r') as f:
    feat_code = f.read()
feat_code = feat_code.replace('object-cover"', 'object-cover object-top md:object-center"')
with open('src/components/FeaturesSection.tsx', 'w') as f:
    f.write(feat_code)
