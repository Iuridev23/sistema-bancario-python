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

while True:
    opcao = input(menu)

    if opcao == 1:
        print("Deposito")
    elif opcao == 2:
        print("Saque")
    elif opcao == 3:
        print("Extrato")
    else:
        print("Opção inexistente! Selecione outra opção.")
