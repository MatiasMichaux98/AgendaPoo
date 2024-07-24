class Contacto:
    def __init__(self,id,nombreCompleto,email,numero ):
        self._id = id
        self._nombreCompleto = nombreCompleto
        self._email = email
        self._numero = numero

    def mostrar_info(self):
        print(f"ID: {self._id}\nNombre:{self._nombreCompleto}\nEmail:{self._email}\nNúmero:{self._numero}")

    @property
    def nombreCompleto(self):
        return self._nombreCompleto
    
    @nombreCompleto.setter
    def nombreCompleto(self,nombreCompleto):
        self._nombreCompleto = nombreCompleto

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



        