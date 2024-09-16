import os
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

menu = '''\nEscolha umas das sequintes opcões numéricas:
1- Exibir saldo
2- Depositar
3- Sacar
4- Extrato
0- sair\nOpção escolhida: '''

saldo = 1500
limite_saques = 3
numero_de_saques = 0
extrato = ""



while True:
    menu_escolhido = input(menu)
    limpar()
    if menu_escolhido == '1':
        print(f"Seu saldo atual é de R$ {saldo:.2f}!")
        
    elif menu_escolhido == '2':
        valor_a_depositar = float(input("Digite o valor a ser depositado: "))
        if valor_a_depositar > 0:
            saldo += valor_a_depositar
            extrato += f"Depósito: R$ {valor_a_depositar:.2f}\n"
            print(f"Você depositou R$ {valor_a_depositar:.2f}!")
        else:
            print("Valor inválido! Digite um valor positivo!")
        
    elif menu_escolhido == '3':
        valor_a_sacar = float(input("Digite o valor a ser sacado: "))
        if valor_a_sacar > 0 and valor_a_sacar <= 500 and numero_de_saques < limite_saques and valor_a_sacar <= saldo:
            saldo -= valor_a_sacar
            extrato += f"Saque: R$ {valor_a_sacar:.2f}\n"
            numero_de_saques += 1
            print(f"Saque no valor de R$ {valor_a_sacar:.2f} realizado com sucesso!")
            
        else:
            if valor_a_sacar <= 0:
                print("Valor inválido! Digite um valor positivo!")
            
            elif valor_a_sacar > 500:
                print("Tentativa de saque bloquado. Seu limite por saque é de R$ 500,00!")
            
            elif numero_de_saques >= limite_saques:
                print(f"Tentativa de saque bloquado. Seu número de saques hoje é de {numero_de_saques} e seu limite de quantidade de saques é de {limite_saques}!")
            else:
                print(f"Tentativa de saque bloquado. Seu saldo é de R$ {saldo:.2f}, saque um valor igual ou abaixo!")
                
    elif menu_escolhido == '4':
        print(f'''
\n============ E X T R A T O ============\n
{"Nenhuma operação foi realizada" if not extrato else extrato}

Saldo em conta: R$ {saldo:.2f}
=======================================\n''')
    
    elif menu_escolhido == '0':
        break
    
    else:
        print("Opção inválida, tente novamente!")