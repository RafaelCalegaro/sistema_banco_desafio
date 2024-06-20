#Exibe o menu de opções
menu = """
Escolha umas das opções abaixo:
    [d] - Depósito
    [s] - Saque
    [e] - Extrato
    [x] - Sair
"""

#Parâmetros iniciais
saldo = 0
saque_maximo = 500
extrato = ""
saques_realizados = 0
LIMITE_SAQUES = 3

#cria o loop
while True:

    opcao_escolhida = input(menu)  #exibe o menu para o usuário

    #Lógica da opção "Depósito" - [d]
    if opcao_escolhida == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Operação falhou! O Valor informado é inválido!")


    #Lógica da opção "Saque" - [s]
    elif opcao_escolhida == "s":
        valor = float(input("Informe o valor do saque: "))


        saldo_insuficiente = valor > saldo

        saque_maximo_execedido = valor > saque_maximo

        excedeu_limite_saques = saques_realizados >= LIMITE_SAQUES


        if saldo_insuficiente:
            print("Operação Falhou! Saldo Insuficiente!")

        elif saque_maximo_execedido:
            print("Operação Falhou! Saque maior que o permitido! (Valor máximo: R$ 500)")

        elif excedeu_limite_saques:
            print("Operação Falhou! Você atingiu o número máximo de saques diário!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            saques_realizados += 1

        else:
            print("Operação Falhou! O valor informado não é válido!")


#Lógica da opção "Extrato" - [s]
    elif opcao_escolhida == "e":
        print("\n============== EXTRATO ================")
        print("Sem movimentações." if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}")
        print("\n=======================================")

    elif opcao_escolhida == "x":
        break
            
    else:
        print("Opção inválida! Escolha uma das opções do menu!")
