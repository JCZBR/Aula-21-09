utilizando = int (input('Digite 1 para utilizar o programa e 0 para encerrar: '))
soma = 0
cont = 0
while utilizando != 0:

  p = 0
  for i in range(1,11):
    print('Questão',i)
    r = input('R: ').upper()
    if i == 1 and r == 'A':
      p = p + 1
    elif i == 2 and r == 'B':
      p = p + 1
    elif i == 3 and r == 'C':
      p = p + 1
    elif i == 4 and r == 'D':
      p = p + 1
    elif i == 5 and r == 'E':
      p = p + 1
    elif i == 6 and r == 'E':
      p = p + 1
    elif i == 7 and r == 'D':
      p = p + 1
    elif i == 8 and r == 'C':
      p = p + 1
    elif i == 9 and r == 'B':
      p = p + 1
    elif i == 10 and r == 'A':
      p = p + 1

  print('GABARITO:','1-A','2-B','3-C','4-D','5-E','6-E','7-D','8-C','9-B','10-A')
  print('NOTA:',p)
  cont = cont + 1
  if cont == 1:
    maior = p
  elif p > maior:
    maior = p
  if cont == 1:
    menor = p
  elif p < menor:
    menor = p
  soma = soma + p
  utilizando = int (input('Digite 1 para utilizar o programa e 0 para encerrar: '))
media_turma = soma / cont
print('Maior acertos:',maior)
print('Menor acertos:',menor)
print('Total de Alunos:',cont)
print('Média da Turma:',media_turma)
