#9

# Algoritmo 25 - Escrever um algoritmo/programa que lê 10 valores e 
# mostra quantos destes valores são negativos.
contagem = 0

for i in range(10):
    valor = float(input(f"Digite o {i+1}º valor: "))
    
    if valor < 0:
        contagem += 1
print(f"Dos 10 valores digitados, {contagem} deles são negativos.")