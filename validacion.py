import data.usuarios

def validacion():
    user = input('\n Digite su usuario: ')
    if data.usuarios.log_in(user):
        secret=input('Ahora digite su PassWord: ')
        if data.usuarios.palabra_clave(user,secret)[0]:
            return True,user
        else:
            return False
    else:
        print('\nGracias por confiar en nosostros')
        return False
if __name__=='__main__':
    pass