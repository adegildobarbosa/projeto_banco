from conta_bancaria.rules.buscar_conta import get_conta
from conta_bancaria.rules.extrato import criar_extrato

def sacar(numero: int, valor: float)->None:
    conta = get_conta(numero)
    if not conta:
        return None
    
    if valor > conta['saldo']:
        print('saldo insuficiente!')
        return
    
    conta['saldo']-= valor
    transacao = criar_extrato("saque", valor)
    conta['extrato'].append(transacao)
    print('saque realizado com sucesso!')