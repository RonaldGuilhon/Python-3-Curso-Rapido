# Solicita a nota do aluno e converte para float
nota = float(input('Informe a nota do aluno: '))

# Verifica faixas de desempenho com base na nota
if nota >= 9:
    print('Duas palavras: para bens! :p')
    print('Quadro de honra')  # Nota excelente
elif nota >= 7:
    print('Aprovado')         # Nota boa
elif nota >= 5:
    print('Recuperação')      # Nota mediana
elif nota >= 3:
    print('Recuperação + trabalho')  # Nota baixa, exige esforço extra
else:
    print('Reprovado')        # Nota muito baixa

# Exibe a nota ao final
print(nota)
