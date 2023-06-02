import data.usuarios


def retirar_efectivo(user):
    retirar = float(input("\¿Cuanto dinero desea retirar? -> "))
    if retirar > data.usuarios.BALANCE[user]:
        print("\n Saldo insuficiente :(")
    else:
        data.usuarios.BALANCE[user] -= retirar
        print(f"\n El saldo en la cuenta es: {data.usuarios.BALANCE[user]}")
