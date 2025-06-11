# tuplas.py

# Criando uma tupla com 4 elementos
nomes = ('Ana', 'Bia', 'Gui', 'Ana')  # Tupla imutável

# Verifica se o valor 'bia' está presente na tupla (case sensitive)
print('bia' in nomes)  # False, pois 'bia' (minúsculo) é diferente de 'Bia'

# Acessando elementos por índice
print(nomes[0])  # 'Ana'
print(nomes[1:3])  # ('Bia', 'Gui') -> fatiamento da posição 1 até antes da 3
print(nomes[:1])  # ('Ana',) -> do início até antes da posição 1

# Verificando o tipo do objeto
print(type(nomes))  # <class 'tuple'>

# Exibindo a tupla completa
print(nomes)  # ('Ana', 'Bia', 'Gui', 'Ana')
