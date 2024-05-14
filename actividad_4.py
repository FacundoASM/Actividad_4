tareas = []
n_tarea = 1

def agregar_tarea():

    global n_tarea

    tarea = {}
    tarea['nombre'] = input("\nIngrese el nombre de la tarea: ")
    tarea['descripcion'] = input("Ingrese la descripción de la tarea: ")
    tarea['estado'] = input("Ingrese el estado de la tarea: ")
    tareas.insert(n_tarea, tarea)
    print("Tarea agregada!")
    n_tarea +=1

def mostrar_tareas():
    if not tareas:
        print("\nNo hay tareas para mostrar.")
    else:
        print("\nLista de tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"Tarea {i}:")
            print(f"Nombre: {tarea['nombre']}")
            print(f"Descripción: {tarea['descripcion']}")
            print(f"Estado: {tarea['estado']}")
            print()

def eliminar_tarea():
    if not tareas:
        print("\nNo hay tareas para eliminar.")
    else:
        n_tarea
        print("\nDe las tareas mostradas: ")
        for i, tarea in enumerate(tareas, 1):
            print(f"Tarea {i}:")
            print(f"Nombre: {tarea['nombre']}")
            print(f"Descripción: {tarea['descripcion']}")
            print(f"Estado: {tarea['estado']}")
            print()
        opcion = int(input("Seleccione la que desea eliminar: ")) -1
        if opcion >= 0 and opcion < len(tareas):
            tareas.pop(opcion)
            print("Tarea eliminada correctamente!")
        else:
            print("La tarea no se puede eliminar, porque no existe.")

def main():
    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Eliminar tareas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_tarea()
        elif opcion == '2':
            mostrar_tareas()
        elif opcion == '3':
            eliminar_tarea()
        elif opcion == '4':
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()