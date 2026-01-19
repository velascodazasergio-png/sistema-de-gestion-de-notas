import logica

CORTES = ("corte 1", "corte 2", "corte 3")

def main():
    archivo = "notas.txt"

    estudiantes, ids = logica.cargar_datos(archivo)

    while True:
        print("\n--★---GESTION DE NOTAS--★---")
        print("\n--★--- 1. Agregar estudiantes--★---")
        print("\n--★--- 2. Ver reporte--★---")
        print("\n--★---3. Guardar y salir--★---")

        opcion =  int(input('seleccione una opcion'))

        if opcion == 1:
            id_est = input("ID del estudiantes: ")

            if id_est in ids:
                print("Este ID ya esta registrado.")
                continue

            nombre = input("Nombre del estudiante: ")
            notas_temp = []

            for corte in CORTES:
                while True:
                    try:
                        nota = float(input(f"ingrese la nota para el {corte}: "))
                        if nota > 0.0 or nota < 100.0:
                            notas_temp.append(nota)
                            break
                        else:
                            print("la nota debe estar entre 0 y 100")
                    except ValueError:
                        print("entrada no valida. ingrese un numero.")
                    except Exception as e:
                        print(f"ocurrio un error inesperado: {e}")

            nuevo_est = {
                "id": id_est,
                "nombre": nombre,
                "notas": notas_temp
            }

            estudiantes.append(nuevo_est)
            ids.add(id_est)

            print(f"El estudiante {nombre} fue agregado exitosamente.")

        elif opcion == 2:
            estudiantes.sort(key=lambda x: logica.calcular_promedio(x["notas"]), reverse=True)

            print(f"\n{'id':<10} {'nombre':<15} {'PROMEDIO':<10}")
            print("-"*35)

            for est in estudiantes:
                prom = logica.calcular_promedio(est["notas"])
                print(f"{est['id']:<10} {est['nombre']:<15} {prom:.2f}")

        elif opcion == 3:

            logica.guardar_datos(archivo, estudiantes)
            print("saliendo del programa....")
            break

        else:
            print("Opcion no valida. intente nuevamente.")


if __name__ == "__main__":
    main()