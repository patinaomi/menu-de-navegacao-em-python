def menu_principal():
    while True:
        print('====== SALESFORCE ======')
        print(' [1] Sobre a Salesforce')
        print(' [2] Sobre CRM')
        print(' [3] Produtos Oferecidos')
        print(' [4] Assine a Newsletter')
        print(' [5] Entre em Contato')
        print(' [6] Sair do Site')
        print('========================')

        op = input(' Digite uma opção: ')

        if op == '1':
            sobre_salesforce()
        elif op == '2':
            sobre_crm()
        elif op == '3':
            sobre_produtos()
        elif op == '6':
            print('\nObrigado por visitar nosso site!')
            break
        else:
            print('Opção inválida. Tente novamente.')


def sobre_salesforce():
    while True:
        print('\n>>>>> SOBRE A SALESFORCE <<<<<')

        print(' [1] O que é Salesforce?')
        print(' [2] O que faz Salesforce?')
        print(' [3] Por que usar Salesforce?')
        print(' [4] Voltar ao menu principal')
        print('------------------------------')

        op = input(' Escolha uma opção: ')

        if op == '1':
            print('\n>>>>> O que é Salesforce? <<<<<')
            print('blablabla')
            print('------------------------------------')
        elif op == '2':
            print('\n>>>>> O que faz Salesforce? <<<<<')
            print('blablabla')
            print('------------------------------------')
        elif op == '3':
            print('\n>>>>> Por que usar Salesforce? <<<<<')
            print('blablabla')
            print('------------------------------------')

        elif op == '4':
            break
        else:
            print(' Opção inválida. Digite novamente.')


def sobre_crm():
    while True:
        print('Submenu 2:')
        print('1. Opção 1')
        print('2. Voltar ao menu principal')

        op = input('Escolha uma opção: ')

        if op == '1':
            print('Executando a opção 1 do Submenu 2.')
        elif op == '2':
            break
        else:
            print('Opção inválida. Tente novamente.')


menu_principal()
