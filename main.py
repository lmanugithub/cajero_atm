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
    if validacion.validacion():
        menus.menu_principal()        

if __name__=='__main__':
    inicio()