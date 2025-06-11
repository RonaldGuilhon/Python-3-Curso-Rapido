# lista.py

# Criando uma lista com elementos inteiros
nums = [1, 2, 3]

# Verificando o tipo do objeto
print(type(nums))  # <class 'list'>

# Adicionando elementos ao final da lista
nums.append(3)
nums.append(4)
nums.append(500)

# Verificando o tamanho da lista após os append
print(len(nums))  # 6 elementos

# Atualizando o valor no índice 3 (0-based indexing)
nums[3] = 100  # Altera o valor 3 para 100 na quarta posição

# Inserindo um elemento no início da lista
nums.insert(0, -200)  # [-200, 1, 2, 3, 100, 4, 500]

# Acessando o sétimo elemento (índice 6)
print(nums[6])  # 500

# Acessando o último elemento usando índice negativo
print(nums[-1])  # 500 (último elemento)

# Imprimindo a lista completa
print(nums)  # [-200, 1, 2, 3, 100, 4, 500]
