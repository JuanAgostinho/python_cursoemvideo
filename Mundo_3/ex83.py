expressao = str(input("Digite uma expressão: "))

a = 0
f = 0

for caracter in expressao:
    if caracter == "(":
        a += 1
    elif caracter == ")":
        f += 1

if a == f:
    print("A expressão é válida!")
else:
    print("A expressão é inválida")