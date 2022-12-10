#Faça uma função chamada calculaSalario que recebe como parâmetro o valor do salário bruto e calcula o salário líquido. O salário líquido é calculado a partir do salário bruto, primeiro descontando 11% referente ao INSS, e do resultado, descontando-se 15% de imposto de renda (IR).

def calculaSalario(bruto):
    inss = bruto * (11/100)
    ir = (bruto - inss) * (15/100)
    liquido = bruto -(inss + ir)
    return liquido

salario_bruto = float(input("Qual é o valor do salário? "))

salario_liquido = calculaSalario(salario_bruto)

print(f"O valor do salário líquido é igual a R$ {salario_liquido}.")
