menu ='''
========== Menu ==========

Digite a opção desejada:
                         
    [1] - Deposito       
    [2] - Saque          
    [3] - Extrato        
    [4] - Sair           
                         
===========================

-> '''

saldo = 5000.00
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
# Desafio: Criar um sistema bancário simples com funcionalidades de depósito, saque e extrato.
    opcao = int(input(menu))
    print()

    if opcao == 1:
        
        deposito = float(input('Digite o valor do depósito: '))
    
        if deposito <= 0:
            print('Desculpe! \nValor de depósito inválido!')
        else:
            saldo += deposito
            extrato.append({"tipo": "Depósito", "valor": deposito})
            print(f'Depósito de R${deposito:.2f} realizado com sucesso!')
    
    elif opcao == 2:
        saque = float(input('Digite o valor do saque: '))

        if saque > saldo:
            print('Desculpe! \nNão será possivel realizar o saque, saldo insuficiente!')
        elif saque > limite:
            print('Desculpe! \nValor de saque excede o limite permitido!')
        elif numero_saques >= LIMITE_SAQUES:
            print('Desculpe! \nNúmero máximo de saques diários excedido!')
        else:
            saldo -= saque
            numero_saques += 1
            extrato.append({"tipo" : "Saque", "valor" : saque})
            print(f'Saque de R${saque:.2f} realizado com sucesso!')
    
    elif opcao == 3:
        if not extrato:
            print('Desculpe! \nNão há transações para exibir no extrato!')
        else:
            print('''\n\n\n===== Extrato =====''')
            for transacao in extrato:
                print(f'{transacao["tipo"]}: R${transacao["valor"]:.2f}')
            print(f'\nSaldo atual: R${saldo:.2f}')
            print('===================\n\n\n')

    elif opcao == 4:
        print('Obrigado por utilizar nossos serviços!')
        break

    else:
        print('Opção inválida! Por favor, escolha uma opção válida.')


                
