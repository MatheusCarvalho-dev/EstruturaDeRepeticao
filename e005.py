""""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""


ano = 0

a = int(input('Digite a população do país A'))
b = int(input('Digite a população do país B'))
a_cres = float(input('Qual o %. do crescimento do país A?'))
b_cres = float(input('Qual o %. do crescimento do país B?'))

while a <= b:
	a += a * (a_cres)
	b += b * (b_cres)
	ano += 1

print ( "A ultrapassa ou iguala a B em %d anos" %ano )