class ContaBancaria:
    def __init__(self, saldo = 0):
        self.saldo = saldo

    def depositar(self):
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            self.saldo += valor
            print("O valor foi depositado")
        else:
            print("Valor invalido, digite um valor positivo")
        

    def sacar(self):
        valor = float(input("Digite o valor a ser sacado: "))
        if valor > self.saldo:
            print("Valor indisponivel em conta")
        elif valor > 0 and valor < self.saldo:
            self.saldo -= valor
            print("O saque foi feito")
        
    def ver_saldo(self):
        return self.saldo
    
print("----------Bem vindo ao Alencar's Bank----------")
conta = ContaBancaria(500)
opcao = -1
while opcao != 0:
    print("Escolha uma operação")
    opcao = int(input(" [1] Ver Saldo \n [2] Depositar \n [3] Sacar \n [0] Sair"))
    if opcao == 1:
        print("Seu saldo é de:", conta.ver_saldo())
    elif opcao == 2:
        conta.depositar()
    elif opcao == 3:
        conta.sacar()
    elif opcao == 0:
        print("Saindo do sistema...")
        break
    else: 
        print("Opção invalida, Digite novamente")
print("Sistema encerrado.")