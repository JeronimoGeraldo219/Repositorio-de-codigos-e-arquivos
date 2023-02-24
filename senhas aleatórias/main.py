import random

print ('Bem-vindo ao gerador de senhas')

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&^,<>;:/?~][-_()+1234567890'

numero= input('Quantas senhas você quer gerar: ')
numero = int(numero)

tamanho = input('tamanho da senha: ')
tamanho = int(tamanho)

print('Aqui estão suas senhas: ')

for pwd in range(numero):
    password = ''
for c in range(tamanho):
    password += random.choice(caracteres)

print(password)