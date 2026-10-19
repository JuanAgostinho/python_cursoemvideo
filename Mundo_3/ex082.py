numbers = []
while True:
    num = int(input("Digite um número: "))
    sn = str(input("Quer continuar [S/N]")).lower().split()
    numbers.append(num)
    if sn == 'n':
        break

par = []
impar = []

for i in numbers:
    if i % 2 == 0:
