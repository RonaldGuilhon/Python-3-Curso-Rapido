def soma(a, b):
    return a + b

<<<<<<< HEAD
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
=======
somar = soma
print(somar(3, 4))
>>>>>>> 4f0a44feea6353cd7cb493ce9e7b4a05b72d2d5d
