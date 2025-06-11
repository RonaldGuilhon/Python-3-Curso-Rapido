# Situação simulada
lockdown = True
grana = 30

# Operador ternário (expressão condicional):
# Sintaxe: valor_se_verdadeiro if condição else valor_se_falso
status = "Em casa" if lockdown or grana <= 100 else "Uhuuu"

print(status)  # Saída: "Em casa"


#exemplo 02
idade = 18
mensagem = "Maior de idade" if idade >= 18 else "Menor de idade"
print(mensagem)  # Maior de idade


#exemplo 03
nota = 7
status = "Aprovado" if nota >= 6 else "Reprovado"
print(status)  # Aprovado
