import os

files_to_patch = [
    'src/App.tsx',
    'src/components/FeaturesSection.tsx',
    'public/quiz.html'
]

for filepath in files_to_patch:
    with open(filepath, 'r') as f:
        content = f.read()
    
    content = content.replace('src="/olesya-bg', 'src="./olesya-bg')
    content = content.replace('src="/features-bg', 'src="./features-bg')
    content = content.replace('video: "/card', 'video: "./card')
    content = content.replace('src="/about.jpg', 'src="./about.jpg')
    
    with open(filepath, 'w') as f:
        f.write(content)
