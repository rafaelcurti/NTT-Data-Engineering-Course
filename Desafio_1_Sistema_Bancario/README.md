
# DIO | NTT DATA | Desafio 1

Criar um Sistema Bancário simples

## 📒 Objetivo Geral
Criar um sistema bancário com as operações sacar, depositar e visualizar extrato.

## 💻 Desafio
Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso excolheu a linguagem Python. Para a primeira versão do sistema devemos implementar 3 operações: depósito, saque e extrato.

| Operação de depósito |
|----------|
**Requisito** - Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato


| Operação de saque |
|----------|
**Requisito** - O sistema deve permitir realizar 3 saques diários com limite máxiumo de R$500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.


| Operação de extrato |
|----------|
**Requisito** - Essa operação deve listar todos os depósitos e saques realizados na conta bancária. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações. Os Valores devem ser exibidos utilizando o formato R$ xxx.xx. Exemplo: 1500.45 = R$ 1500.45

