print()
print("### INÍCIO DO PROGRAMA ###")
print()

a = "Vinícius"      # String a
b = "Albuquerque"   # String b
c = "Nóbrega"       # String c

concatenar = a + " " + b + " " + c                      # concatenação das Strings em conjunto com os espaços

print(concatenar)                                       # Printar na tela
print()

tamanho = len(concatenar)                               # Método len faz a contagem de caracteres da string na variável

print(tamanho)                                          # Printar na tela
print()

print(concatenar[0], concatenar[9], concatenar[21])     # Printa as respectivas posições da String concatenar na tela
print(a[0], b[0], c[0])                                 # Printa as posições 0 das respectivas Strings
print()

print(concatenar[0:28:2])                               # Printa as posições da String de 0 a 28-1 de 2 em 2

print()
print("### FIM DO PROGRAMA")