#8

# Algoritmo 24 - Escrever um algoritmo/programa que lê 20 valores e mostra quantos destes 
# valores são maiores ou iguais a 5.
contagem = 0

for i in range(20):
    valor = float(input(f"Digite o {i+1}º valor: "))
    
    if valor >= 5:
        contagem += 1

print(f"Entre os 20 valores digitados, {contagem} deles são maiores ou iguais a 5.")