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
            print('A Salesforce é uma empresa de softwares que foca na solução de'
                  '\ngerenciamento de relacionamento para aproximar empresas e pessoas.'
                  '\nÉ uma plataforma de CRM integrada que oferece a todos os departamentos'
                  '\numa visão única e compartilhada de cada cliente.')
        elif op == '2':
            print('\n>>>>> O que faz Salesforce? <<<<<')
            print('Utilizando o Salesforce Customer 360, nossa plataforma de CRM integrada,'
                  '\nsua empresa oferece experiências personalizadas para seus clientes.'
                  '\nNossa solução fornece produtos poderosos e conectados para melhorar seu'
                  '\nmarketing, vendas, commerce, atendimento aocliente, TI e muito mais.')

        elif op == '3':
            print('\n>>>>> Por que usar Salesforce? <<<<<')
            print('- Atraia mais compradores com uma estratégia de marketing personalizada')
            print('- Conquiste mais clientes conhecendo suas necessidades e preocupações')
            print('- Atenda às expectativas dos seus clientes oferecendo experiências incríveis de compra')
            print('- Responda rapidamente aos problemas de suporte ao cliente em qualquer canal')
            print('- Automatize tarefas demoradas criando aplicativos personalizados')

        elif op == '4':
            break
        else:
            print(' Opção inválida. Digite novamente.')


def sobre_crm():
    while True:
        print('\n>>>>> SOBRE CRM <<<<<')

        print(' [1] O que é CRM?')
        print(' [2] O que faz Salesforce?')
        print(' [3] Por que usar Salesforce?')
        print(' [4] Voltar ao menu principal')
        print('------------------------------')

        op = input(' Escolha uma opção: ')

        op = input('Escolha uma opção: ')

        if op == '1':
            print('Executando a opção 1 do Submenu 2.')
            print('CRM é a sigla usada para Customer Relationship Management e se refere ao conjunto de práticas, estratégias de negócio e tecnologias focadas no relacionamento com o cliente.')
        elif op == '2':
            break
        else:
            print('Opção inválida. Tente novamente.')


menu_principal()
