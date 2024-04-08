#11

# Algoritmo 27 - Escreva um algoritmo/programa que receba 30 números e mostre a soma dos
#números positivos recebidos.
soma = 0

for i in range(30):
    numero = float(input(f"Digite o {i+1}º número: "))
    
    if numero > 0:
        soma += numero

print("A soma dos números positivos recebidos é:", soma)