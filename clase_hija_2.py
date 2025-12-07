# Integrantes:
# - Collaguari Israel
# - Macias Brithany
# - Suarez Yanina
from clase_base import Tramite

class PermisoFuncionamiento(Tramite):
    def __init__(self, descripcion, costo_base, tipo_negocio):
        # Llamar al constructor padre con prefijo "PF"
        super().__init__(descripcion, costo_base, prefijo="PF")
        self.tipo_negocio = tipo_negocio

    @property
    def tipo_negocio(self):
        return self._tipo_negocio

    @tipo_negocio.setter
    def tipo_negocio(self, valor):
        try:
            if not valor:
                raise ValueError("El tipo de negocio no puede estar vacío.")
            if not isinstance(valor, str):
                raise ValueError("El tipo de negocio debe ser texto.")
            self._tipo_negocio = valor

        except ValueError:
            raise
        except Exception as e:
            raise ValueError(f"Error al procesar el tipo de negocio: {str(e)}")

    # ---- Polimorfismo ----
    def calcular_costo(self):

        "los comerciantes y industrias tiene un recargo adicionado por el tipo de negocio"
        try:
            tipo_lower = self.tipo_negocio.lower()

            if tipo_lower == "comercial":
                return self.costo_base + 50
            elif tipo_lower == "industrial":
                return self.costo_base + 75
            else:
                return self.costo_base

        except Exception as e:
            print(f"Error al calcular costo: {e}")
            return self.costo_base

    def __str__(self):
        return f"[Permiso de Funcionamiento] {self.codigo} - {self.tipo_negocio} - Total: ${self.calcular_costo()}"


# ========== PRUEBAS ==========
if __name__ == "__main__":
    print("=" * 60)
    print("PRUEBA DE LA CLASE PERMISO DE FUNCIONAMIENTO")
    print("=" * 60)

    #  Prueba 1: Crear permisos válidos
    print("\n Creando permisos válidos:")
    try:
        p1 = PermisoFuncionamiento("Tienda de ropa", 100, "comercial")
        print(f"   {p1}")

        p2 = PermisoFuncionamiento("Fábrica textil", 100, "industrial")
        print(f"   {p2}")

        p3 = PermisoFuncionamiento("Oficina administrativa", 100, "otro")
        print(f"   {p3}")
    except ValueError as e:
        print(f"    Error: {e}")

    #  Prueba 2: Tipo de negocio vacío
    print("\n Prueba con tipo de negocio vacío:")
    try:
        p4 = PermisoFuncionamiento("Sin tipo", 100, "")
    except ValueError as e:
        print(f"   Error capturado correctamente: {e}")

    #  Prueba 3: Verificar cálculos
    print("\n Verificando cálculos de costos:")
    permisos = [
        PermisoFuncionamiento("Comercio", 100, "comercial"),
        PermisoFuncionamiento("Industria", 100, "industrial"),
        PermisoFuncionamiento("Otro tipo", 100, "otro"),
    ]

    for p in permisos:
        recargo = p.calcular_costo() - p.costo_base
        print(f"   {p.tipo_negocio}: Base ${p.costo_base} + Recargo ${recargo} = Total ${p.calcular_costo()}")

    print("\n" + "=" * 60)
