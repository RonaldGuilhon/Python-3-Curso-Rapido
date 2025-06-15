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
    def concluir_soma(b):
        return a + b
    return concluir_soma