
def simular_banco():
    nome_usu = "Julia Alves"
    num_conta = 109835
    saldo = 10000.00

    print("Bem-Vindo(a) ao nosso Banco SuperBB!")
    print("Escolha qual opção abaixo deseja selecionar: \n[1] - Depositar dinheiro \n[2] - Sacar dinheiro \n[3] - Exibir saldo em conta \n[4] - Sair ")

    while True:

        opcao = int(input("1, 2, 3 ou 4? \nR: "))

        if opcao == 1:
            deposito = float(input("Qual valor deseja depositar em sua conta? \nR: "))
            saldo += deposito
            print(f"O saldo atual da conta {nome_usu}, do número {num_conta} é : {saldo}")
        
        elif opcao == 2:
            while True:
                sacar = float(input("Quando deseja sacar de sua conta? \nR: "))
                if sacar <= saldo:
                    saldo -= sacar
                    print(f"O saldo atual da conta {nome_usu}, do número {num_conta} é : {saldo}")
                    break
                else:
                    print("Você digitou um valor de saque maior que o valor encontrado em sua conta! Tente sacar outro valor.")

        elif opcao == 3:
            print(f"O saldo atual da conta {nome_usu}, do número {num_conta} é : {saldo}")

        elif opcao == 4:
            print("Você decidiu sair do sistema! Bye...")
            break

        else:
            print("Você não escolheu nenhuma opção! Por favor, escolha: ")

simular_banco()