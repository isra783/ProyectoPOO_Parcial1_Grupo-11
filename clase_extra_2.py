# Integrantes:
# - Collaguari Israel
# - Macias Brithany
# - Suarez Yanina


class GestorTramites:
    # Método polimórfico 1
    def calcular_totales(self, lista_tramites):
        try:
            if not lista_tramites:
                return 0

            total = 0
            for t in lista_tramites:
                total += t.calcular_costo()
            return total

        except AttributeError as e:
            print(f"Error: Uno de los objetos no tiene el método calcular_costo(). {e}")
            return 0
        except TypeError as e:
            print(f"Error de tipo: {e}")
            return 0
        except Exception as e:
            print(f"Error inesperado: {str(e)}")
            return 0

    # Método polimórfico 2
    def generar_reporte(self, lista_tramites):
        try:
            if not lista_tramites:
                print(" No hay trámites para reportar.")
                return

            print("===== REPORTE DE TRÁMITES =====")
            for t in lista_tramites:
                print(t)
            print("================================")

        except Exception as e:
            print(f"Error al generar reporte: {str(e)}")





