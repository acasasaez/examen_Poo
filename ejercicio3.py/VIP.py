from CuentaBancaria import CuentaBancaria
# A continuación tenemos la clase VIP, una clase heredada de CuentaBancaria, por lo que heredará todos sus atributos y métodos, aunque podrán ser modificados 
class VIP(CuentaBancaria):
    #La primera modificación la encontramos en el constructor, pues nuestra clase cuenta con un nuevo atributo, negativo, que indicará que cantidad en dinero
    #en negativo, o en deuda, puede tener esl cliente que cuente con este tipo de cuenta
    def __init__(self,id,titular,fecha,numerocuenta,saldo,negativo):
        CuentaBancaria.__init__(self,id,titular,fecha,numerocuenta,saldo)
        self.negativo=negativo
#En consecuencia deberemos crearar el getter y setter de nuestro nuevo atributo
    def setnegativo(self,negativo):
        self.negativo = negativo 

    def getnegativo(self):
        return self.negativo
#Por otro lado al permitir que nuestra cuente con saldo negativo, la condición para retirar dinero y hacer transferencias cambia: 
#Definimos el nuevo método retirar dinero:
#Ahora la cantidad de dinero que queremos retirar podrá ser superior al saldo con el que contamos en la cuenta 
#sin embargo, debe ser menor, o como máximo igual, a la suma del saldo más la cantidad de dinero que se nos permite tener en negativo
# Explicación con ejemplo: SI nosotros tenemos 10 euros en nuestra cuenta y el máximo de dinero que podemos tener en negativo es de 5 euros, entonce podemos retirar 1, 2 , ...., 13,1
# e incluso 15 euros de nuestra cuenta bancaria.
#Sin embargo, si intentamos retirar 16 nuestro banco ya no nos permitiría realizar esta operación
#PÑor lo tanto ahí está la función de nuestro nuevo método
    def retirardinero(self,dinero):
        if(self.saldo+self.negativo>=dinero):# COmprueba que la operación que queremos realizar es posible,poniendo la condición
        # de que la suma entre el saldo y el máximo dinero que podemols tener en negativo sea mayor o igual al dinero que queremos extraer 
            self.saldo=self.saldo-dinero # Si se cumple la condición etonces recalcula nuestro saldo
        else:
            print("Error, el dinero a retirar está fuera de tu limite") #SI no se cumple la condición no se puede realizar la operación y por lo tanto
            #el programa se lo hace saber al clienente mostrándole un mensaje de error

#Con el nuevo método dinerotransferido ocurre exactemente lo mismo:
#El método 
    def transferirdinero(self,dinero,cuenta):
        if (self.saldo+self.negativo>=dinero): # Impone la condición de que el dinero que se desea retirar no puede superar entre la suma entre el saldo y el dinero en negativo
            #si se cumple la condición
            self.saldo=self.saldo-dinero #Entonces recalcula nuestro saldo
            cuenta.saldo=cuenta.saldo+dinero # y también recalcula el nuevo saldo de la cuenta a la que le hemos hecho la transferencia ( cuenta, será también un objeto de clase cuenta bancaia => explicación en la clase principal)

        else:
            print("Error, el dinero a transferir está fuera de tu limite")
            #EN caso contrario, el dinero supera el límite de dinero que se puede extraer de la cuenta y por lo tanto nuestro método imprimirá un mensaje de error para avisar al cliente
            
#Por último modificamos nuestro método cuenta
    def cuenta(self):
        cuentastr=CuentaBancaria.cuenta(self)
        return cuentastr + " Cuenta VIP con limite negativo de " + str(self.negativo)
    #Ahora no solo nos mostrará el nombre y el saldo, sino que también nos mostrará la cantidad de dinero que se nos permite tener en negatrivo.