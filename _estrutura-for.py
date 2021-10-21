"""
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
Depois modifique o programa para que ele mostre os números um ao lado do outro.
"""

"""
ESTRUTURA BÁSICA FOR:
for <item> in <conjunto_de_itens>:
    <bloco_de_codigo>
"""

"""
i = 0

for i in range(21):
    print (i)
"""



"""
pessoas = [({'nome': 'João', 'cidade': 'Belo Horizonte'}), 
           ({'nome': 'Maria', 'cidade': 'São Paulo'}), 
           ({'nome': 'Pedro', 'cidade': 'Curitiba'})]

contador = 0
for pessoa in pessoas:
    contador += 1
    print(contador)
    if pessoa['nome'] == 'Maria':
        print(pessoa['nome'], "mora em", pessoa['cidade'])
        break
"""











pessoas = [({'nome':'joao', 'profissao':'programador'}), 
           ({'nome':'maria','profissao':'medica'}), 
           ({'nome':'marcio','profissao':'engenheiro'})]

contador = 0

for pessoa in (pessoas):
    contador +=1
    if pessoa['nome'] == 'maria':
        continue
    print (contador)
    print(pessoa['nome'], 'trabalha com',pessoa['profissao'])
    
    