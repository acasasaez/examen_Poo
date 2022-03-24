import random
def crearnumero():
    numero=0#Inicialemnte nuestro número de cuenta será 0
    for i in range(0,13): #Creamos un bucle donde i toma valores del 0 al 13
        num=random.randint(0,9)
        numero+=(num*10)
    return numero
print (crearnumero())
    

