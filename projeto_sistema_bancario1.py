menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""            # o extrato é uma string
numero_saques = 0       # o número de saques começa zerado
LIMITE_SAQUES = 3       # uma constante aqui!

# abaixo o while loop infinito
while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Operação inválida. Favor digitar um valor válido.")       # tem que verificar SE TEM saldo para fazer a operação e se cabe no LIMITE DIÁRIO: 500!
    
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))

        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saque_excedido = numero_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print("Não é possível efetuar o saque. Saldo insuficiente.")
        elif limite_excedido:
            print("Não é possível efetuar o saque. Limite insuficiente.")
        elif saldo_excedido:
            print("Não é possível efetuar o saque. Limite de saques excedidos.")
        elif valor> 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
        else:
            print("Não é possível efetuar o saque. Favor digitar um valor válido.")

    elif opcao == "3":
        print("\n~~~~~~~~~~~ EXTRATO ~~~~~~~~~~~")
        print("Nenhuma movimentação foi realizada."if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")