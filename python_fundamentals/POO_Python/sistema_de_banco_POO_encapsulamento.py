class Conta:
    def __init__(self,nro_agencia, saldo = 0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self):
        valor = float(input("Digite o valor a ser depositado:"))
        if valor > 0:
            self._saldo += valor
            print("Valor Depositado")
        else:
            print("Digite um valor maior que 0.")

    def sacar(self):
        valor = float(input("Digite o valor a ser sacado:"))
        if valor <= self._saldo:
            self._saldo -= valor
            print("Valor Sacado")
        else:
            print("Este valor não está disponivel em conta.")

    def mostrar_saldo(self):
        return self._saldo

print("---------- Bem Vindo ao Alencar's Bank ----------")
conta = Conta("0001", 100)

opcao = 0
while opcao != 3:
    print("O que deseja fazer hoje?")
    print(" [0] Ver Saldo \n [1] Depositar \n [2] Sacar \n [3] Sair")
    opcao = int(input("Digite sua opção:"))

    if opcao == 0:
        print("Seu saldo é: R$", conta.mostrar_saldo())
        
    elif opcao == 1:
        conta.depositar()
        
    elif opcao == 2:
        conta.sacar()
        
    elif opcao == 3:
        print("Muito obrigado pela preferência, saindo do Sistema")
        break
    else:
        print("Opção invalida, tente novamente")
        




