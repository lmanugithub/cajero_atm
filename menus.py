from consultar import consultar_saldo
import retirar
import depositar
import data.usuarios



def menu_principal(user):
    
    while True:
        print ('''*********ATM SIMULACION BANCARIO*************\n''')
        print ('Selecciona la Opcion que deseas?\n')
        print ('1.- Consultar Saldo')
        print ('2.- Retirar Efectivo')
        print ('3.- Depositar a Cuenta')
        print ('4.- SALIR \n')
        print ('************************************************')

        opcion=int(input('Seleciona la Opcion que deseas:'))

        if (opcion==1):
            consultar_saldo(user)

        elif (opcion==2):
            retirar.retirar_efectivo(user)

        elif (opcion==3):
            depositar.depositar_cuenta()

        elif(opcion==4):
            print("Finalizando...Cerrando Aplicacion")
            break
        else:
            print("Ese numero de Opcion no existe.. Intente de nuevo")