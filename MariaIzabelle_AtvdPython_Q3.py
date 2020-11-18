n1 = int(input('Insira a primeira nota: '))
n2 = int(input('Insira a segunda nota: '))
n3 = int(input('Insira a terceira nota: '))
freq = int(input('Insira o percentual de frequência: '))

mf = (n1 + n2 + n3) / 3

if mf >= 7 :
  print('Aprovado Por Media')

else:
  print('Reprovado Por Media')

if freq >= 75 :
  print('Aprovado por frequência adequada')  

else:
  print('Reprovado por frequência inaquedada')

