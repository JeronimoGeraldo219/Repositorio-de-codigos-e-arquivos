a1 = float(input("Digite o primeiro termo da PG: "))
r = float(input("Digite a razão da PG: "))

# Cálculo do valor do termo geral
n = int(input("Digite o número do termo que deseja encontrar: "))
an = a1 * (r ** (n-1))
print('O valor do {} º termo é: {}'.format(n, an))

# Cálculo da soma dos termos
s = 0
n = int(input("Digite o número de termos que deseja somar: "))
for i in range(n):
    s += a1 * (r ** i)
print('A soma dos{} "primeiros termos é: {}' .format(n,s))

# Cálculo da soma dos infinitos termos
if abs(r) < 1:
    si = a1 / (1 - r)
    print('A soma dos infinitos termos é: {}'.format(si))
else:
    print("A soma dos infinitos termos não existe.")




