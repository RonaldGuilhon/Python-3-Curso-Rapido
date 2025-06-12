# Loop de 0 até 9 (range com início implícito em 0)
for i in range(10):
    print(i , end=' ')
print(' ')  # Quebra de linha

# Loop de 1 até 99, pulando de 7 em 7
for i in range(1, 100, 7):
    print(i, end=' ')
print(' ')

# Contagem regressiva de 20 até 1, pulando de 3 em 3
for i in range(20, 0, -3):
    print(i, end=' ')
print(' ')

# Percorrendo uma lista
nums = [2, 4, 6, 8]
for n in nums:
    print(n, end=',')
print(' ')

# Iterando sobre os caracteres de uma string
texto = 'Python é muito massa!'
for letra in texto:
    print(letra, end=' ')
print(' ')

# Percorrendo um conjunto (valores únicos, ordem não garantida)
for n in {1, 2, 3, 4, 4, 4}:
    print(n, end=' ')
print(' ')

# Iterando sobre as chaves de um dicionário
produto = {
    'nome': 'Caneta',
    'preco': 7.99,
    'desconto': 0.5
}
for atrib in produto:
    print(atrib, '==>', produto[atrib], end=' ')
print(' ')

# Iterando com chave e valor (usando items())
for atrib, valor in produto.items():
    print(atrib, '=>', valor, end=' ')
print(' ')

# Iterando apenas os valores
for valor in produto.values():
    print(valor, end=' ')
print(' ')

# Iterando apenas as chaves
for chave in produto.keys():
    print(chave, end=' ')
print(' ')
