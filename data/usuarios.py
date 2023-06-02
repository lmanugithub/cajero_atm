USUARIOS = {
    'manu':'7548' ,
    'stef':'0613' ,
    'admin':'123'
}
BALANCE ={
    'manu':3000,
    'stef':4500,
    'admin':10000000
}

def palabra_clave(usuario,password):
    i=0
    while i < 3:
        if USUARIOS[usuario] == password:
            return True,USUARIOS[usuario] 
        else:
            password = input('Digite otra vez su contraseña: ')
            i += 1
    return False


def log_in(usuario):
    i = 0
    while i < 3:
        if usuario in USUARIOS.keys():
            return True

        else:
            usuario = input('Digite otra vez su usuario: ')
            i += 1

    return False