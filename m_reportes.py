
#Metodo que realiza la opcion 1 (consulta de tareas por estado)
def metodo_1 (info):
    print("Ingrese la opcion segun el estado de las tareas que desea consultar:\n(1) Pendientes\n(2) En progreso\n(3) Completadas")
    op = input("Opciones (1/2/3): ")
    print("\n*****lista*****")
    if op == "1":
        for proyecto in info:
            for tarea in proyecto.tareas:
                if tarea.estado == "Pendiente":
                    print(str(tarea.id) +"\n"+ tarea.nombre +"\n"+ tarea.empresa_cliente +"\n"+ tarea.descripcion +"\n"+ str(tarea.fecha_inicio) +"\n"+ str(tarea.fecha_vencimiento) +"\n"+ tarea.estado +"\n"+ str(tarea.porcentaje))


#Menu de opciones del modulo de reportes
def menu_reportes(info):
    print("*****Menu de opciones*****\n(1) Consulta de Tareas por estado\n(2) Filtrar las tareas por fecha\n(3) filtrar los proyectos por fecha de inicio, vencimiento, estado o empresa\n(4) Listar subtareas segun nombre o id del proyecto")
    opcion = input("Opciones (1/2/3/4): ")
    if opcion == "1":
        metodo_1(info)
    #elif opcion == "2":
    
    #elif opcion == "3":
    
    #elif opcion == "4":

    else:
        print("Opcion escogida no es valida")
