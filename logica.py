def calcular_promedio(notas):
    if not notas:
        return 0.0
    
    return sum(notas)/len(notas)


def cargar_datos(nombre_archivo):
    estudiantes = []

    idss_registrados = set()

    try:
        with open(nombre_archivo,"r",encoding="utf-8")as archivo:
            """ID,NOMBRE,NOTA1,NOTA2,NOTA3"""
            for linea in archivo:
                partes = linea.strip().split(",")

                if len(partes) >= 2:
                    id_est = partes[0]
                    nombre = partes[1]
                    notas = [float(n) for n in partes[2:]]

                    estudiantes ={
                        "id": id_est,
                        "nombre": nombre,
                        "notas": notas,
                    }

                    estudiantes.append(estudiantes)
                    idss_registrados.add(id_est)
    except FileExistsError:
        print("archivo no encontrado. se creara uno nuevo al guardar")
    except ValueError:
        print("error en el formato en el archivo.")
    except Exception as e:
        print(f"ocurrio un error inesperado: {e}")

        return estudiantes, idss_registrados
    

def guardar_datos(nombre_archivo, estudiantes):
    try: 
        with open (nombre_archivo, "w") as archivo:
            for est in estudiantes:
                notas_str = ",".join([str(n) for n in est["notas"]])
                archivo.write(f"{est['id']}, {est['nombre']}, {notas_str}")
                print("Datos guardados exitosamente")
    except Exception as e:
        print(f"error al guardar: {e}")
"""nota: 50"""
"""nota2: 20"""
"""nota3: 70"""
"""total:140/3"""