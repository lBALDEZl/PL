#4

# Algoritmo 4 - Crie um programa que calcule o valor total a ser pago 
# em uma conta de restaurante, considerando o valor da refeição e uma taxa de serviço.
valor_refeicao = float(input("Digite o valor da refeição: "))

taxa_servico = float(input("Digite a taxa de serviço (em porcentagem): "))

taxa = valor_refeicao * (taxa_servico / 100)

total = valor_refeicao + taxa

print("O valor total a ser pago, incluindo a taxa de serviço, é de R$", total)