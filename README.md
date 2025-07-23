# Sistema Bancário Simples em Python
Este é um sistema bancário de linha de comando simples, desenvolvido em Python, que permite aos usuários realizar operações básicas como depósito, saque e visualização de extrato. O projeto foi criado como um desafio para demonstrar conceitos fundamentais de programação, como laços de repetição, condicionais e manipulação de listas.

## Funcionalidades
### O sistema oferece as seguintes opções ao usuário:

- Depósito: Adiciona um valor ao saldo da conta, com validação para garantir que o valor seja positivo.

- Saque: Permite sacar dinheiro, aplicando validações para:

- Verificar se há saldo suficiente.

- Respeitar um limite máximo por saque.

- Controlar um número máximo de saques diários.

- Extrato: Exibe um histórico de todas as transações (depósitos e saques) realizadas, além do saldo atual da conta.

- Sair: Encerra a aplicação.

### Como Usar
Para executar este sistema bancário em sua máquina, siga os passos abaixo:

Clone o Repositório (ou copie o código diretamente):

- git clone <URL_DO_SEU_REPOSITORIO>

Navegue até o Diretório do Projeto:

- cd <nome_do_diretorio>

Execute o Script Python:

- python banco.py

  
(Certifique-se de que o nome do arquivo Python seja banco.py ou o nome que você salvou.)
Uma vez executado, o programa apresentará um menu no terminal, solicitando que você digite a opção desejada.

### Regras de Negócio

O sistema opera com as seguintes regras pré-definidas:

- Saldo Inicial: A conta começa com um saldo de R$ 5000.00.

- Limite por Saque: O valor máximo que pode ser sacado em uma única operação é de R$ 500.00.

- Limite de Saques Diários: O usuário pode realizar um máximo de 3 saques por dia.

- Depósitos: Apenas valores positivos são aceitos para depósitos.

- Extrato: Exibe o tipo de transação (Depósito ou Saque) e o valor correspondente.

## Estrutura do Código
O código é estruturado de forma procedural, utilizando um loop while True para manter o menu interativo ativo até que o usuário decida sair. As operações são controladas por meio de condicionais (if/elif/else), e as transações são armazenadas em uma lista chamada extrato, onde cada item é um dicionário contendo o tipo e o valor da transação.

saldo = 5000.00 # Saldo inicial da conta

limite = 500    # Limite máximo por saque

extrato = []    # Lista para armazenar as transações

numero_saques = 0 # Contador de saques diários

LIMITE_SAQUES = 3 # Limite máximo de saques por dia

# Loop principal do menu
while True:
    # ... (código do menu e das operações)
###Contribuições

Este projeto é um exemplo básico e pode ser expandido com diversas funcionalidades, como:

- Persistência de dados: Salvar saldo e extrato em um arquivo (TXT, CSV, JSON) para que não sejam perdidos ao encerrar o programa.

- Múltiplos usuários/contas: Implementar um sistema para gerenciar várias contas bancárias.

- Funções: Refatorar o código utilizando funções para cada operação (depósito, saque, extrato) para melhor organização e reusabilidade.

- Tratamento de erros: Adicionar blocos try-except para lidar com entradas inválidas do usuário (ex: digitar texto onde se espera um número).

### Sinta-se à vontade para fazer um fork deste repositório, implementar melhorias e enviar pull requests!
