import json
import re

def menu_principal():
    while True:
        print('======= SALESFORCE =======')
        print(' [1] Sobre a Salesforce')
        print(' [2] Sobre CRM')
        print(' [3] Produtos Oferecidos')
        print(' [4] Assine a Newsletter')
        print(' [5] Formulário de Contato')
        print(' [0] Sair do Site')
        print('==========================')

        op = input(' Digite uma opção: ')

        if op == '1':
            sobre_salesforce()
        elif op == '2':
            sobre_crm()
        elif op == '3':
            sobre_produtos()
        elif op == '4':
            assinar_newsletter()
        elif op == '5':
            cadastro_contato()
        elif op == '0':
            print('\n Obrigado por visitar nosso site!')
            break
        else:
            print(' Opção inválida, digite novamente.\n')


def sobre_salesforce():
    while True:
        print('\n>>>>> SOBRE A SALESFORCE <<<<<')

        print(' [1] O que é Salesforce?')
        print(' [2] O que faz Salesforce?')
        print(' [3] Por que usar Salesforce?')
        print(' [0] Voltar ao menu principal')
        print('------------------------------')

        op = input(' Digite uma opção: ')

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
                  '\nmarketing, vendas, commerce, atendimento ao cliente, TI e muito mais.')

        elif op == '3':
            print('\n>>>>> Por que usar Salesforce? <<<<<')
            print('- Atraia mais compradores com uma estratégia de marketing personalizada')
            print('- Conquiste mais clientes conhecendo suas necessidades e preocupações')
            print('- Atenda às expectativas dos seus clientes oferecendo experiências incríveis de compra')
            print('- Responda rapidamente aos problemas de suporte ao cliente em qualquer canal')
            print('- Automatize tarefas demoradas criando aplicativos personalizados')

        elif op == '0':
            break
        else:
            print(' Opção inválida, digite novamente.')


def sobre_crm():
    while True:
        print('\n>>>>> SOBRE CRM <<<<<')

        print(' [1] O que é CRM?')
        print(' [2] O que faz um CRM?')
        print(' [3] Por que o CRM é importante e quais os benefícios?')
        print(' [0] Voltar ao menu principal')
        print('------------------------------')

        op = input(' Digite uma opção: ')

        if op == '1':
            print('\n>>>>> O que é CRM? <<<<<')
            print('CRM é a sigla usada para Customer Relationship Management e se refere ao conjunto'
                  '\nde práticas, estratégias de negócio e tecnologias focadas no relacionamento com o cliente.')

        elif op == '2':
            print('\n>>>>> O que faz um CRM? <<<<<')
            print('O CRM armazena informações de clientes atuais e potenciais, e suas atividades e pontos de'
                  '\ncontato com a empresa, incluindo visitas a sites, ligações telefônicas, e-mails, entre'
                  '\noutras interações. Entretanto, o software de CRM não é apenas uma lista de contatos'
                  '\nelaborada: ele reúne e integra dados valiosos para preparar e atualizar suas equipes'
                  '\ncom informações pessoais dos clientes, histórico e preferência de compras.')

        elif op == '3':
            print('\n>>>>> Por que o CRM é importante e quais os benefícios? <<<<<')
            print('Um CRM ajuda sua empresa a dispensar os processos obsoletos e o esforço manual para que o seu'
                  '\nnegócio possa progredir. A plataforma organiza as contas e contatos de forma acessível, em'
                  '\ntempo real, acelerando e simplificando o processo de vendas.')

        elif op == '0':
            break
        else:
            print(' Opção inválida, digite novamente.')


def sobre_produtos():
    while True:
        print('\n>>>>> PRODUTOS OFERECIDOS <<<<')
        print('A Salesforce oferece uma ampla gama de serviços e produtos que ajudam as empresas a aprimorar'
              '\no relacionamento com os clientes, automatizar processos de negócios e tomar decisões baseadas'
              '\nem dados. Alguns dos principais serviços e produtos oferecidos pela Salesforce incluem: ')
        print('\n- Sales Cloud, Service Cloud, Marketing Cloud, Commerce Cloud, Community Cloud, Einsten AI,'
              '\nPlatform e App Cloud, Industries Cloud, IoT Cloud, Tableau, MuleSoft e Heroku.')

        print('\n [1] Saber mais sobre um produto específico')
        print(' [0] Voltar ao menu principal')
        print('------------------------------')

        op = input(' Digite uma opção: ')

        if op == '1':
            produto_especifico()

        elif op == '0':
            break
        else:
            print(' Opção inválida, digite novamente.')


def produto_especifico():
    while True:
        print('\n>>>>> LISTA DE PRODUTOS <<<<<')

        print(' 1.  Salescloud')
        print(' 2.  Service Cloud')
        print(' 3.  Marketing Cloud')
        print(' 4.  Commerce Cloud')
        print(' 5.  Community Cloud')
        print(' 6.  Einstein AI')
        print(' 7.  Platform e App Cloud')
        print(' 8.  Industries Cloud')
        print(' 9.  IoT Cloud')
        print(' 10. Tableau')
        print(' 11. MuleSoft')
        print(' 12. Heroku')
        print('------------------------------')
        print(' Sobre qual produto você gostaria de saber mais?')
        op = input(' Digite uma opção ou \'0\' para retornar ao menu anterior: ')

        if op == '1':
            print('\n>>>>> Produto - Salescloud <<<<<')
            print('Uma solução de gerenciamento de vendas que ajuda a acompanhar leads, oportunidades e clientes,'
                  '\nalém de fornecer automação de vendas e análises.')

        elif op == '2':
            print('\n>>>>> Produto - Service Cloud <<<<<')
            print('Oferece ferramentas para gerenciar o atendimento ao cliente, incluindo casos, serviços de'
                  '\ncampo, suporte multicanal e chat ao vivo.')

        elif op == '3':
            print('\n>>>>> Produto - Marketing Cloud <<<<<')
            print('Uma suíte de automação de marketing que permite segmentação de público, personalização de'
                  '\ncampanhas e análises avançadas.')

        elif op == '4':
            print('\n>>>>> Produto - Commerce Cloud <<<<<')
            print('Ajuda as empresas a criar e gerenciar lojas online e experiências de comércio eletrônico.')

        elif op == '5':
            print('\n>>>>> Produto - Community Cloud <<<<<')
            print('Facilita a criação de comunidades online para interações com clientes, parceiros e funcionários.')

        elif op == '6':
            print('\n>>>>> Produto - Einstein AI <<<<<')
            print('Incorpora recursos de inteligência artificial (IA) em várias soluções Salesforce para análise'
                  '\npreditiva, automação e aprendizado de máquina.')

        elif op == '7':
            print('\n>>>>> Produto - Platform e App Cloud <<<<<')
            print('Permite que as empresas criem aplicativos personalizados na plataforma Salesforce ou usem'
                  '\naplicativos disponíveis no Salesforce AppExchange, que é um mercado de aplicativos de terceiros.')

        elif op == '8':
            print('\n>>>>> Produto - Industries Cloud <<<<<')
            print('Oferece soluções específicas da indústria, como Health Cloud para saúde e Financial Services'
                  '\nCloud para serviços financeiros.')

        elif op == '9':
            print('\n>>>>> Produto - IoT Cloud <<<<<')
            print('Ajuda as empresas a conectar e monitorar dispositivos da Internet das Coisas (IoT) para'
                  '\ncoletar dados e acionar ações com base nesses dados.')

        elif op == '10':
            print('\n>>>>> Produto - Tableau <<<<<')
            print('A Salesforce adquiriu o Tableau, uma plataforma de análise de dados líder, que oferece'
                  '\nvisualizações avançadas e análise de dados.')

        elif op == '11':
            print('\n>>>>> Produto - MuleSoft <<<<<')
            print('Outra aquisição da Salesforce, a MuleSoft é uma plataforma de integração que facilita a'
                  '\nconexão de sistemas e aplicativos.')

        elif op == '12':
            print('\n>>>>> Produto - Heroku <<<<<')
            print('Uma plataforma de desenvolvimento de aplicativos que permite a criação e hospedagem de'
                  '\naplicativos web e móveis.')

        elif op == '0':
            break
        else:
            print(' Opção inválida, digite novamente.')


def validar_email(email):
    regex_email = r'^[\w\.-]+@[\w\.-]+\.\w+'
    if re.match(regex_email, email):
        return True
    else:
        print('Email inválido, digite novamente ou \'0\' para retornar ao menu anterior. ')
        return False


def validar_nome(nome):
    regex_nome = r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$'
    if re.match(regex_nome, nome):
        return True
    else:
        print('Nome inválido, digite novamente ou \'0\' para retornar ao menu anterior. ')
        return False


def validar_telefone(telefone):
    # aqui vai adicionar somente os números sem os caracteres!
    telefone_limpo = ''.join(filter(str.isdigit, telefone))
    if telefone_limpo.isdigit() and len(telefone_limpo) in (10, 11):
        return True
    else:
        print('Telefone inválido, digite novamente ou \'0\' para retornar ao menu anterior. ')
        return False


def assinar_newsletter():
    print('\n>>>>> ASSINE A NEWSLETTER <<<<<')
    print('Inscreva-se na nossa newsletter para receber conteúdos exclusivos da Salesforce.')

    while True:
        nome = input('Digite seu nome: ')
        if nome == '0':
            return
        elif validar_nome(nome):
            break

    while True:
        email = input('Digite seu e-mail: ')
        if email == '0':
            return
        if validar_email(email):
            break

    with open('contatos-newsletter.json', 'r') as arquivo:
        dados = json.load(arquivo)

        ctt_newsletter = {'nome': nome, 'email': email}
        dados.append(ctt_newsletter)

        with open('contatos-newsletter.json', 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)

    print(f'\nOlá {nome.capitalize()}, a newsletter será enviada com sucesso para o e-mail {email.lower()}\n')


def cadastro_contato():
    print('\n>>>>> CONTATO <<<<<')
    print('Basta preencher o formulário e entraremos em contato o mais rápido possível!')

    while True:
        nome = input('Digite seu nome: ')
        if nome == '0':
            return
        elif validar_nome(nome):
            break

    while True:
        email = input('Digite seu e-mail: ')
        if email == '0':
            return
        elif validar_email(email):
            break

    while True:
        telefone = input('Digite seu telefone: ')
        if telefone == '0':
            return
        if validar_telefone(telefone):
            # armazena o número de telefone sem nenhum caracter
            telefone = ''.join(filter(str.isdigit, telefone))
            break

    empresa = input('Digite o nome da sua empresa: ')
    mensagem = input('Digite sua mensagem: ')

    with open('contatos-formulario.json', 'r') as arquivo:
        dados = json.load(arquivo)

        ctt_formulario = {"nome": nome, "email": email, 'telefone': telefone, 'empresa': empresa,
                          'mensagem': mensagem}
        dados.append(ctt_formulario)

        with open('contatos-formulario.json', 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)

    print(f'\nOlá {nome.capitalize()}, formulário enviado com sucesso!\n')


# executar o programa
menu_principal()
