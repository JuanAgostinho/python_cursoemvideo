lista = []
lista_par = []
lista_impar = []
while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    sn = str(input("Quer continuar [S/N] "))
    if sn in "Nn":
        break
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista_par.append(lista[i])
    else:
        lista_impar.append(lista[i])

print(f"Valores digitados {lista}")
print(f"Lista de pares {lista_par.sort()}")
print(f"Lista de impares {lista_impar.sort()}")