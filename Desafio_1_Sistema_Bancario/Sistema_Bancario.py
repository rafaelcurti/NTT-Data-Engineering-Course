menu = """

=== Bem vindo ao Banco Python! ===

[s] Sacar
[d] Depositar
[e] Extrato
[q] Sair

==================================
=> """

saldo = 0
vlr_limite_saque = 500
extrato = ""
qtde_saques = 0
LIM_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "s":
        valor = float(input("Digite o valor do saque: "))

        saldo_excedido = valor > saldo

        limite_excedido = valor > vlr_limite_saque

        nr_saques_excedidos = qtde_saques >= LIM_SAQUES

        if saldo_excedido:
            print("Operação não realizada! Saldo suficiente.")

        elif limite_excedido:
            print(f"Operação não realizada! O valor do saque excede o limite diário (R${vlr_limite_saque:.2f}).")

        elif nr_saques_excedidos:
            print("Operação não realizada! Você atingiu o número máximo de saques.")

        #Verifica se o valor de saque é maior que zero e adiciona no extrato o valor informado
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            qtde_saques += 1
            print(f"Saque realizado com sucesso no valor de R${valor:.2f}")
        else:
            print("Operação não realizada! O valor informado é inválido.")

    elif opcao == "d":
        valor = float(input("Digite o valor do depósito: "))

        #Verifica se o valor depositado é maior que zero e adiciona no extrato o valor informado
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            print(f"Depósito realizado com sucesso no valor de R${valor:.2f}")
        else:
            print("Operação não realizada! O valor informado é inválido.")

    elif opcao == "e":
        cabecalho_ext = ' EXTRATO '
        print(cabecalho_ext.center(42, "="),"\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}\n")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor selecione uma opção válida.")