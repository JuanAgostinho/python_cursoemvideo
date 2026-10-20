lista = []
for i in range(5):
    entrada = int(input(f"Digite um valor pra posição {i}: "))
    lista.append(entrada)
print(f"Você digitou os valores: {lista}")
lista_ordenada = sorted(lista)
pos_maior = []
pos_menor = []
for i in range(5):
    if lista_ordenada[4] == lista[i]:
        pos_maior.append(i)
for i in range(5):
    if lista_ordenada[0] == lista[i]:
        pos_menor.append(i)
pos_maior.sort()
pos_menor.sort()
print(f"O maior valor foi {lista_ordenada[4]} nas posições {pos_maior}")
print(f"O menor valor foi {lista_ordenada[0]} nas posições {pos_menor}")