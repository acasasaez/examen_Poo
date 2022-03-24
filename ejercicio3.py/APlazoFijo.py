from CuentaBancaria import CuentaBancaria,fechatostring, compararfechas
# A continuación tenemos la clase VIP, una clase heredada de CuentaBancaria, por lo que heredará todos sus atributos y métodos, aunque podrán ser modificados 
class APlazoFijo(CuentaBancaria):
    def __init__(self,id,titular,fecha,numerocuenta,saldo,vencimiento):
        CuentaBancaria.__init__(self,id,titular,fecha,numerocuenta,saldo)
        self.vencimiento=vencimiento
    #La primera modificación la encontramos en sus atributos, y por lo tanto en el constructor.
    #Ahora, en la cuenta a plazo fijo, añadimos un nuevo atributo, vencimiento, que es la fecha a partir de la cuál tú puedes retirar dinero sin sufrir una penalización
    #Por lo tanto, nuestro método retirar dinero es modificado:
    def retirardinero(self,dinero,fechaactual): #ahora cuenta con 2 parámetros
        #Por un lado tenemos el dinero que queremos retirar
        #Por otro, la fecha de ncimiento
        #Expliación: Cuando tenemos una cuentga a plazo fijo no podemos retirar dinero hasta que pase la fecha de vencimiento 
        #si realizásemos esta operación sufriríamos una penalización
        if(compararfechas(fechaactual,self.vencimiento)<0): # Por lo tanto, lo primero que hace  nuestro método es comparar ambas fechas
            #recordando la notación que habíamos empleado y teniendo en cuenta que la fecha de vencimiento es la segunda que pasamos por parámetro, recordamos que nuestro
            #método compararfechas nos devolverá un -1 si la fecha de vencimiento es mayor que la actual, un -1 si la fecha actual es mayor que la de vencimientoy un 0 si son iguales
            dinero=dinero*1.05 #por lo taanto, en caso que nos devuelva -1 quiere decir que estamos dentro de plazo y por lo tanto
            #el retirar dinero conlleva una penalización, por lo tanto el dinero que se retira de la cuenta ya no es el dinero inicial, sino el dinero más la penalización que se lleva el banco
            #por lo tanto es necesario recacular el valor del dinero que se extraerá
        CuentaBancaria.retirardinero(self,dinero) #Lo siguiente es llamar al método retirar dinero de la clase CuentaBancaria, cuyo funcionamiento ya está explicado y que se necargará
        # de devolvernos el resultado deseado.

#intereses de ganancia -------
#En último lugar, el método cuenta también se implementa
    def cuenta(self): 
        cuentastr=CuentaBancaria.cuenta(self) #cuentastr toma el valor del resultado del método cuenta de la clase CuencaBancaria
        return cuentastr + " Cuenta a plazo fijo con vencimento " + fechatostring(self.vencimiento) # Ahora el resultado nos permite revisar, también, la fecha de vencimiento
        #de nuestro plazo fijo