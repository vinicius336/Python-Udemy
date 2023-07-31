print()
print("### INÍCIO DO PROGRAMA")
print()

print("Funções são techos de códigos que podem ser executados mais de uma vez quando necessário sem que precise escrever este código repetidamente")
print("Em Python uma função é declarada através da palavra reservada 'def' antes de ser chamada")
print("O resultado da função é calculado e passado para fora da função através da palavra reservada 'return'")
print()
print("Veja no código como foi feita uma função de soma e multiplicaçãço")
print()

def soma(x, y):
    return x + y

def multiplicacao(x, y):
    return x * y

a = 2
b = 3

print("A soma de a e b é: ", soma(a, b))
print("A multiplicação de a e b é: ", multiplicacao(a, b))
print("O produto da soma de a e b com o valor de a é: ", multiplicacao(soma(a, b), a))

print()
print("### FIM DO PROGRAMA")