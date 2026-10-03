with open('public/quiz.html', 'r') as f:
    html = f.read()

html = html.replace("window.location.href = '/';", "window.location.href = './';")

with open('public/quiz.html', 'w') as f:
    f.write(html)
