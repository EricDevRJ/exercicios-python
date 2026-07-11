if int(input('Qual sua idade: ')) >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')

nota = int(input('Digite sua nota: '))

if nota >= 10:
    print('Nota máxima!')
elif nota >= 7:
    print('Aprovado!')
elif nota >= 5:
    print('Recuperação!')
else:
    print('Reprovado!')

contador = 0 #while repete enquanto a condição for verdadeira #contador é a variável
while True:
    contador += 1
    print(contador)
    if contador >= 3:
        break #break interrompe o loop

for numero in range(1, 6): #for repete um número de vezes definido pelo range #Comece do 1 e vá até 5, o 6 é exclusivo
    print(numero * 2)