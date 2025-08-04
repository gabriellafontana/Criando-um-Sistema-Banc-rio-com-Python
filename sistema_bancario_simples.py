
menu = """ ======MENU INICIAL =========
        SELECIONE UMA OPÇÃO
      [d] Depositar
      [s] Sacar
      [e] Extrato
      [q] Sair
      ===================
      """

saldo = 0
extrato = " "
limite_saque = 3
numero_saque = 0
limite = 500

while True:

    opcao = input(menu)

    if opcao == "d":
        print("deposito")
        valor = float(input("informe o valor que sera depositado:  "))
        if valor > 0:
            saldo += valor
            extrato += f"Depositos> R$ {valor:.2f}\n"
        else:
            print("operação invalida, valor informado invalido!") 

    elif opcao == "s":
        valor = float(input("informe o valor a ser sacado:  "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= limite_saque

        if excedeu_saldo:
            print("Operação falhou! você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! o valor de saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! numero máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R${valor:.2f}\n"
            numero_saque += 1
        else:
            print("operação falhou! o valor informado é invalido.")
            
    
    elif opcao == "e":
        print("======EXTRATO BANCARIO========")
        print("Não foram realizadas movimentações nesta conta ainda." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("============FIM============")
    
    elif opcao == "q":
        break

    else:
        print ("Opção invalida, favor selecionar novamente a operação desejada")



