lista = []
while True:
    n = int(input("Digite um número: "))
    sn = str(input("Quer continuar? [S/N]: ")).upper()
    if n not in lista:
        lista.append(n)
    lista_ordenada = sorted(lista)
    if sn[0] == "N":
        print(lista_ordenada)
        break