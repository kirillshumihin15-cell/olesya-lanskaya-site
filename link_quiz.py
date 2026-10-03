import re

with open('public/quiz.html', 'r') as f:
    html = f.read()

# Replace the entire sell block with a redirect to the React landing page
sell_block_pattern = r'else if \(step\.kind === "sell"\) \{.*?(?=^\s*else if|^\s*\}$)'
# Wait, regex dotall might be tricky here. Let's just use simple text replacement of a known chunk.

# I'll just find the exact string that starts the sell block and replace the inside.
old_sell = """            else if (step.kind === "sell") {
                html = `
                    <div class="w-full flex flex-col h-full pt-2 pb-10 text-left">
                        
                        <!-- БЛОК 1: Оффер -->
                        <div class="text-center mb-10">"""

new_sell = """            else if (step.kind === "sell") {
                window.location.href = '/';
                return;
                html = `
                    <div class="w-full flex flex-col h-full pt-2 pb-10 text-left">
                        
                        <!-- БЛОК 1: Оффер -->
                        <div class="text-center mb-10">"""

html = html.replace(old_sell, new_sell)

# Also fix the image path just in case: <img src="about.jpg" -> <img src="/about.jpg"
html = html.replace('src="about.jpg"', 'src="/about.jpg"')

with open('public/quiz.html', 'w') as f:
    f.write(html)
