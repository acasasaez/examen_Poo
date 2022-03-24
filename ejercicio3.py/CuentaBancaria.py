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
#Creación de setters and getters: Métodos de acceso a los atributos de una clase

#Creamos los "set" que nos permiten modificar el valor de su respectivo atributo
    def setid(self,id):
        self.id=id

    def settitular(self,titular):
        self.titular=titular

    def setFecha(self,fecha):
        self.fecha=fecha

    def setnumerocuenta(self,numerocuenta):
        self.numerocuenta=numerocuenta

    def setsaldo(self,saldo):
        self.saldo=saldo
#Creamos los "get" que nos permiten mostrar el valor de su respectivo atributo
    def getid(self):
        return self.id

    def gettitular(self):
        return self.titular

    def getFecha(self):
        return self.fecha

    def getnumerocuenta(self):
        return self.numerocuenta

    def getsaldo(self):
        return self.saldo