saldo = 1000000

while True:
    print ("\n------------------- BANCO NOOVI  -----------------")
    print("---------- 1    -     VER SALDO         ----------")
    print("---------- 2    - DEPOSITAR DINHEIRO    ----------")
    print("---------- 3    -  SACAR DINHEIRO       ----------")
    print("---------- 4    -       SAIR            ----------")

    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "1":
        print(f"Seu Saldo é: R$ {saldo:.2f}")

    elif opcao == "2":
        deposito = int (input("Digite o valor que você deseja depositar: "))
        
        if deposito <= 0:
            print("Valor invalido!")
        else:
            saldo = saldo + deposito
        print("Depósito realizado com sucesso!")
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "3":
        saque = int(input("Digite o valor que você deseja sacar: "))

        if saldo <= 0:
            print("Saldo insuficiente!")
        else:
            saldo = saldo - saque
            print(f"Saldo atual: R$ {saldo:.2f}")
            print("Saque realizado com sucesso!")
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")




