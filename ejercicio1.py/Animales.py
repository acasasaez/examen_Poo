class Animal(): #Clase Animal
    def __init__(self,name): #Cuenta con el atributo name
        self.name=name  #self.name toma el valor de name

class Mamifero(Animal): #Mamífero hereda de la clase animal (métodos y atributos y no son vriados)
    def __init__(self,name):
        Animal.__init__(self,name) 

class Oviparo(Animal): #Mamífero hereda de la clase animal (métodos y atributos y no son vriados)
    def __init__(self,name):
        Animal.__init__(self,name)

class Gato(Mamifero): #La clase gato hereda de la clase mamífero, por lo tanto no solo heredará métodos y atributos de la clase mamífero (que ya heredaba métodos  y atributos de la clase animal)
    def __init__(self,name):
        Mamifero.__init__(self,name)

class Ornitorrinco(Mamifero,Oviparo): #La clase ornitorrinco hereda métodos y atributos de la clase mamífero y de la clase ovíparo, por lo tanto hereda también los métodos y atributos de clase animal
    def __init__(self,name):
        Mamifero.__init__(self,name)
        Oviparo.__init__(self,name)

class Pato(Oviparo):# La clase pato hereda de la clase ovíparo y como consecuencia también de la clase animal
    def __init__(self,name):
        Oviparo.__init__(self,name)
