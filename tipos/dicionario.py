# dicionario.py

# ------------------------------
# DICIONÁRIOS EM PYTHON (dict)
# ------------------------------
# Dicionários são coleções de pares chave-valor.
# São mutáveis, não ordenados (até o Python 3.6) e não aceitam chaves duplicadas.

# Criando um dicionário
aluno = {
    'nome': 'João',
    'idade': 20,
    'curso': 'Ciência da Computação',
    'nota': 9.2,
    'ativo': True
}

# Verificando o tipo
print(type(aluno))  # <class 'dict'>

# Acessando valores por chave
print(aluno['nome'])   # João
print(aluno['nota'])   # 9.2
print(aluno['ativo'])  # True

# Tamanho do dicionário (número de pares chave-valor)
print(len(aluno))  # 5

# ------------------------------
# MÉTODOS ÚTEIS
# ------------------------------

# Adicionar ou modificar um valor
aluno['nota'] = 9.8
aluno['email'] = 'joao@email.com'
print(aluno)

# Remover item com del
del aluno['email']
print(aluno)

# Método .get() — evita erro caso a chave não exista
print(aluno.get('matricula'))  # None
print(aluno.get('nome', 'Sem nome'))  # João

# .keys(), .values(), .items()
print(aluno.keys())    # dict_keys(['nome', 'idade', 'curso', 'nota', 'ativo'])
print(aluno.values())  # dict_values(['João', 20, 'Ciência da Computação', 9.8, True])
print(aluno.items())   # dict_items([('nome', 'João'), ('idade', 20), ...])

# ------------------------------
# ITERANDO EM UM DICIONÁRIO
# ------------------------------

# Chaves
for chave in aluno:
    print(chave)

# Valores
for valor in aluno.values():
    print(valor)

# Chave e valor
for chave, valor in aluno.items():
    print(f'{chave}: {valor}')

# ------------------------------
# REMOÇÃO COM pop() e popitem()
# ------------------------------
nota = aluno.pop('nota')  # Remove e retorna o valor da chave 'nota'
print(nota)
print(aluno)

# popitem() remove o último item inserido (desde o Python 3.7)
ultimo = aluno.popitem()
print(ultimo)
print(aluno)

# ------------------------------
# DICIONÁRIOS ANINHADOS
# ------------------------------
turma = {
    'aluno1': {'nome': 'João', 'idade': 20},
    'aluno2': {'nome': 'Maria', 'idade': 21}
}
print(turma['aluno1']['nome'])  # João

# ------------------------------
# VERIFICANDO SE UMA CHAVE EXISTE
# ------------------------------
print('curso' in aluno)    # True
print('matricula' in aluno)  # False

# ------------------------------
# COPIANDO DICIONÁRIOS
# ------------------------------
copia = aluno.copy()
print(copia)

# ------------------------------
# LIMPAR DICIONÁRIO
# ------------------------------
copia.clear()
print(copia)  # {}

# ------------------------------
# COMPREENSÃO DE DICIONÁRIOS
# ------------------------------
quadrados = {x: x**2 for x in range(5)}
print(quadrados)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
