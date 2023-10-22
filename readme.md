
# Menu de Site Python   
## Descrição
Este é um projeto de uma implementação de um menu de seleção em Python. O menu permite ao usuário escolher uma opção a partir de uma lista de escolhas. Cada opção é associada a uma função correspondente que é executada quando a escolha é feita. Além disso, o projeto inclui a funcionalidade de armazenamento de informações de contato em dois arquivos JSON separados.

## Índice
 * [Descrição](#descrição)
 * [Vídeo](#vídeo)
 * [Funcionalidades](#funcionalidades)
 * [Funções](#funções)
 * [Pilares do Pensamento Computacional](#pilares-do-pensamento-computacional)

## Vídeo
Vídeo da explicação do projeto e o código em execução: [Link no youtube](https://www.youtube.com/watch?v=wS5WSZMN7d8&ab_channel=BrunoCarrilo)


## Funcionalidades:
 -  **Menu de Navegação:** Um menu que permite aos usuários navegar por diferentes seções.
    
-   **Formulário de Contato:** Os usuários podem preencher um formulário de contato com informações, como nome e email.
    
-   **Armazenamento de Contatos:** As informações de contato fornecidas pelos usuários são armazenadas em dois arquivos JSON separados para futura referência.


[:arrow_double_up: voltar ao índice :arrow_double_up: ](#índice)

## Funções

 - **menu_principal()**
A função exibe um menu de opções, permitindo ao usuário fazer uma seleção e, em seguida, retorna a escolha do usuário. Um loop  `while` mantém o menu visível até que o usuário escolha a opção "0" para sair. Se o usuário inserir uma opção inválida, uma mensagem de erro será exibida.

- **sobre_salesforce()**
A função exibe um menu de opções para que o usuário tenha mais informações sobre a empresa Salesforce. Um loop while mantém o menu visível até que o usuário escolha a opção "0" para retornar ao menu principal. Em caso de inserção de uma opção inválida, uma mensagem de erro é exibida.

- **sobre_crm()**
A função apresenta um menu de escolhas para permitir que o usuário obtenha informações adicionais sobre o CRM (Customer Relationship Management). O menu permanece visível até que o usuário opte por retornar ao menu principal, digitando "0". Se o usuário inserir uma escolha que não seja válida, o sistema mostrará uma mensagem de erro.

- **sobre_produtos()**
A função oferece uma visão geral dos produtos da Salesforce. O usuário pode obter detalhes sobre um produto específico digitando "1". O menu permanece disponível até que o usuário retorne ao menu principal com "0", e qualquer escolha inválida resultará em uma mensagem de erro.

- **produto_especifico()**
A função lista os produtos da Salesforce. Se o usuário quiser informações detalhadas sobre um produto específico, pode selecionar a opção desejada na lista. Para retornar ao menu principal, basta digitar "0". Qualquer escolha inválida resultará em uma mensagem de erro.

- **validar_email(email)**
Essa função recebe como parâmetro um endereço de e-mail digitado pelo usuário. Para validação, o e-mail deve conter um "@" e pelo menos um ".". Se a validação for bem-sucedida, a função retorna `True`; caso contrário, retorna `False`.

- **validar_nome(nome)**
Essa função recebe um nome fornecido pelo usuário como parâmetro. Para validar, o nome deve consistir apenas de letras ou conter um único espaço em branco. Se a validação for bem-sucedida, a função retorna `True`; caso contrário, retorna `False`.

- **validar_telefone(telefone)**
Essa função aceita um número de telefone fornecido pelo usuário como parâmetro. Para validar, o número de telefone deve consistir apenas de dígitos e ter um comprimento de até 10 ou 11 caracteres. Se a validação for bem-sucedida, a função retorna `True`; caso contrário, retorna `False`.

- **assinar_newsletter()**
Nessa função, o usuário insere os dados de nome e e-mail. Posteriormente, esses dados são validados utilizando as funções `validar_nome` e  `validar_email`. Se os dados forem validados com sucesso, a função abre um arquivo JSON, cria um dicionário contendo as informações inseridas e adiciona o novo contato à lista de newsletter. Em seguida, a lista atualizada é salva no arquivo JSON.
No entanto, se os dados fornecidos pelo usuário não passarem na validação, uma mensagem de erro é exibida, informando que os dados estão incorretos. Isso assegura que apenas informações válidas sejam incluídas na lista de newsletter.

- **cadastro_contato()**
Nessa função, o usuário fornece informações de nome, e-mail, telefone, empresa e uma mensagem. Após a inserção, esses dados são validados usando as funções `validar_nome`, `validar_email` e `validar_telefone`. Se todos os dados forem validados com sucesso, a função abre um arquivo JSON, cria um dicionário contendo as informações inseridas e adiciona o novo contato à lista de contatos do formulário. A lista atualizada é, então, salva no arquivo JSON.
No entanto, se os dados fornecidos pelo usuário não passarem na validação, uma mensagem de erro é exibida, indicando que os dados estão incorretos. Isso garante que apenas informações válidas sejam incluídas na lista de contatos, mantendo a integridade dos dados.

[:arrow_double_up: voltar ao índice :arrow_double_up:](#índice)



 
## Pilares do Pensamento Computacional   
Os pilares do pensamento computacional são princípios fundamentais que englobam habilidades essenciais para enfrentar desafios complexos e desenvolver soluções eficazes no campo da ciência da computação. A seguir, destacaremos como esses quatro pilares foram aplicados no código:  
  
#### Decomposição:  
A decomposição é a divisão de um problema complexo em partes menores, traduzida na **fragmentação de um programa em funções menores**. Isso facilita a manutenção, depuração e desenvolvimento colaborativo, permitindo que várias pessoas trabalhem em partes distintas do código independentemente.  
  
#### Reconhecimento de Padrões:  
O Reconhecimento de Padrões é a identificação de tendências em dados e problemas, frequentemente usado para simplificar processos complexos e encontrar **soluções reutilizáveis** em códigos para problemas semelhantes.  
#### Abstração:  
A abstração é a simplificação de problemas, eliminando detalhes desnecessários, geralmente **encapsulando comportamentos em funções para criar interfaces mais simples e legíveis** . É uma técnica crucial para simplificar a complexidade e facilitar a reutilização de código no desenvolvimento de software.   
#### Algoritmo:  
Algoritmos são conjuntos de instruções que resolvem problemas específicos, servindo como base para a resolução de problemas na ciência da computação, descrevendo os passos necessários para realizar tarefas ou cálculos.

[:arrow_double_up: voltar ao índice :arrow_double_up: ](#índice)
