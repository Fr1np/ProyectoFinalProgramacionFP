import random

signos = 'abcdefghijklmnopqrstvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ!@$&^&*().,?0123456789'

largo = int(input('Ingrese el largo de su contraseña: '))
num = int(input('Ingrese la cantidad de contraseñas que desea: '))

for pwd in range(num):
    passwd = ''
    for i in range(largo):
        passwd += random.choice(signos)
    print(passwd)