from clase_extra_1 import Ciudadano
from clase_extra_2 import GestorTramites
from clase_hija_1 import TramiteCedula
from clase_hija_2 import PermisoFuncionamiento


def mostrar_menu():
    """Muestra el menú principal del sistema"""
    print("=" * 50)
    print("SISTEMA MUNICIPAL DE GESTIÓN DE TRÁMITES")
    print("=" * 50)
    print("1. Registrar ciudadano")
    print("2. Crear trámite de cédula")
    print("3. Crear permiso de funcionamiento")
    print("4. Calcular costo total ")
    print("5. Generar reporte ")
    print("6. Mostrar ciudadanos registrados")
    print("7. Salir")
    print("=" * 50)


def main():
    gestor = GestorTramites()
    ciudadanos = []
    tramites = []  # Lista polimórfica

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        # ----------------------------------------------------------
        # 1. Registrar ciudadano
        # ----------------------------------------------------------
        if opcion == "1":
            print("\n--- Registro de ciudadano ---")
            try:
                cedula = input("Ingrese cédula (10 dígitos): ").strip()
                nombre = input("Ingrese apellido y nombre: ").strip()

                ciudadano = Ciudadano(cedula, nombre)
                ciudadanos.append(ciudadano)
                print(f" Ciudadano registrado: {ciudadano}\n")
            except ValueError as e:
                print(f" Error: {e}\n")

        # ----------------------------------------------------------
        # 2. Crear trámite de cédula (código automático)
        # ----------------------------------------------------------
        elif opcion == "2":
            print("\n--- Crear Trámite de Cédula ---")
            try:
                print("\nSeleccione el tipo de trámite:")
                print("1. Cédula nueva")
                print("2. Renovación de cédula")
                while True:
                    opcion_desc= input("Seleccione opción: ").strip()
                    if opcion_desc == "1":
                        descripcion = "Cédula nueva"
                        break
                    elif opcion_desc == "2":
                          descripcion = "Renovación de cédula"
                          break
                    else:
                        print(' Elija una de las opciones válidas (1,o 2')



                costo = float(input("valor a cobrar (ej: 50): ").strip())

                print("\nTipo de trámite:")
                print("1. Primera vez")
                print("2. Renovación (20% descuento)")

                while True:
                    tipo = input("Seleccione una de las opción: ").strip()
                    if tipo == "1":
                        break
                    elif tipo == "2":
                        break
                    else:
                        print('elija una de las opciones validas')

                es_renovacion = True if tipo == "2" else False

                # Código se genera automáticamente
                tramite = TramiteCedula(descripcion, costo, es_renovacion)
                tramites.append(tramite)

                print(f" Trámite registrado: {tramite}\n")
            except ValueError as e:
                print(f" Error: {e}\n")

        # ----------------------------------------------------------
        # 3. Crear permiso de funcionamiento (código automático)
        # ----------------------------------------------------------
        elif opcion == "3":
            print("\n--- Crear Permiso de Funcionamiento ---")
            try:
                descripcion = input("Descripción del negocio: 'ejemplo ; Pasteleria ").strip()
                costo = float(input("valor a cobrar (ej: 100): ").strip())

                print("\nTipo de negocio:")
                print("1. Comercial (+$50)")
                print("2. Industrial (+$100)")
                print("3. Otro (sin recargo)")
                while True:
                    tipo = input("Seleccione opción: ").strip()

                    if tipo == "1":
                        tipo_negocio = "comercial"
                        break
                    elif tipo == "2":
                        tipo_negocio = "industrial"
                        break
                    elif tipo == "3":
                        tipo_negocio = "otro"
                        break
                    else:
                        print(' Elija una de las opciones válidas (1, 2 o 3)\n')


                # Código se genera automáticamente
                tramite = PermisoFuncionamiento(descripcion, costo, tipo_negocio)
                tramites.append(tramite)

                print(f" Trámite registrado: {tramite}\n")
            except ValueError as e:
                print(f" Error: {e}\n")


        # ----------------------------------------------------------
        # 4. Calcular costo total –
        # ----------------------------------------------------------
        elif opcion == "4":
            if not tramites:
                print("\n No hay trámites para calcular.\n")
            else:
                total = gestor.calcular_totales(tramites)
                print(f"\n COSTO TOTAL DE TODOS LOS TRÁMITES: ${total}\n")

        # ----------------------------------------------------------
        # 5. Generar reporte –
        # ----------------------------------------------------------
        elif opcion == "5":
            if not tramites:
                print("\n No hay trámites para generar reporte.\n")
            else:
                gestor.generar_reporte(tramites)
                print()

        # ----------------------------------------------------------
        # 6. Mostrar ciudadanos registrados
        # ----------------------------------------------------------
        elif opcion == "6":
            print("\n--- Ciudadanos registrados ---")
            if not ciudadanos:
                print(" No hay ciudadanos registrados.\n")
            else:
                for i, c in enumerate(ciudadanos, 1):
                    print(f"{i}. {c}")
                print()

        # ----------------------------------------------------------
        # 7. Salir
        # ----------------------------------------------------------
        elif opcion == "7":
            print("\n Gracias por usar el Sistema Municipal de Trámites.")
            print("=" * 50)
            break

        else:
            print(" Opción no válida, intente nuevamente.\n")

if __name__ == "__main__":
    main()


