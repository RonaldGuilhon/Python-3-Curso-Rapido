# conjunto.py

# ------------------------------
# CONJUNTOS (SETS) EM PYTHON
# ------------------------------
# Conjuntos são coleções não ordenadas, mutáveis e que não permitem elementos duplicados.

# Criando um conjunto com chaves {}
meu_conjunto = {1, 2, 3}
print(type(meu_conjunto))  # <class 'set'>
print(meu_conjunto)        # {1, 2, 3}

# Elementos duplicados são automaticamente removidos
conjunto_com_duplicatas = {1, 2, 3, 3, 3, 3}
print(conjunto_com_duplicatas)  # {1, 2, 3}
print(len(conjunto_com_duplicatas))  # 3 (elementos únicos)

# Também é possível criar conjuntos com a função set()
conjunto_via_set = set([1, 2, 2, 4, 5])
print(conjunto_via_set)  # {1, 2, 4, 5}

# Conjuntos não garantem ordem
conjunto = {10, 20, 30, 40}
print(conjunto)  # Pode aparecer em qualquer ordem

# ------------------------------
# MÉTODOS ÚTEIS DE CONJUNTOS
# ------------------------------

# Adicionando elementos
conjunto.add(50)
print(conjunto)  # {10, 20, 30, 40, 50}

# Removendo elementos (gera erro se não existir)
conjunto.remove(30)
print(conjunto)  # {10, 20, 40, 50}

# Removendo com descuido (NÃO gera erro se não existir)
conjunto.discard(100)  # Nenhum erro
print(conjunto)

# Limpando o conjunto
conjunto.clear()
print(conjunto)  # set()

# ------------------------------
# OPERAÇÕES ENTRE CONJUNTOS
# ------------------------------

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# União
print(a | b)  # {1, 2, 3, 4, 5, 6}

# Interseção
print(a & b)  # {3, 4}

# Diferença
print(a - b)  # {1, 2}
print(b - a)  # {5, 6}

# Diferença simétrica (elementos exclusivos de cada conjunto)
print(a ^ b)  # {1, 2, 5, 6}

# ------------------------------
# VERIFICAÇÕES
# ------------------------------

# Subconjunto
print({1, 2} <= a)  # True

# Superconjunto
print(a >= {1, 2})  # True

# Conjuntos disjuntos (sem elementos em comum)
print(a.isdisjoint({10, 11}))  # True
print(a.isdisjoint({2, 9}))    # False

# ------------------------------
# ITERANDO EM CONJUNTOS
# ------------------------------
for elemento in a:
    print(elemento)  # Não garante ordem

# ------------------------------
# CONJUNTOS IMUTÁVEIS (frozenset)
# ------------------------------
# Úteis quando você precisa de um conjunto que não pode ser alterado (por exemplo, como chave em dicionários)

imutavel = frozenset([1, 2, 3])
print(imutavel)

# imutavel.add(4)  # ERRO: 'frozenset' object has no attribute 'add'

# ------------------------------
# CUIDADO: conjuntos só aceitam elementos imutáveis (int, float, str, tuple)
# ------------------------------

# conjunto = {1, 2, [3, 4]}  # ERRO: list é mutável e não pode ser elemento de um set

# ------------------------------
# EXEMPLO PRÁTICO: eliminar duplicatas de uma lista
# ------------------------------
nomes = ['Ana', 'João', 'Ana', 'Carlos', 'João']
nomes_unicos = list(set(nomes))
print(nomes_unicos)  # ['João', 'Carlos', 'Ana'] — ordem não garantida
