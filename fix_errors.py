with open('index.html', encoding='utf-8') as f:
    c = f.read()

c = c.replace('CATALOG O INDUSTRIAL 2026', 'CATALOGO INDUSTRIAL 2026')
c = c.replace('<tr style=""><td', '<tr><td')

with open('index.html', 'w', encoding='utf-8', newline='\n') as f:
    f.write(c)

print('Feito')
print('CATALOG O restantes:', c.count('CATALOG O'))
print('tr style vazios restantes:', c.count('<tr style=""><td'))
