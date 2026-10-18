import re

with open('/Users/znoirewgmail.com/Desktop/valter_source.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Diana Valter references with Olesya Lanskaya
html = html.replace('Диана Вальтер', 'Олеся Ланская')
html = html.replace('Вальтер Диана', 'Олеся Ланская')
html = html.replace('/opora14/diana-avatar.jpg', './opora/olesya-avatar.jpg')
html = html.replace('/opora14/diana.jpg', './opora/olesya-author.jpg')
html = html.replace('/opora14/hero.jpg', './opora/hero.jpg')
html = html.replace('/opora14/opora-book.jpg', './opora/opora-book.jpg')

# Update Author role to Olesya's persona
html = html.replace(
    'Психолог. Работает с устойчивостью, реализацией и отношениями с деньгами',
    'Психолог. 12 лет практики. Автор системы восстановления устойчивости и выхода из эмоциональных сценариев'
)

# Update prices: 990 rubles instead of 1190 rubles, 67% discount instead of 60%
html = html.replace('1190', '990')
html = html.replace('Скидка 60%', 'Скидка 67%')

# Update support email and links
html = html.replace('support@valterpsy.ru', 'support@lanskaya.pro')
html = html.replace('https://valterpsy.ru/oferta.html', '#oferta')
html = html.replace('https://valterpsy.ru/privacy.html', '#privacy')
html = html.replace('https://valterpsy.ru/support.html', '#support')
html = html.replace('https://payform.ru/racyreZ/', '#pay')

# Set default payUrl in config
html = html.replace("payUrl:  'https://payform.ru/racyreZ/'", "payUrl:  '#'")
html = html.replace("brand:   'Диана Вальтер'", "brand:   'Олеся Ланская'")

# Update title
html = html.replace('<title>Тест на жизненные схемы</title>', '<title>Тест на жизненные схемы | Олеся Ланская</title>')

with open('/Users/znoirewgmail.com/Desktop/drift-landing/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully generated index.html for Olesya Lanskaya!")
