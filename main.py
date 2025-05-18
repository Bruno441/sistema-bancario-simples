def sacar(valor, saldo):
  extrato = ""

  while True:
    valor = float(input("Informe o valor do depósito: "))
    if valor <= 0:
      print("Valor negativo! Informe um valor positivo para que seja válido.")
    else:
      saldo += valor
      extrato = f"Depósito: R$ {valor}"
      print("Valor depositado com sucesso!")
      break

  return extrato, saldo

def depositar(saldo, limite_diario):
  extrato = ""

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
    extrato = f"Saque: R$ {valor}"
    print("Saque realizado com sucesso!")
  
  return extrato, limite_diario, saldo

def visualizar_historico(extrato, saldo):
    print("Extrato:")
    
    for transacao in extrato:
      print(transacao)
    print(f"Saldo: R$ {saldo}")

def criar_usuario(usuarios):
  count = True

  cpf = input("Para criar um novo usuário precisamos de algumas informações básicas!\nPrimeiro, iremos ver se o seu CPF já está cadastrado no nosso banco de dados.\nQual seu CPF?\n=>")

  while count:
    usuario_encontrado = True
    if usuarios:
      for usuario in usuarios:
        if usuario['cpf'] == cpf:
          print("CPF já cadastrado! Digite um CPF diferente para criar um novo usuário.")
          usuario_encontrado = False
          cpf = input("=>")
          break
    

    if usuario_encontrado:
      count = False
    
  
  nome = input("CPF não cadastrado ainda! Vamos continuar o cadastro.\nQual seu nome?\n=>")
  data_nascimento = input("Qual sua data de nascimento?\n=>")
  endereco = input("Qual seu endereço?\n*Obs: O endereço deve ser passado nas máscara logradouro - bairro - cidade/sigla estado\n=>")
  print("Usuário cadastrado com sucesso!")

  usuario_criado = {
    "cpf": cpf,
    "nome": nome,
    "data_nascimento": data_nascimento,
    "endereco": endereco
  }

  return usuario_criado

def criar_conta_corrente(usuarios, numero_conta, registros_conta_corrente):
  cpf = input("Qual cpf você deseja vincular sua conta corrente?\n=>")

  if usuarios:
    for usuario in usuarios:
      if usuario['cpf'] == cpf:
        opcao_cadastro = input(f"\nCpf encontrado!\n\nUsuário: {usuario['nome']}\n\nDeseja criar a conta corrente para o usuário indicado?\n\n1. Sim\n2. Não\n=>")
        while True:
          if opcao_cadastro == "1":
            json_conta = {
              "agencia": "0001",
              "numero_conta": numero_conta,
              "usuario": usuario
            }

            registros_conta_corrente.append(json_conta)
            numero_conta =+ 1
            print("Usuário criado")
            break
          elif opcao_cadastro == "2":
            print("Conta não criada!")
            break
          else:
            print("Opção inválida!")
  else:
    print("Nenhum cliente cadastro ainda para vincular sua conta corrente.")
    
  return numero_conta, registros_conta_corrente

def main():
  menu = """
  [1] Depositar
  [2] Sacar
  [3] Extrato
  [4] Criar usuário
  [5] Listar usuário
  [6] Criar conta corrente
  [7] Listar contas
  [0] Sair

  =>"""

  saldo = 0
  extrato = []
  limite_diario = 0

  usuarios = []
  registros_conta_corrente = []
  numero_conta = 1

  while True:

    opcao = input(menu)

    if opcao == "1":
      historico, saldo = sacar(opcao, saldo)
      extrato.append(historico)
      
    elif opcao == "2":
      historico, limite_diario, saldo = depositar(saldo=saldo, limite_diario=limite_diario)
      
    elif opcao == "3":
      visualizar_historico(extrato, saldo)

    elif opcao == "4":
      usuario_criado = criar_usuario(usuarios=usuarios)
      usuarios.append(usuario_criado)

    elif opcao == "5":
      print(usuarios)

    elif opcao == "6":
      numero_conta, registros_conta_corrente = criar_conta_corrente(usuarios=usuarios, numero_conta=numero_conta, registros_conta_corrente=registros_conta_corrente)
    elif opcao == "7":
      print(registros_conta_corrente)
    elif opcao == "0":
      break
    else:
      print("Opção inválida!")


if __name__ == "__main__":
  main()