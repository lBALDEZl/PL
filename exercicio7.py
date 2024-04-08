#7

# Algoritmo 10 - Crie um programa que verifique se um caractere inserido pelo usuário 
# é uma letra maiúscula ou minúscula. 
caractere = input("Digite um caractere: ")

if 'A' <= caractere <= 'Z':
    print("O caractere digitado é uma letra maiúscula.")

elif 'a' <= caractere <= 'z':
    print("O caractere digitado é uma letra minúscula.")
else:
    print("O caractere digitado não é uma letra.")