from Contacto import Contacto

class ContactoTrabajo(Contacto):
    def __init__(self, nombreCompleto, email, numero,empresa,instagram):
        super().__init__(nombreCompleto, email, numero)
        self._empresa = empresa
        self._instagram = instagram

    def mostrar_info(self):
        super().mostrar_info()
        print("empresa", self._empresa,
              "instagram",self._instagram)
    
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
