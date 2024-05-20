print('Banco Central'.center(40, '='))
menu = '''
[d] - Depósito
[s] - Saque
[e] - Extrato
[q] - Sair

=>'''
print(menu)
saldo = 0
limite = 500
NUMERO_SAQUE = 0
saque = 0
depositos = 0
extrato = ''

while True:
    print('-'*35)
    opcao = input('Escolha uma opção: ').strip().lower()
    print()

    if opcao == 'd':
      print('Depósito'.center(35, '-'))
      valor = float(input('Informe o valor do depósito: R$ '))
      if valor < 0:
        print('Valor inválido!')
        continue
      saldo += valor
      extrato += f'Depósito R$ {valor:.2f}\n'
      depositos += 1
      print('Depósito realizado com sucesso!')
      
    elif opcao == 's':
      print('Saque'.center(35, '-'))
      if NUMERO_SAQUE == 3:
        print('Limite de saque excedido!')
        continue
      valor = float(input('Informe o valor do saque: R$ '))
      if valor > 500:
        print('Você não pode sacar mais do que 500 reais!')
        continue
      if valor > saldo:
        print('Saldo insuficiente!')
        continue
      else:
        saldo -= valor
        extrato += f'Saque R$ {valor:.2f}\n'
        NUMERO_SAQUE += 1
      print('Saque realizado com sucesso!')
      

    elif opcao == 'e':
      print('Extrato'.center(35, '-'))
      
      print('Não houve movimentação.' if not extrato else extrato)

      print(f'Saldo:'.ljust(25, '.')+f'R$ {saldo:.2f}')

    elif opcao == 'q':
      print('Sair'.center(35, '-'))
      break

    else:
      print('Opção inválida')
    print('')

