print()
print("### INÍCIO DO PROGRAMA ###")
print()

a = "Vinícius"      # String a
b = "Albuquerque"   # String b
c = "Nóbrega"       # String c

concatenar = a + " " + b + " " + c                      # concatenação das Strings em conjunto com os espaços

print(concatenar)                                       # Printar na tela
print()

"""
    Métodos em Strings
        São funções nativas que aplicam modificações à string
        Considerando a variável "nome" os métodos são aplicados com o seguinte formato:
            nome.metodo()

    Principais Métodos em Strings
        nome.lower()        # Todas as letras da string ficam minúsculas
        nome.upper()        # Todas as letras da string ficam maiúsculas
        nome.capitaliza()   # A primeira letra da string fica em maiúscula
        nome.stripe()       # Remove um caractere especial do final da string, como quebra de linha e espaço, por exemplo
        nome.split()        # Transforma a string em uma lista
        nome.find()         # Procura a primeira posição de um termo/caractere na string
        nome.replace()      # Substitui a string encontrada na primeira posição pela string informada na segunda posição
"""

print(concatenar.lower() + " | concatenar - lower")
print(concatenar.upper() + " | concatenar - upper")
print(concatenar.capitalize() + " | concatenar - capitalize")
print(a.lower() + " " + b.lower() + " " + c.lower() + " | a + b + c - lower")
print(a.capitalize() + " " + b.capitalize() + " " + c.capitalize() + " | a + b + c - capitalize")
print()

concatenar = concatenar.upper()
print(concatenar + " | upper")
concatenar = concatenar.capitalize()
print(concatenar + " | capitalize")
concatenar = concatenar + "\n"
print(concatenar + " | \\n na variável")
print(concatenar.strip() + " | strip (corta o \\n (ou outros caracteres especiais) da variável)")
print()

Nome = concatenar.split()
print(Nome)
print()
nome = a.split("i")
print(nome)
print()

busca = concatenar.find("u")
print(busca)
print()

a = a.replace("Vinícius", "Sarah")
print(a)

print()
print("### FIM DO PROGRAMA")