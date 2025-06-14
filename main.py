#!python
#print('Ola mundo!')
#import pacote.sub.arquivo

#import tipos.variaveis
#from tipos import variaveis, basicos
#import tipos.lista
#import tipos.tuplas
#import tipos.conjuntos
#import tipos.dicionario

#import operadores.unarios
#import operadores.aritimeticos
#import operadores.relacionais
#import operadores.atribuicao
#import operadores.logicos
#import operadores.ternario

#import controle.if_1
#import controle.if_2
#import controle.for_1
#import controle.while_1
#import controle.outros_exemplos

from funcoes import basico

basico.saudacao()  
basico.saudacao('João')
basico.saudacao('Maria', 33)
basico.saudacao(idade=25)

a =basico.soma_e_multi(a=2, b=3, x=10)
b =basico.soma_e_multi(a=3, b=7, x=20)

resultado = a + b
print(resultado)
print(a)