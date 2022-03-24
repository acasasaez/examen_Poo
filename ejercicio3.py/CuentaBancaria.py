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
    
    #Método retirar dinero
    def retirardinero(self,dinero): #Parámetros: dinero = cantidad de dinero en la cuenta bancaria
#Para poder poder retirar x cantidad de dinero necesitamos un método que:
        if (self.saldo>=dinero): #1)Compare si la cantidad de dinero actual en la cuenta, es decir el saldo de la cuenta, sostiene la cantidad de dinero que se quiere retirar
            #en otras palabras, nuestro método debe asegurarse de que la cantidad de dinero que se desea retirar es menor, o como máxmo igual, al saldo de nuestra cuenta. 
            self.saldo=self.saldo-dinero #2) Si la cantidad de dinero que se intenta retirar es menor o igual al saldo, entonces la acción es posible
            #por lo tanto nuestro método recalcula el valor del saldo una vez retirado el dinero.
        else:
            print("Error, quiere retirar más dinero del que tienes") #3)En caso contrario(la cantidad de dinero que se intenta retirar es maayor al saldo) es necesario hacer saber al cliente que el saldo de la cuenta
            # no cuenta con el saldo suficiente, por lo tanto nuestro programa imprime un mensaje de error.

    #Método ingresardinero:
    def ingresardinero(self, dinero): #parámetro: dinero = cantidad de dinero que se desea ingresar
        self.saldo=self.saldo+dinero #como ingresar dinero es una acción que siempre se pede realizar
        #sin ninguna condición, nuestro método simplemente necesita recalcular el valor del saldo una veza ingresada la cantidad de dinero indicada(pasada por parámetro)

    #Método transferir dinero:
#Nuestro nuevo método nos permite hacer transferencias (pasar dinero de una cuenta a otra)
#pero debemos tener en cuenta que eesta es una acción renstringida y por lo tanto debemos tener en cuenta que nuestra cuenta debe cumplir ciertas condiciones
#para poder hacer transferenciaspor lo tanto:
    def transferirdinero(self,dinero,cuenta): 
#Nuestra función juega con 3 elementos fundamentales:
    #Uno de ellos es un atributo y es el saldo disponible de la cuenta
    #Los otros dos debemos pasarlos por parámetros:
        #Por un lado, para poder hacer una transferencia es necesario saber qué cantidad de dinero queremos transferir dinero
        #Por otro lado necesitaremos otra instancia//objeto de nuestra clase CuentaBancaria a la que le haremos la transferencia.
    #Ahora bien, para poder transferir dinero, es necesario que la cantidad de dinero a transferir sea menor, o como máximo igual, al saldo de nuestra cuenta, el caso contrario sería "imposible" (de momento).
    #Por lo tanto nuestro método se encarga de realizar esta comparación:
        if (self.saldo>=dinero):
    #En caso de cumplirse la condición, entonces se realiza la transferencia, por lo tanto:
            self.saldo=self.saldo-dinero #1) El método recalcula el saldo de nuestra cuenta (que habrá disminuido)
            cuenta.saldo=cuenta.ingresardinero(dinero) #2) El método recalculará el saldo de la cuenta a la que realizamos la transferencia (que aumentará)
        else:
            print("Error, quiere transferir más dinero del que tienes") #En caso de que la condición no se cumpla (y la cantidad de dinero que se intenta transferir es mayor al saldo del la cuenta), entonces 
            #La acción de transferir dinero es imposible y por lo tanto el programa se lo comunica al cliente imprimiendo un mensaje de error.

        # Método cuenta:
    #Si tenemos una cuenta bancaria es fundamental poder saber cuál es su saldo, para así hacer un control de los gastos y los ingresos
    #por lo tanto a continuación definimos un método que nos permite comprobar el saldo de nuestra cuenta
    def cuenta(self):
        return "Cuenta bancaria: " + str(self.id) + " Saldo: " + str(self.saldo) # El método nues debvuelve AEl nombre del propietario de la cuenta y el valor del
        #saldo de la misma

#Por otro lado creamos funciones que necesitaremos a lo largo de nuestro ejericio:
#Por un lado, necesitaremos un algoritmo que que calcule si nuestro año es bisisesto no (implementamos la función escribir fechas que habíamos creado)
def esBisiesto(año): #Pasamos por parámetro el año
    Bisiesto=False #Inicialmente nuestro algoritmo toma el valor de false
    if(año%4==0): #En caso de que el año introducido sea un mçmúltiplo de cuatro comprobamos:
        if(año%100==0):#Si el año introducido es múltiplo de 100
            if(año%400==0):#para que nuestro año sea bissiesto necesitamos también quje cumpla la condición de ser múltiplo de cuatro
    
                Bisiesto=True #Bisiesto toma el valor True
        else: #En caso de que nuestro número sea múltiplo de 4 pero no de 100 entonces también será bisiesto
            Bisiesto=True #Bisiesto toma el valor True
        #En otro caso año no cumple ninguna de las condiciones para ser bisiesto, por lo tanto Bisiesto mantiene su valor inicial False
    return Bisiesto #Nos devuelve un Boolean que permite saber si nuestro año es bisisesto o no

#Función escribirfecha:
#Que dará la feche de apertura(fecha aleatoria)
def escribirfecha():
    año=random.randint(2021,2050) #Nuestra fecha toma un valor random para el año 2021 y el 2050
    mes=random.randint(1,12) #Nuestra fecha toma un valor random para el mes, entre el 1 y el 12
    día=0 #El día toma valor 0, es necesario calcularlo en funión del mes y del año en el que estemos
    if(mes==2): # si mes toma valor 2 => Febrero
        if(esBisiesto(año)==True): #Entonces si nuestro año es bisiesto, este mes implementa un día
            #Así que debemos pasar por parámetro el año a la función esBisiesto para que compruebe si estamos en año bisiesto o no
            día=random.randint(1,29) #Si el año es visiesto nuestro día tomará un valor aleatorio entre eçl 1 y el 29
        else:
            día=random.randint(1,28) #Si nuestro año no es bisiesto nuestro día tomará un valor random entre el 1 y el 28
    elif(mes==4 or mes==6 or mes==9 or mes==11): #Por otro lado, si nuestro mes no toma el valor 2, pero toma alguno de los siguientes valores (abril, junio, septiembre o noviembre)
        día=random.randint(1,30) #nuestro valor día solo puede tomar un número aleatorip entre el 1 y el 30, estos meses tienen un máximo de 30 días
    else: # En caso de que nuestro mes no tome ninguno de los valores mencionados (2,4,6,9,11); es decir, nos encontramos en enero, marzo,mayo,julio,agosto, octubre o diciembre
        día=random.randint(1,31) #Entonces nuestro día podrá tomar un valor entre 1 y 31, pues 31 es el máximo de días que contienen estos meses
    fecha=[año,mes,día] #por último, creamos la variable fecha, que será una lista que tome como valores el año, el mes y el día de nuestra fecha
    return fecha # Nuestra función nos devuelve el valor de dicha fecha.
