valor = int(input('Insira o valor inicial: '))
tempo = int(input('Insira a quantidade de dias em atraso: '))
taxa = int(input('Insira a taxa de atraso: '))

prestacao = valor+(valor*(taxa/100)*tempo)

print('O valor total é de ', prestacao)