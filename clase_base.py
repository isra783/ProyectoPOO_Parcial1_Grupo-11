# Integrantes:
# - Collaguari Israel
# - Macias Brithany
# - Suarez Yanina
#clase principal para realizar tramites
class Tramite:
# Contador de clase (compartido entre todas las instancias)
    _contador = 0

    def __init__(self, descripcion, costo_base, prefijo="TRM"):
        # Generar código automático
        Tramite._contador += 1
        codigo_auto = f"{prefijo}{Tramite._contador:04d}"  # TRM0001, TRM0002, etc.

        self.codigo = codigo_auto
        self.descripcion = descripcion
        self.costo_base = costo_base

    # ---- Encapsulamiento ----
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        try:
            if not valor:
                raise ValueError("El código no puede estar vacío.")
            self._codigo = valor

        except ValueError:
            raise
        except Exception as e:
            raise ValueError(f"Error al procesar el código: {str(e)}")

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor):
        try:
            if not valor:
                raise ValueError("La descripción no puede estar vacía.")
            self._descripcion = valor

        except ValueError:
            raise
        except Exception as e:
            raise ValueError(f"Error al procesar la descripción: {str(e)}")

    @property
    def costo_base(self):
        return self._costo_base

    @costo_base.setter
    def costo_base(self, valor):
        try:
            # Validar que sea numérico
            if not isinstance(valor, (int, float)):
                raise ValueError("El costo base debe ser un número.")

            # Validar que no sea negativo
            if valor < 0:
                raise ValueError("El costo base no puede ser negativo.")

            self._costo_base = valor

        except ValueError:
            raise
        except Exception as e:
            raise ValueError(f"Error al procesar el costo base: {str(e)}")

    # ---- Métodos a sobrescribir (polimórficos) ----
    def calcular_costo(self):
        return self.costo_base

    def __str__(self):
        return f"Trámite {self.codigo}: {self.descripcion} - Costo base: ${self.costo_base}"



if __name__ == '__main__':
    print("=" * 50)
    print("PRUEBA DE LA CLASE TRAMITE")
    print("=" * 50)

    #  Prueba 1: Crear trámites válidos
    print("\nCreando trámites válidos:")
    try:
        t1 = Tramite("Certificado de residencia", 25)
        print(f"   {t1}")
        print(f"   Costo calculado: ${t1.calcular_costo()}")

        t2 = Tramite("Permiso de construcción", 150.50, prefijo="PC")
        print(f"   {t2}")

        t3 = Tramite("Licencia ambiental", 200, prefijo="LA")
        print(f"   {t3}")
    except ValueError as e:
        print(f"    Error: {e}")

    #  Prueba 2: Descripción vacía
    print("\n Prueba con descripción vacía:")
    try:
        t4 = Tramite("", 50)
    except ValueError as e:
        print(f"   Error capturado correctamente: {e}")

    #  Prueba 3: Costo negativo
    print("\n Prueba con costo negativo:")
    try:
        t5 = Tramite("Trámite inválido", -100)
    except ValueError as e:
        print(f"   Error capturado correctamente: {e}")

    #  Prueba 4: Costo no numérico
    print("\n Prueba con costo no numérico:")
    try:
        t6 = Tramite("Trámite inválido", "cincuenta")
    except ValueError as e:
        print(f"   Error capturado correctamente: {e}")

    #  Prueba 5: Verificar códigos únicos
    print("\n Verificando generación de códigos únicos:")
    tramites = []
    for i in range(5):
        t = Tramite(f"Trámite de prueba {i + 1}", 10 + (i * 5))
        tramites.append(t)
        print(f"   {t.codigo} - {t.descripcion}")

    #  Prueba 6: Modificar atributos con setters
    print("\n Modificando atributos con setters:")
    try:
        t7 = Tramite("Trámite original", 100)
        print(f"   Antes: {t7}")

        t7.descripcion = "Trámite modificado"
        t7.costo_base = 120
        print(f"   Después: {t7}")
    except ValueError as e:
        print(f"    Error: {e}")

    print("\n" + "=" * 50)
    print("FIN DE LAS PRUEBAS")
    print("=" * 50)



