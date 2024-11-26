conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 2000
cheque = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque):
        print("Saque realizado com cheque especial")
    else:
        print("Saldo insuficiente para saque")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente")
else:
    print("Conta não encontrada, selecione o tipo de conta")