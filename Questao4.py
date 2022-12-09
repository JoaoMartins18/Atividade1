#Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos.

idade = int(input("Qual a idade do indivíduo? "))
cont = 0
soma = 0

while (idade >= 0):
    cont += 1
    soma += idade
    idade = int(input("Qual a idade do indivíduo? "))

if(cont != 0):
  media = soma / cont
  print(f"A média das idades é igual a {media} anos.")
else:
  print("Não foi digitado nenhuma idade.")
