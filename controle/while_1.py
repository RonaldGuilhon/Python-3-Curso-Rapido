# Inicializa as variáveis que irão acumular o total das notas e a quantidade de alunos
total = 0      # Soma acumulada das notas
qtde = 0       # Quantidade de notas válidas inseridas
nota = 0       # Variável de controle para o loop

# Laço que continua até que o usuário digite -1
while nota != -1:
    # Solicita uma nota ao usuário
    nota = float(input('Informe a nota do aluno ou -1 para sair: '))

    # Verifica se a nota é válida antes de acumular
    if nota != -1:
        qtde += 1         # Conta mais um aluno
        total += nota     # Soma a nota ao total

# Após o loop, verifica se alguma nota válida foi inserida
if qtde > 0:
    media = total / qtde
    print(f'\nTotal de alunos: {qtde}')
    print(f'Soma das notas: {total}')
    print(f'A média da turma é: {media:.2f}')
else:
    print('\nNenhuma nota válida foi inserida.')
