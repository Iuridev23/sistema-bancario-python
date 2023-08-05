menu = """
Escolha uma opção:
1 - Depositar
2 - Sacar
3 - Imprimir Extrato
0 - Sair

"""

saldo = 0
LIMITE = 500
extrato = ""
LIMITE_SAQUES = 3
contator_saque = 0

while True:
    opcao = input(menu)

    if opcao == "1":
        print("Deposito")
        valor_deposito = float(input("Qual o valor do depósito? "))
        if(valor_deposito >= 0):
            saldo += valor_deposito
            extrato += f"Depósito: {valor_deposito}\n Saldo: {saldo}\n"
        else:
            print("Valor Inválido!")

    elif opcao == "2":
        print("Saque")
        if(contator_saque < 3):
            valor_saque = float(input("Qual o valor a ser sacado? "))        
            if(valor_saque > 0 and valor_saque <= saldo and valor_saque <= LIMITE):
                saldo -= valor_saque
                contator_saque += 1
                extrato += f"Saque: {valor_saque}\n Saldo: {saldo}\n"
            else:
                print("Saldo Insufciente ou Valor Inválido")
        else:
            print("Limite de saques excedido!")
            
    elif opcao == "3":
        print("Extrato")
        print(extrato)

    elif opcao == "0":
        print("Saindo da conta...")
        break    
    else:
        print("Opção inexistente! Selecione outra opção.")




