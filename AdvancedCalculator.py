import math as m

n1 = float(input('insira o v1: '))
n2 = float(input('insira o v2: '))

while True:
  opcao = input('\nEscolha uma Operação:\n1-Soma \n2-Subtração \n3-Multiplicação \n4-Divisão \n5-Arredondar para cima\n6-Arredondar para baixo\n7-Parte inteira (truncamento)\n8-Raiz quadrada\n9-Potência\n10-Raiz quadrada inteira\n11-Fatorial\n12-Sair\n\n' )
  if opcao == '12':
    print('Obrigado, Volte sempre')
    break
  if opcao == '1':
    print(f'\nOs valores {n1, n2}: resultado da soma {m.fsum([n1, n2]):.2f}')
  elif opcao == '2':
    print(f'\nOs valores {n1, n2}: resultado da subtração {n1-n2:.2f}')
  elif opcao == '3':
    print(f'\nOs valores {n1, n2}: resultado da multiplicação {n1*n2}')
  elif opcao == '4':
    print(f'\nOs valores {n1, n2}: resultado da divisão {n1 / n2} resultado inteiro {n1 // n2}')
  elif opcao == '5':
    print(f'\nOs valores arredondados para cima {n1, n2}: resultado {m.ceil(n1)} e {m.ceil(n2)}')
  elif opcao == '6':
    print(f'\nOs valores arredondados para baixo {n1, n2}: resultado {m.floor(n1)} e {m.floor(n2)}')
  elif opcao == '7':
    print(f'\nOs valores {n1, n2}: inteiros {m.trunc(n1)} e {m.trunc(n2)}')
  elif opcao == '8':
    if n1 and n2 < 0:
      print('número invalido para essa operação, insira um novo número')
    else:
      n1_baixo= m.floor(n1)
      n2_baixo= m.floor(n2)
      print(f'\nOs valores {n1, n2}: Raiz quadrada {m.sqrt(n1_baixo)} e {m.sqrt(n2_baixo)}')
  elif opcao == '9':
    print(f'\nOs valores {n1, n2}: Potência {m.pow(n1,n2)} e {m.pow(n2,n1)}')
  elif opcao == '10':
    n1_int = int(n1)
    n2_int = int(n2)
    print(f'\nOs valores {n1, n2}: Raiz quadrada inteira {m.isqrt(n1_int)} e {m.isqrt(n2_int)}')
  elif opcao == '11':
    if n1 and n2 < 0:
      print('número invalido para essa operação, insira um novo número')
    else:
      n1_int = int(n1)
      n2_int = int(n2)
      print(f'\nOs valores {n1, n2}: Fatorial {m.factorial(n1_int)} e {m.factorial(n2_int)}')
  else:
    print('\n\nOpção invalida, tente novamente!')
