""""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""
nome_a = 'Espanha'
nome_b = 'Brasil'

ano = 0

a = int(input('Digite a população do país A'))
b = int(input('Digite a população do país B'))
a_cres = float(input('Qual o %. do crescimento do país A?'))
b_cres = float(input('Qual o %. do crescimento do país B?'))

while a <= b:
	a += a * (a_cres)
	b += b * (b_cres)
	ano += 1

print ( "%s ultrapassa ou iguala ao %s em %d anos" %(nome_a, nome_b, ano) )

"""s
%s ---> mais usado para formatação em variaveis tipo string
%d ---> mais usado para formatação em variaveis tipo int
"""
