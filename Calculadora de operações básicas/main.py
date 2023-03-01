num1 = float(input('Digite um número:'))
num2 = float(input('Digite outro número:'))

print('Selecione as opções de operações:')
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

escolha = input('Digite sua escolha(1/2/3/4):')

if escolha =='1':

   resultado = num1 + num2
   print('{} + {} = {}' .format(num1, num2, resultado))

elif escolha =='2':
   
   resultado = num1 - num2
   print('{} - {} = {}' .format(num1, num2, resultado))

elif escolha == '3':
   
   resultado = num1 * num2
   print('{} * {} = {}'.format(num1, num2, resultado))

elif escolha == '4':
   
   resultado = num1 / num2
   print('{} / {} = {}'.format(num1, num2, resultado))

else:
   print('O que você está tentando fazer, chefe?')

