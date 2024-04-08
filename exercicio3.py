#3

# Algoritmo 3 - Faça um programa que leia um caractere e indique se é uma vogal ou consoante.
caractere = input("Digite um caractere: ")

if caractere.lower() in 'aeiou':
    print("O caractere digitado é uma vogal.")
else:
    print("O caractere digitado é uma consoante.")