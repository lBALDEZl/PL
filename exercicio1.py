#1

# Algoritmo 1 - Crie um programa que receba o salário de um empregado e o percentual de 
# aumento, calcule e mostre o valor do aumento e o novo salário. 

salario = float(input("Digite seu salário total: R$ "))
aumento = float(input("Digite o percentual de aumento (%): "))

aumento = salario * (aumento / 100)
novo_salario = salario + aumento

print(f"O valor do aumento será de R$ {aumento:.2f}")
print(f"O novo salário será de R$ {novo_salario:.2f}")
