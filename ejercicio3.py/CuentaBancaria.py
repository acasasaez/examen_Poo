import random

#Creación de la clase principa o clase padre "CuentaBanciaria", que a través de herencia y agregaciones nos permitirá definir los distintos tipos de cuentas bancarias
class CuentaBancaria():
#Creamlos nuestro constructor, de parámetros "id", "titular", "fecha","numerocuenta", "saldo"
    def __init__(self,id,titular,fecha,numerocuenta,saldo): 
        self.id=id # self.id toma el valor de id
        self.titular=titular #self.titular toma el valor de titular
        self.fecha=fecha #self.fecha toma el valor de fecha
        self.numerocuenta=numerocuenta #self.numerocuenta toma el valor de numerocuenta
        self.saldo=saldo #self.saldo toma el valor de saldo
