# 1. Update App.tsx to redirect to quiz if not completed
with open('src/App.tsx', 'r') as f:
    app = f.read()

quiz_redirect = """import { useEffect } from 'react';

"""

# Add redirect logic at top of App component
app = app.replace(
    "function App() {",
    """function App() {
  useEffect(() => {
    const quizDone = localStorage.getItem('quizCompleted');
    if (!quizDone) {
      window.location.href = './quiz.html';
    }
  }, []);
"""
)

with open('src/App.tsx', 'w') as f:
    f.write(app)

# 2. Update quiz.html to set localStorage flag before redirect
with open('public/quiz.html', 'r') as f:
    quiz = f.read()

quiz = quiz.replace(
    "window.location.href = './';",
    "localStorage.setItem('quizCompleted', 'true'); window.location.href = './';"
)

with open('public/quiz.html', 'w') as f:
    f.write(quiz)

print("Done!")
