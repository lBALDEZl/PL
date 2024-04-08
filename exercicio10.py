#10

# Algoritmo 26 - Escrever um algoritmo/programa que lê 10 valores e mostra a média dos valores
# lidos.
soma = 0

for i in range(10):
    valor = float(input(f"Digite o {i+1}º valor: "))
    soma += valor
	media = soma/ 10

print("A média dos 10 valores digitados é:", media)