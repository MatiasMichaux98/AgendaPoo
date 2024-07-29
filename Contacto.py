class Contacto:
    def __init__(self, id=None, nombrecompleto=None, email=None, numero=None, favorito=False):
        self._id = id
        self._nombrecompleto = nombrecompleto
        self._email = email
        self._numero = numero
        self._favorito = favorito

    def mostrar_info(self):
        print(f"ID: {self._id}\nNombre:{self._nombrecompleto}\nEmail:{self._email}\nNúmero:{self._numero}\nFavorito:{self._favorito}")

    @property
    def nombrecompleto(self):
        return self._nombrecompleto
    
    @nombrecompleto.setter
    def nombrecompleto(self,nombrecompleto):
        self._nombrecompleto = nombrecompleto

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, numero):
        self._numero = numero 

    @property
    def favorito(self):
        return self._favorito
    
    @favorito.setter
    def favorito(self, favorito):
        self._favorito = favorito 



        