

pessoas = ['Gui', 'Rebeca']

adj = ['Sapeca', 'Inteligente']

for p in pessoas:
    for a in adj:
        print(f'{p} é {a}')
        
for i in [1, 2, 3]:
    pass

for i in range(1, 10):
    if i % 2:
        continue
    print(i, end=' ')

for i in range(1, 10):
    if i == 5:
        break
    print(i, end=' ')
    
print('\nFim')
# for i in range(1, 10):