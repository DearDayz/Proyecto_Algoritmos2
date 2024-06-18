from datetime import datetime


#validaciones
def verifica_formato_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
      
def es_entero(cadena):
    try:
        int(cadena)
        return True
    except ValueError: 
        return False
    

#Metodo que realiza la opcion 1 (consulta de tareas por estado)
def metodo_1 (info):
    print("Ingrese la opcion segun el estado de las tareas que desea consultar:\n(1) Pendientes\n(2) En progreso\n(3) Completadas")
    op = input("Opciones (1/2/3): ")
    while op!="1" and op!="2" and op!="3":
        op=input("Ingrese correctamente su opcion: ")
    print("\n*****lista*****")
    if op == "1":
        for proyecto in info:
            for tarea in proyecto.tareas:
                if tarea.estado == "Pendiente":
                    print(str(tarea.id) +"\n"+ tarea.nombre +"\n"+ tarea.empresa_cliente +"\n"+ tarea.descripcion +"\n"+ str(tarea.fecha_inicio) +"\n"+ str(tarea.fecha_vencimiento) +"\n"+ tarea.estado +"\n"+ str(tarea.porcentaje))
    elif op == "2":
        for proyecto in info:
            for tarea in proyecto.tareas:
                if tarea.estado == "En progreso":
                    print(str(tarea.id) +"\n"+ tarea.nombre +"\n"+ tarea.empresa_cliente +"\n"+ tarea.descripcion +"\n"+ str(tarea.fecha_inicio) +"\n"+ str(tarea.fecha_vencimiento) +"\n"+ tarea.estado +"\n"+ str(tarea.porcentaje))
    elif op == "3":
        for proyecto in info:
            for tarea in proyecto.tareas:
                if tarea.estado == "Completada":
                    print(str(tarea.id) +"\n"+ tarea.nombre +"\n"+ tarea.empresa_cliente +"\n"+ tarea.descripcion +"\n"+ str(tarea.fecha_inicio) +"\n"+ str(tarea.fecha_vencimiento) +"\n"+ tarea.estado +"\n"+ str(tarea.porcentaje))
    menu_reportes(info)

#Metodo que realiza la opcion 2 (filtrar las tareas por fecha de inicio, fecha de vencimiento u otras fechas relevantes.)
def metodo_2 (info):
    print("Filtrar por:\n(1) Fecha de incio\n(2) Fecha de vencimiento")
    filtrar = input("Opciones (1/2): ")
    while filtrar!="1" and filtrar!="2":
        filtrar = input("Ingrese correctamente su opcion: ")
    print("Especifique si quiere filtrar segun:\n(1) Un rango de fechas\n(2) Fechas anteriores a otra\n(3) Fechas posteriores a otra\n")
    opcion = input("Opciones (1/2/3): ")
    while opcion!="1" and opcion!="2" and opcion!="3":
        opcion = input("Ingrese correctamente su opcion: ")
    if opcion == "2" or opcion == "3":
        fecha = input("Ingrese la fecha con el formato ano-mes-dia: ")
        while not(verifica_formato_fecha(fecha)):
            fecha = input("Ingrese correctamente la fecha con el formato ano-mes-dia: ")
        fechar = datetime.strptime(fecha,"%Y-%m-%d")
        #Fechas anteriores a...
        if opcion == "2":
            #...fechas de incio de las tareas.
            if filtrar == "1":
                print("*****Lista de tareas segun sus fechas de inicio anteriores a "+fecha+"*****")
                for proyecto in info:
                    for tarea in proyecto.tareas:
                        if tarea.fecha_inicio < fechar:
                            print(str(tarea.id) +"\n"+ tarea.nombre +"\n"+ tarea.empresa_cliente +"\n"+ tarea.descripcion +"\n"+ str(tarea.fecha_inicio) +"\n"+ str(tarea.fecha_vencimiento) +"\n"+ tarea.estado +"\n"+ str(tarea.porcentaje)+"\n")
            #...fechas de vencimiento de las tareas
            else:
                print("*****Lista de tareas segun sus fechas de vencimiento anteriores a "+fecha+"*****")
                for proyecto in info:
                    for tarea in proyecto.tareas:
                        if tarea.fecha_vencimiento < fechar:
                            print(str(tarea.id) +"\n"+ tarea.nombre +"\n"+ tarea.empresa_cliente +"\n"+ tarea.descripcion +"\n"+ str(tarea.fecha_inicio) +"\n"+ str(tarea.fecha_vencimiento) +"\n"+ tarea.estado +"\n"+ str(tarea.porcentaje)+"\n")
        #Fechas posteriores a...
        else:
            #...fechas de incio de las tareas.
            if filtrar == "1":
                print("*****Lista de tareas segun sus fechas de inicio anteriores a "+fecha+"*****")
                for proyecto in info:
                    for tarea in proyecto.tareas:
                        if tarea.fecha_inicio < fechar:
                            print(str(tarea.id) +"\n"+ tarea.nombre +"\n"+ tarea.empresa_cliente +"\n"+ tarea.descripcion +"\n"+ str(tarea.fecha_inicio) +"\n"+ str(tarea.fecha_vencimiento) +"\n"+ tarea.estado +"\n"+ str(tarea.porcentaje)+"\n")
            #...fechas de vencimiento de las tareas
            else:
                print("*****Lista de tareas segun sus fechas de vencimiento anteriores a "+fecha+"*****")
                for proyecto in info:
                    for tarea in proyecto.tareas:
                        if tarea.fecha_vencimiento < fechar:
                            print(str(tarea.id) +"\n"+ tarea.nombre +"\n"+ tarea.empresa_cliente +"\n"+ tarea.descripcion +"\n"+ str(tarea.fecha_inicio) +"\n"+ str(tarea.fecha_vencimiento) +"\n"+ tarea.estado +"\n"+ str(tarea.porcentaje)+"\n") 
    elif opcion == "1":
        fecha_inferior = input("Ingrese la fecha inferior del rango con el formato ano-mes-dia: ")
        while not(verifica_formato_fecha(fecha_inferior)):
            fecha_inferior = input("Ingrese correctamente la fecha con el formato ano-mes-dia: ")
        fecha_superior = input("Ingrese la fecha superior del rango con el formato ano-mes-dia: ")
        while not(verifica_formato_fecha(fecha_superior)):
            fecha_superior = input("Ingrese correctamente la fecha con el formato ano-mes-dia: ")
        fecha_inf = datetime.strptime(fecha_inferior,"%Y-%m-%d")
        fecha_sup = datetime.strptime(fecha_superior,"%Y-%m-%d")
        if filtrar == "1":
            print("*****Lista de tareas segun sus fechas de inicio entre un rango especifico*****")
            for proyecto in info:
                for tarea in proyecto.tareas:
                    if (fecha_inf < tarea.fecha_inicio) and (tarea.fecha_inicio < fecha_sup):
                        print(str(tarea.id) +"\n"+ tarea.nombre +"\n"+ tarea.empresa_cliente +"\n"+ tarea.descripcion +"\n"+ str(tarea.fecha_inicio) +"\n"+ str(tarea.fecha_vencimiento) +"\n"+ tarea.estado +"\n"+ str(tarea.porcentaje)+"\n")
        
        else:
            print("*****Lista de tareas segun sus fechas de vencimiento entre un rango especifico*****")
            for proyecto in info:
                for tarea in proyecto.tareas:
                    if (fecha_inf < tarea.fecha_vencimiento) and (tarea.fecha_vencimiento < fecha_sup):
                        print(str(tarea.id) +"\n"+ tarea.nombre +"\n"+ tarea.empresa_cliente +"\n"+ tarea.descripcion +"\n"+ str(tarea.fecha_inicio) +"\n"+ str(tarea.fecha_vencimiento) +"\n"+ tarea.estado +"\n"+ str(tarea.porcentaje)+"\n") 
    menu_reportes(info)

#Metodo que que realiza la opcion 3 (filtra los proyectos por fecha de inicio, vencimiento, estado o empresa. Ademas muestra porcentaje de finalizacion)
def metodo_3 (info):
    print("Filtrar los proyectos por:\n(1) Fecha de incio \n(2) Fecha de vencimiento\n(3) Estado\n(4) Empresa")
    opcion = input("Opciones (1/2/3/4): ")
    while opcion!="1" and opcion!="2" and opcion!="3" and opcion!="4":
        opcion = input("Ingrese correctamente su opcion: ")
    if opcion =="1":
        f = input("Ingrese una fecha con el formato ano-mes-dia: ")
        while not(verifica_formato_fecha(f)):
            f = input("Ingrese correctamente una fecha con el formato ano-mes-dia: ")
        fecha = datetime.strptime(f,"%Y-%m-%d")
        print("\n*****Lista de proyectos segun su fecha de inicio*****\n")
        for proyecto in info:
            porcentaje = 0
            cont = 0
            n = 0 
            if proyecto.fecha_inicio == fecha:
                print(str(proyecto.id)+"\n"+proyecto.nombre+"\n"+proyecto.descripcion+"\n"+str(proyecto.fecha_inicio)+"\n"+str(proyecto.fecha_vencimiento)+"\n"+proyecto.estado+"\n"+proyecto.empresa+"\n"+proyecto.gerente)
                for tarea in proyecto.tareas:
                    cont += 1
                    if tarea.estado =="Completada":
                        n += 1
                porcentaje = int(n/cont*100)
                print("Procentaje de finalizacion: ",porcentaje)
    elif opcion == "2":
        f = input("Ingrese una fecha: ")
        while not(verifica_formato_fecha(f)):
            f = input("Ingrese correctamente una fecha con el formato ano-mes-dia: ")
        fecha = datetime.strptime(f,"%Y-%m-%d")
        print("\n*****Lista de proyectos segun su fecha de inicio*****\n")
        for proyecto in info:
            porcentaje = 0
            cont = 0
            n = 0 
            if proyecto.fecha_vencimiento == fecha:
                print(str(proyecto.id)+"\n"+proyecto.nombre+"\n"+proyecto.descripcion+"\n"+str(proyecto.fecha_inicio)+"\n"+str(proyecto.fecha_vencimiento)+"\n"+proyecto.estado+"\n"+proyecto.empresa+"\n"+proyecto.gerente)
                for tarea in proyecto.tareas:
                    cont += 1
                    if tarea.estado =="Completada":
                        n += 1
                porcentaje = int(n/cont*100)
                print("Procentaje de finalizacion: ",porcentaje)
    elif opcion == "3":
        estado = input("Ingrese un estado especifico (Completada / En progreso / Pendiente): ")
        while estado!="Completada" and estado!="En progreso" and estado!="Pendiente":
            estado = input("Ingrese correctamente un estado especifico (Completada / En progreso / Pendiente): ")
        for proyecto in info:            
            porcentaje = 0
            cont = 0
            n = 0 
            if proyecto.estado == estado:
                print(str(proyecto.id)+"\n"+proyecto.nombre+"\n"+proyecto.descripcion+"\n"+str(proyecto.fecha_inicio)+"\n"+str(proyecto.fecha_vencimiento)+"\n"+proyecto.estado+"\n"+proyecto.empresa+"\n"+proyecto.gerente)
                for tarea in proyecto.tareas:
                    cont += 1
                    if tarea.estado =="Completada":
                        n += 1
                porcentaje = int(n/cont*100)
                print("Procentaje de finalizacion: ",porcentaje)
    elif opcion =="4":
        empresa = input("Ingrese una empresa especifica: ")
        for proyecto in info:            
            porcentaje = 0
            cont = 0
            n = 0 
            if proyecto.empresa== empresa:
                print(str(proyecto.id)+"\n"+proyecto.nombre+"\n"+proyecto.descripcion+"\n"+str(proyecto.fecha_inicio)+"\n"+str(proyecto.fecha_vencimiento)+"\n"+proyecto.estado+"\n"+proyecto.empresa+"\n"+proyecto.gerente)
                for tarea in proyecto.tareas:
                    cont += 1
                    if tarea.estado =="Completada":
                        n += 1
                porcentaje = int(n/cont*100)
                print("Procentaje de finalizacion: ",porcentaje)
    menu_reportes(info)

#Metodo que realiza la opcion 4 (Buscar proyecto según su nombre o id y mostrar todas las tareas junto a sus respectivas sub tareas e información básica.)
def metodo_4 (info):
    print("Listar las tareas y subtareas de un proyecto segun su:\n(1) Nombre\n(2) id")
    opcion = input("Opciones (1/2): ")
    while opcion!="1" and opcion!="2":
        opcion = input("Ingrese correctamente su opcion: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del proyecto que desea buscar: ")
        for proyecto in info:
            if proyecto.nombre == nombre:
                for tarea in proyecto.tareas:
                    porcentaje = 0
                    n = 0
                    cont = 0
                    print(str(tarea.id) +"\n"+ tarea.nombre +"\n"+ tarea.empresa_cliente +"\n"+ tarea.descripcion +"\n"+ str(tarea.fecha_inicio) +"\n"+ str(tarea.fecha_vencimiento) +"\n"+ tarea.estado +"\n"+ str(tarea.porcentaje)+"\n")
                    for subtarea in tarea.subtareas:
                        print("\t"+str(subtarea.id)+"\n\t"+subtarea.nombre+"\n\t"+subtarea.descripcion+"\n\t"+subtarea.estado)
                        cont+=1
                        if subtarea.estado == "Completada":
                            n+=1
                    porcentaje = int((n/cont)*100)
                    print("Porcentaje de progreso de la tarea: ",porcentaje)
    elif opcion == "2":
        id = int(input("Ingrese el id del proyecto que desea buscar: "))
        for proyecto in info:
            if proyecto.id == id:
                for tarea in proyecto.tareas:
                    porcentaje = 0
                    n = 0
                    cont = 0
                    print(str(tarea.id) +"\n"+ tarea.nombre +"\n"+ tarea.empresa_cliente +"\n"+ tarea.descripcion +"\n"+ str(tarea.fecha_inicio) +"\n"+ str(tarea.fecha_vencimiento) +"\n"+ tarea.estado +"\n"+ str(tarea.porcentaje)+"\n")
                    for subtarea in tarea.subtareas:
                        print("\t"+str(subtarea.id)+"\n\t"+subtarea.nombre+"\n\t"+subtarea.descripcion+"\n\t"+subtarea.estado)
                        cont+=1
                        if subtarea.estado == "Completada":
                            n+=1
                    porcentaje = int((n/cont)*100)
                    print("Porcentaje de progreso de la tarea: ",porcentaje)
    menu_reportes(info)

#Menu de opciones del modulo de reportes
def menu_reportes(info):
    print("\n*****Menu de opciones*****\n(1) Consulta de Tareas por estado\n(2) Filtrar las tareas por fecha\n(3) filtrar los proyectos por fecha de inicio, vencimiento, estado o empresa\n(4) Listar subtareas segun nombre o id del proyecto\n(5) Finalizar programa")
    opcion = input("Opciones (1/2/3/4/5): ")
    while opcion!="1" and opcion!="2" and opcion!="3" and opcion!="4" and opcion!="5":
        opcion = input("Ingrese correctamente su opcion (1/2/3/4/5): ")
    print("\n")
    if opcion == "1":
        metodo_1(info)
    elif opcion == "2":
        metodo_2(info)
    elif opcion == "3":
        metodo_3(info)
    elif opcion == "4":
        metodo_4(info)
    else:
        print("Fin del Programa")