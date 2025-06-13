class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, valor):
        if valor > 0:
         self.saldo += valor
         print(f"Deposito de R${valor:.2f} realizado com sucesso.")
        else:
         print("Valor de deposito invalido!")

def sacar(self, valor):
   if valor > 0:
    if self.valor >= valor:
       self.saldo -= valor
       print(f"Saque de R${valor:.2f} realizado com sucesso")
    else:
       ("Saldo insuficiente!")
   else:
      ("Valor de saque invalido!")

def exibir_saldo(self):
   print("Saldo atual da conta de {self.titular}: R${self.saldo:.2f}")

def menu():
    nome = input("Digite o nome do titular: ")
    conta = ContaBancaria(nome) 

    while True:
         print("==MENU==")
         print("1.Depositar")
         print("2.Sacar")
         print("3.Exibir Valor")
         print("4.Sair")
         opcao = input("Escolha uma opcao: ")

         if opcao == "1":
            try:
               valor = float(input("Digite o valor para depositar: R$"))
               conta.depositar(valor)
            except ValueError:
               print("Digite um valor valido")
         elif opcao == "2":
            try:
               valor = float(input("Digite o valor para saque: R$"))
               conta.sacar(valor)
            except ValueError:
             print("Digite um valor valido!")
         elif opcao == "3":
            print("Encerrando o sistema.")
            break
         else:
            print("Opcao invalida!")




