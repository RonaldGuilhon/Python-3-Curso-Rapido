a = 'valor'       # True - string com conteúdo
a = 0             # False - número zero
a = -0.00001      # True - número diferente de zero
a = ''            # False - string vazia
a = ' '           # True - espaço em branco ainda é um caractere
a = []            # False - lista vazia
a = {}            # False - dicionário vazio

if a:
    print('Existe!')  # Só executa se a for "truthy"
else:
    print('Não existe ou zero ou vazio...')  # Executa se a for "falsy"
