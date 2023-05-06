menu = """
[d] -> Depositar
[s] -> Sacar
[e] -> Extrato
[q] -> Sair
"""

limite_saque = 500
numero_saque = 0
saldo = 0
extrato = ["Extrato bancario:\n"]

import os
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
while True:
    operacao = input(menu)

    if operacao == "d":
        deposito = float(input("Deposito: "))
        saldo += deposito
        extrato.append("Deposito de R${:.2f}".format(deposito))
        
    elif operacao == "s":
        if numero_saque < 3:
            saque = float(input("Saque: "))
            if saque <= saldo:
                if saque <= limite_saque:
                    saldo -= saque
                    extrato.append("Saque de R${:.2f}".format(saque))
                    numero_saque += 1
                else:
                    print("O valor esta acima do limite maximo de saque")
            else:
                print("Saque maior que o saldo disponível")
        else:
            print("Numero maximo de saques diarios ja atingido")

    elif operacao == "e":
        clear_terminal()
        
        for item in extrato:
            print(item)
        print("\nSaldo: R${:.2f}".format(saldo))

    elif operacao == "q":
        break

    else:
        print("Operacao invalida")