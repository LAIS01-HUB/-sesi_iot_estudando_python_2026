# Programa que compara dois números
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

if x > y:
    print("O maior número é:", x)
elif y > x:
    print("O maior número é:", y)
else:
    print("Os dois números são iguais")
