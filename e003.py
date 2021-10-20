#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';


nome = str(input('Digite seu nome: '))
while (len(nome) <= 3):
    nome = str(input('Digite seu nome contendo mais de 3 letras: '))

idade = int(input('Digite sua idade: '))
while (idade < 0 or idade > 150 ):
    idade = int(input('Digite sua idade (ela deve ser maior que 0): '))

salario = int(input('Digite seu salário: '))
while (salario < 0 ):
    salario = int(input('Digite sua salário (ele deve ser maior que 0): '))

sexo = str(input('Digite f para feminino ou m para masculino '))
while (sexo != "f" and sexo != "m"):
    sexo = str(input('Digite f para feminino ou m para masculino: '))
if (sexo == 'm'):
    sexo = 'Masculino'
else:
    sexo = 'Feminino'

estado_civil = str(input('Estado civil: c, s, d ou v '))
while (estado_civil != "c" and estado_civil != "s" and estado_civil != "d" and estado_civil != "v"):
    estado_civil = str(input('Estado civil: c, s, d ou v: '))
    



print('Nome: ',nome)
print('Idade: ',idade)
print('Salário: R$',salario)
print('Sexo: ', sexo)
print('Estado civil: ',estado_civil)

