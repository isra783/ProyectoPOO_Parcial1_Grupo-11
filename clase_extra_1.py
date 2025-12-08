# Integrantes:
# - Collaguari Israel
# - Macias Brithany
# - Suarez Yanina

class Ciudadano:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, valor):
        try:
            if not valor:
                raise ValueError("La cédula no puede estar vacía.")
            if not isinstance(valor, str):
                raise ValueError("La cédula debe ser un texto.")
            if len(valor) != 10:
                raise ValueError("La cédula debe tener exactamente 10 dígitos.")
            if not valor.isdigit():
                raise ValueError("La cédula debe contener solo números del 0 al 9.")

            self._cedula = valor

        except Exception as e:
            raise ValueError(f"Error al procesar la cédula: {str(e)}")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor:
            raise ValueError("El nombre no puede estar vacío.")
        if not isinstance(valor, str):
            raise ValueError("El nombre debe ser un texto.")
        self._nombre = valor

    def __str__(self):
        return f"Ciudadano {self.nombre} - Cédula: {self.cedula}"

if __name__ == "__main__":

    c1 = Ciudadano("1234567890", "Juan Pérez")  # Correcto
print(c1)

   # c2 = Ciudadano("123", "Ana López")
 #  c3 = Ciudadano("12345678901", "Pedro Gómez")
  #  c4 = Ciudadano("123456789a", "María Torres")
   # c5 = Ciudadano("12-3456789", "Luis Ramírez")
    #c6 = Ciudadano("", "Carlos Ruiz")