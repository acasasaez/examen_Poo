class Libro():
    def __init__(self,titulo,autor,fecha,editorial,ISBN):
        self.titulo=titulo
        self.autor=autor
        self.fecha=fecha
        self.editorial=editorial
        self.ISBN=ISBN

    def setTitulo(self,titulo):
        self.titulo=titulo

    def setAutor(self,autor):
        self.autor=autor

    def setFecha(self,fecha):
        self.fecha=fecha

    def setEditorial(self,editorial):
        self.editorial=editorial

    def setISBN(self,ISBN):
        self.ISBN=ISBN

    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor

    def getFecha(self):
        return self.Fecha

    def getEditorial(self):
        return self.editorial

    def getISBN(self):
        return self.ISBN
