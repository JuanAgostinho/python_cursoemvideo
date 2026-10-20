#lista geral de todos os numeros
lista = []

#lista de numeros pares, numeros entram com uma condicional
lista_par = []

#lista de numeros impares, numeros entram com uma condicional
lista_impar = []

#entrada dos valores, para quando o usuario digita algo como N ou n
while True:

    n = int(input("Digite um valor: "))
    lista.append(n)
    condicao = str(input("Quer continuar? [S/N]"))
    
    #condição de parada
    if condicao in 'Nn':
        break

#condicional para definir par e impares
for num in lista:
    if num % 2 == 1:
        lista_impar.append(num)
    else:
        lista_par.append(num)

#saida das listas
print(f'Números digitados: {lista}')
print(f'Lista de pares: {lista_par}')
print(f'Lista de ímpares: {lista_impar}')