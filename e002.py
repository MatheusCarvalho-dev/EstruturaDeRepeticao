#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.
print('Insira seu nome e senha de modo que sejam diferentes \n')
nome = str(input('Digite seu nome: '))
senha = str(input('Digite sua senha: '))
    
while nome == senha:
    print('Insira seu nome e senha de modo que sejam diferentes! \n')
    nome = str(input('Digite seu nome: '))
    senha = str(input('Digite sua senha: '))
else:
    print('Nome e senha inseridos corretamente!')
