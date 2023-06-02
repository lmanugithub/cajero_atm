import data.usuarios
import validacion
import menus



def inicio():
    print('\n')
    print('\n')
    print("\t******************************")
    print("\t   Bienvenido a BanManu:)")
    print("\t******************************") 
    print('\tEl banco para tí')
    print("\t***********************") 
    print('\n')
    print('\n')   
    if validacion.validacion()[0]:
        user = validacion.validacion()[1]
        menus.menu_principal(user)        

if __name__=='__main__':
    inicio()