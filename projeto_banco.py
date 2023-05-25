menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor que será depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Por favor, informe um valor válido.")

    elif opcao == "2":
        valor = float(input("Informe o valor a ser sacado: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não possui saldo suficiente, tente novamente.")
        elif excedeu_limite:
            print("O valor limite de saque foi excedido, entre em contato com seu gerente.")
        elif excedeu_saques:
            print("Número máximo de saques permitido por dia foi excedido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

    elif opcao == "3":
        print("\n================ EXTRATO ==================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")