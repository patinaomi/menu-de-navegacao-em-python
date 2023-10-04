# cores
reset = '\033[0m'
black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
magenta = '\033[35m'
cyan = '\033[36m'


def exibir_menu_principal():
    print(f'===== Bem-vindo a {blue}Salesforce{reset} ====')
    print(f'[{yellow}1{reset}] Página Inicial')
    print(f'[{yellow}2{reset}] Sobre a Salesforce')
    print(f'[{yellow}3{reset}] O que é CRM')
    print(f'[{yellow}4{reset}] Serviços')
    print(f'[{yellow}5{reset}] Formulário de Contato')
    print(f'[{yellow}0{reset}] Sair do Site')
    print('=================================')


def pagina_inicial():
    print('Você está na Página Inicial.')


def sobre_nos():
    print(f'===== {blue}O que é a Salesforce?{reset} =====')
    print('Salesforce é uma empresa de tecnologia de software que é mais conhecida por sua plataforma de\n'
          'gerenciamento de relacionamento com o cliente (CRM), chamada Salesforce CRM. O Salesforce CRM é uma\n'
          'plataforma baseada em nuvem que ajuda as empresas a gerenciar e automatizar várias atividades\n'
          'relacionadas a vendas, marketing, atendimento ao cliente e análise de dados. Ele é projetado para\n'
          'ajudar as empresas a melhorar o envolvimento do cliente, aumentar as vendas e melhorar a eficiência'
          'operacional.')

    retornar_menu_principal()


def produtos():
    print('Veja nossos produtos.')


def contato():
    print('Entre em contato conosco.')


def sair_programa():
    print('Encerrando o programa...')


def retornar_menu_principal():
    while True:
        op = int(input('Digite 1 para retornar ao menu ou 0 para sair do site: '))
        if op == 1:
            exibir_menu_principal()
            break
        else:
            sair_programa()
            break


while True:
    exibir_menu_principal()
    escolha = input("Digite uma opção: ")

    if escolha == "1":
        pagina_inicial()
    elif escolha == "2":
        sobre_nos()
    elif escolha == "3":
        produtos()
    elif escolha == "4":
        contato()
    elif escolha == "0":
        print(f'Obrigado por visitar o nosso site.')
        break
    else:
        print(f'{red}Opção inválida. Por favor, escolha novamente.{reset}')
