menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=>"""

saldo = 0
extrato = []
limite_diario = 0

while True:

  opcao = input(menu)

  if opcao == "1":

    while True:
      valor = float(input("Informe o valor do depósito: "))
      if valor <= 0:
        print("Valor negativo! Informe um valor positivo para que seja válido.")
      else:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor}")
        print("Valor depositado com sucesso!")
        break
  elif opcao == "2":
    valor = float(input("Informe o valor do saque: "))
    if valor <= 0:
      print("Valor negativo! Informe um valor positivo para que seja válido.")
    elif valor > saldo:
      print("Saldo insuficiente!")
    elif valor > 500:
      print("Valor acima do limite diário!")
    elif limite_diario >= 3:
      print("Limite diário de saques atingido!")
    else:
      saldo -= valor
      limite_diario += 1
      extrato.append(f"Saque: R$ {valor}")
      print("Saque realizado com sucesso!")
  elif opcao == "3":
    print("Extrato:")
    
    for transacao in extrato:
      print(transacao)
    print(f"Saldo: R$ {saldo}")
  elif opcao == "0":
    break
  else:
    print("Opção inválida!")
