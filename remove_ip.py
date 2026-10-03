import re

with open('src/components/Footer.tsx', 'r') as f:
    footer = f.read()

# Remove the fake IP/INN/OGRN data
footer = footer.replace('<span>ИП Ланская О. В.</span>', '')
footer = footer.replace('<span>ИНН 123456789000</span>', '')
footer = footer.replace('<span>ОГРНИП 321123456789012</span>', '')

with open('src/components/Footer.tsx', 'w') as f:
    f.write(footer)
