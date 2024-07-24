from Contacto import Contacto

class Contactopersonal(Contacto):
    def __init__(self,id,nombreCompleto, email, numero,pais,genero):
        super().__init__(id,nombreCompleto, email,numero)
        self._pais = pais
        self._genero = genero

    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Pais:{self._pais}\nGenero:{self._genero}\n")
    

    @property
    def pais(self):
        return self._pais 
    @pais.setter
    def pais(self, pais):
        self._pais = pais

    
    @property
    def genero(self):
        return self._genero
    @genero.setter
    def genero(self, genero):
        self._genero = genero
    