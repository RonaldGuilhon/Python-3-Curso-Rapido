def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

somar = soma
print(somar(2, 3))

def operacao_aritimetica(fn, op1, op2):
    return fn(op1, op2)

resultado = operacao_aritimetica(soma, 10, 20)
print(resultado)

resultado = operacao_aritimetica(subtracao, 10, 20)
print(resultado)

def soma_parcial(a):
    # processamento pesado 1 - 10s
    # processamento pesado 2 - 10s
    # processamento pesado 3 - 40s
    def concluir_soma(b):
        return a + b # 10s
    return concluir_soma

# r1 = soma_total(1, 2) => 1m10s
# r2 = soma_total(1, 3) => 1m10s
# r3 = soma_total(1, 4) => 1m10s

soma_1 = soma_parcial(1) # 1 min
r1 = soma_1(2)
r2 = soma_1(3)
r3 = soma_1(3)

resultado_final = soma_parcial(10)(12)
print(resultado_final)
