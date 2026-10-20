lista = []
while True:
    n = int(input("Digite um valor: "))
    sn = str(input("Quer continuar? S/N "))
    lista.append(n)
    if sn in "Nn":
        break
print('-=-' * 18)
print(f"Você digitou {len(lista)} elementos")
print(f"A lista em ordem decrescente: {lista[::-1   ]}")
if 5 not in lista:
    print("O valor 5 não está na lista")
else: 
    print("o valor 5 está na lista")