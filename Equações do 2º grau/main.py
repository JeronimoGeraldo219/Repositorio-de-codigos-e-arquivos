a = float(input('valor de a: '))
b = float(input('valor de b: '))
c = float(input('valor de c: '))

delta = (b ** 2) - 4 * a * c


if a == 0:
    print("a deve ser diferente de 0")
elif delta < 0:
    print("Não possui raízes reais")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print("x1 =  {}, x2 = {}".format(x1, x2))