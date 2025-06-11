# variaveis.py

# Atribuição de variáveis numéricas
a = 3           # inteiro
b = 4.4         # float (número com ponto decimal)

# Soma entre inteiro e float resulta em float
print(a + b)    # 7.4

# Variáveis com string e concatenação
texto = 'Sua idade e ...'
idade = 23

# Concatenando string com número convertido para string
print(texto + str(idade))  # Sua idade e ...23

# Interpolação com f-string (forma mais moderna e recomendada)
print(f'{texto}{idade}')  # Sua idade e ...23

# Repetição de string com multiplicação
saudacao = 'Bom dia '
print(3 * saudacao)  # Bom dia Bom dia Bom dia 

# Constante (por convenção, variáveis em maiúsculas são consideradas constantes)
PI = 3.14

# Entrada de dados (o input sempre retorna uma string, então usamos float() para converter)
raio = float(input('Informe o raio da circunferencia: '))

# Verificando o tipo da variável 'raio'
print(type(raio))  # <class 'float'>

# Cálculo da área de uma circunferência: A = π * r²
area = PI * raio * raio

# Exibindo a área
print(area)

# Exibindo a área com texto explicativo usando f-string
print(f'A area da circunferencia e {area} m2')
