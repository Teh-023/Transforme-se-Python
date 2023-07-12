def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite, "historico": []}
    return conta


def transferir(conta_origem, conta_destino, valor):
    if conta_origem["saldo"] >= valor:
        conta_origem["saldo"] -= valor
        conta_destino["saldo"] += valor
        transacao(conta_origem, "Transferência realizada! {}".format(conta_destino['numero']), -valor)
        transacao(conta_destino, "Transferência recebida! {}".format(conta_origem['numero']), valor)
        print("Transferência de R${}".format(valor), "efetuada com sucesso!")
    else:
        print("Saldo insuficiente na conta de origem.")

def sacar(conta, valor):
    if conta["saldo"] >= valor:
        conta["saldo"] -= valor
        transacao(conta, "Saque", -valor)
        print("Saque de R${}".format(valor), "efetuado com sucesso!")
    else:
        print("Voce não possui saldo suficiente para essa transação.")

def depositar(conta, valor):
    conta["saldo"] += valor
    transacao(conta, "Depósito", valor)
    print("Depósito de R${}".format(valor), "efetuado com sucesso!")

def transacao(conta, tipo, valor):
    transacao = {"tipo": tipo, "valor": valor}
    conta["historico"].append(transacao)

def extrato(conta):
    print("Número da conta: {}".format(conta['numero']))
    print("Titular da conta: {}".format(conta['titular']))
    print("Saldo da conta: R${}".format(conta['saldo']))
    print("Limite da conta: R${}".format(conta['limite']))
    print("-----------------------")

def historico(conta):
    print(f"Extrato {conta['numero']} - {conta['titular']}:")
    for transacao in conta["extrato"]:
        tipo = transacao["tipo"]
        valor = transacao["valor"]
        print(f"Tipo: {tipo}, Valor: {valor}")
    print("-----------------------")



conta1 = cria_conta('145-0', 'Elenice Silva', 5000.0, 80000.0)

conta2 = cria_conta('346-7', 'João Oliveira', 1000.0, 15000.0)

conta3 = cria_conta('278-1', 'Laura Miranda', 4000.0, 45000.0)

transferir(conta1, conta2, 180)

depositar(conta1, 1000.0)

depositar(conta2, 350.0)

depositar(conta3, 290.0)

transferir(conta3, conta1, 700.0)


sacar(conta1, 400.0)

sacar(conta3, 950.0)

transferir(conta2, conta3, 800.0)

sacar(conta2, 60)

print("Extrato da conta 1:")
extrato(conta1)

print("Extrato da conta 2:")
extrato(conta2)

print("Extrato da conta 3:")
extrato(conta3)

print("Histórico da conta 1:")
historico(conta1)

print("Histórico da conta 3:")
historico(conta3)