from Contacto import Contacto

class Contactotrabajo(Contacto):
    def __init__(self,id, nombreCompleto, email, numero,empresa,instagram):
        super().__init__(id ,nombreCompleto, email, numero)
        self._empresa = empresa
        self._instagram = instagram

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Empresa:{self._empresa}\nInstagram:{self._instagram}\n")
      
    
    @property
    def empresa(self):
        return self._empresa
    @empresa.setter
    def empresa(self, empresa):
        self._empresa = empresa


    @property
    def instagram(self):
        return self._instagram
    @instagram.setter
    def instagram(self, instagram):
        self._instagram = instagram
