# Integrantes:
# - Collaguari Israel
# - Macias Brithany
# - Suarez Yanina
from clase_base import Tramite


class TramiteCedula(Tramite):
    def __init__(self, descripcion, costo_base, es_renovacion):
        # Llamar al constructor padre con prefijo "CED"
        super().__init__(descripcion, costo_base, prefijo="CED")
        self.es_renovacion = es_renovacion

    @property
    def es_renovacion(self):
        return self._es_renovacion

    @es_renovacion.setter
    def es_renovacion(self, valor):
        try:
            if not isinstance(valor, bool):
                raise ValueError("es_renovacion debe ser booleano (True o False).")
            self._es_renovacion = valor

        except ValueError:
            raise
        except Exception as e:
            raise ValueError(f"Error al procesar es_renovacion: {str(e)}")

    # ---- Polimorfismo ----
    def calcular_costo(self):
        """Calcula el costo: renovación tiene 20% de descuento"""
        try:
            if self.es_renovacion:
                return self.costo_base * 0.8  # 20% descuento
            return self.costo_base  # Precio completo

        except Exception as e:
            print(f"Error al calcular costo: {e}")
            return self.costo_base

    def __str__(self):
        tipo = "Renovación" if self.es_renovacion else "Primera vez"
        return f"[Cédula] {self.codigo} - {tipo} - Total: ${self.calcular_costo()}"


# ========== PRUEBAS ==========
if __name__ == "__main__":
    print("=" * 60)
    print("PRUEBA DE LA CLASE TRAMITE CEDULA")
    print("=" * 60)

    # ✅ Prueba 1: Crear cédulas válidas
    print("\n✅ Creando trámites de cédula válidos:")
    try:
        c1 = TramiteCedula("Cédula nueva", 50, False)
        print(f"   {c1}")

        c2 = TramiteCedula("Renovación de cédula", 50, True)
        print(f"   {c2}")

        c3 = TramiteCedula("Cédula por pérdida", 50, False)
        print(f"   {c3}")
    except ValueError as e:
        print(f"   ❌ Error: {e}")

    # ❌ Prueba 2: Valor no booleano
    print("\n❌ Prueba con valor no booleano:")
    try:
        c4 = TramiteCedula("Cédula inválida", 50, "si")
    except ValueError as e:
        print(f"   Error capturado correctamente: {e}")

    # ✅ Prueba 3: Verificar descuento en renovación
    print("\n✅ Verificando descuento del 20% en renovación:")
    cedulas = [
        TramiteCedula("Primera vez - Base $50", 50, False),
        TramiteCedula("Renovación - Base $50", 50, True),
        TramiteCedula("Primera vez - Base $100", 100, False),
        TramiteCedula("Renovación - Base $100", 100, True),
    ]

    for c in cedulas:
        tipo = "Renovación" if c.es_renovacion else "Primera vez"
        descuento = " (20% desc.)" if c.es_renovacion else ""
        print(f"   {tipo}: Base ${c.costo_base} → Total ${c.calcular_costo()}{descuento}")

    print("\n" + "=" * 60)
