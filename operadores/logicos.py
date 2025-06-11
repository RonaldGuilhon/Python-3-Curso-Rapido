# Variáveis booleanas
b1 = True
b2 = False
b3 = True

# Operadores lógicos:

print(b1 and b2 and b3)  # False → AND só é True se todos forem True
print(b1 or b2 or b3)    # True  → OR é True se ao menos um for True
print(b1 != b2)          # True  → diferente → equivale a XOR em alguns contextos
print(not b1)            # False → inverte True para False
print(not b2)            # True  → inverte False para True
print(b1 and not b2 and b3)  # True → todos são True após aplicar NOT em b2

# Avaliação de expressões com comparação e booleanos
x = 3
y = 4

print(b1 and not b2 and x < y)  # True → b1=True, not b2=True, x<y=True → tudo True
