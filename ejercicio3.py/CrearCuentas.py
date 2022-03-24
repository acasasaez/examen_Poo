from APlazoFijo import APlazoFijo
import CuentaBancaria
from VIP import VIP
import random

class CreadorCuenta():
    __id=1
    def __init__(self, tipodeCuenta,titular):
        self.cuenta = None
        fecha1=CuentaBancaria.escribirfecha()
        fecha2=CuentaBancaria.escribirfecha()
        self.fecha=CuentaBancaria.fechamenor(fecha1,fecha2)
        if(self.fecha==fecha1):
            self.vencimiento=fecha2
        else:
            self.vencimiento=fecha1
        self.numerocuenta=CuentaBancaria.crearnumero()
        self.saldo=10000
        self.negativo=random.randint(1,self.saldo/8)
        if(tipodeCuenta=="CuentaBancaria"):
            self.cuenta=CuentaBancaria.CuentaBancaria(CreadorCuenta.__id,titular,self.fecha,self.numerocuenta,self.saldo)
        elif(tipodeCuenta=="APlazoFijo"):
            self.cuenta=APlazoFijo(CreadorCuenta.__id,titular,self.fecha,self.numerocuenta,self.saldo,self.vencimiento)
        elif(tipodeCuenta=="VIP"):
            self.cuenta=VIP(CreadorCuenta.__id,titular,self.fecha,self.numerocuenta,self.saldo,self.negativo)
        CreadorCuenta.__id+=1
