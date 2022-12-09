#Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

cont = 0 

for i in range(1,6,1):
    numero = int(input(f"Escolha o {i}º número inteiro: "))
    if(numero % 2 == 0):
        cont = cont + 1

print(f"\nQuantidade de números pares: {cont}.")
