C = float(input('Digite o valor do capital em reais: R$'))
i = float(input('Digite o valor da taxa de juros em decimal: '))
n = int(input('Digite o valor do tempo da applicação em meses: '))

Montante = C*(1+i)**n

print('O valor do montante é {}'.format(Montante))