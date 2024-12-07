from conta_bancaria.repositorio.conta_repositorio import contas

def listar() -> None:
    print('--- contas cadastradas---')
    for cliente in contas:
        print(f"numero:{cliente['numero']}")
        print(f"nome:{cliente['nome']}")
        print(f"saldo:{cliente['saldo']}")
        print('-'*50)