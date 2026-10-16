# Programa que calcula o fatorial de um número
numero = int(input("Digite um número inteiro não negativo: "))

fatorial = 1

if numero < 0:
    print("Digite um número não negativo")
else:
    for i in range(1, numero + 1):
        fatorial = fatorial * i

    print("O fatorial é:", fatorial)
