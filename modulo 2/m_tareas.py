from datetime import datetime
from tareas_prio import Subtarea, Tarea
from pilas_y_colas import Pila, Cola, Nodo, ListaEnlazada
from m_proyectos import Proyecto, es_entero,verifica_nombre,verifica_formato_fecha




# Inicializamos las estructuras de datos


def gestionar_tareas_prioritarias(proyecto):
    print("\nGestión de Tareas Prioritarias")
    print("1. Agregar nueva tarea prioritaria")
    print("2. Eliminar tarea prioritaria de la cima")
    print("3. Consultar la tarea prioritaria más alta")
    print("4. Mostrar tiempo total de tareas prioritarias")
    print("5. Volver")

    resp = input("Seleccione una opción: ")

    if resp == "1":
        nombre = input("Nombre de la tarea: ")
        prioridad = int(input("Prioridad de la tarea: "))
        tiempo = int(input("Duración estimada en minutos: "))
        tarea = {
            'nombre': nombre,
            'prioridad': prioridad,
            'tiempo': f"{tiempo} min"
        }
        proyecto.agregar_tarea_prioritaria(tarea)
        print("Tarea agregada exitosamente.")
    elif resp == "2":
        tarea = proyecto.eliminar_tarea_prioritaria()
        if tarea:
            print(f"Tarea eliminada: {tarea['nombre']}")
        else:
            print("La pila está vacía.")
    elif resp == "3":
        tarea = proyecto.consultar_tarea_prioritaria()
        if tarea:
            print(f"Tarea más prioritaria: {tarea['nombre']} - Prioridad: {tarea['prioridad']}")
        else:
            print("La pila está vacía.")
    elif resp == "4":
        proyecto.mostrar_tiempo_total_tareas_prioritarias()
    elif resp == "5":
        return
    else:
        print("Opción no válida.")

    gestionar_tareas_prioritarias(proyecto)

def gestionar_tareas_proximas(proyecto):
    print("\nGestión de Tareas Próximas a Vencer")
    print("1. Agregar nueva tarea próxima a vencer")
    print("2. Eliminar tarea próxima a vencer del frente")
    print("3. Consultar la tarea más próxima a vencer")
    print("4. Mostrar tiempo total de tareas próximas a vencer")
    print("5. Volver")

    resp = input("Seleccione una opción: ")

    if resp == "1":
        nombre = input("Nombre de la tarea: ")
        fecha_str = input("Fecha de vencimiento (AAAA-MM-DD): ")
        tiempo = int(input("Duración estimada en minutos: "))
        fecha_vencimiento = datetime.datetime.strptime(fecha_str, '%Y-%m-%d')
        tarea = {
            'nombre': nombre,
            'fecha_vencimiento': fecha_vencimiento,
            'tiempo': datetime.timedelta(minutes=tiempo)
        }
        proyecto.agregar_tarea_proxima(tarea)
        print("Tarea agregada exitosamente.")
    elif resp == "2":
        tarea = proyecto.eliminar_tarea_proxima()
        if tarea:
            print(f"Tarea eliminada: {tarea['nombre']}")
        else:
            print("La cola está vacía.")
    elif resp == "3":
        tarea = proyecto.consultar_tarea_proxima()
        if tarea:
            print(f"Tarea más próxima a vencer: {tarea['nombre']} - Vence: {tarea['fecha_vencimiento'].strftime('%Y-%m-%d')}")
        else:
            print("La cola está vacía.")
    elif resp == "4":
        proyecto.mostrar_tiempo_total_tareas_proximas()
    elif resp == "5":
        return
    else:
        print("Opción no válida.")

    gestionar_tareas_proximas(proyecto)

def opcion_2(lista):
    print("\nMódulo de Gestión de Tareas y Prioridades")
    print("1. Agregar nueva tarea")
    print("2. Insertar tarea en posición específica")
    print("3. Eliminar tarea")
    print("4. Buscar tarea por nombre u otros criterios")
    print("5. Actualizar información de tarea existente")
    print("6. Gestionar tareas prioritarias")
    print("7. Gestionar tareas próximas a vencer")
    print("8. Salir")
    
    resp = input("Seleccione una opción: ")
    while not (es_entero(resp) and 1 <= int(resp) <= 8):
        resp = input("Seleccione una opción válida: ")
    
    if resp == "1":
        # Agregar nueva tarea al final de la lista de tareas de un proyecto específico
        id_proyecto = input("Ingrese el ID único del proyecto donde desea agregar la tarea: ")
        

        index = -1
        x = 0
        for i in lista:
            if i.id == int(id_proyecto):
                index = x 
                break
            x += 1
        
        if index != -1:
            idt = input("Id de la nueva tarea: ")
            while not (es_entero(idt) and int(idt) >= 1):
                idt = input("Coloca un ID válido (solo enteros mayores a cero): ")
            
            nombret = input("Nombre de la nueva tarea: ")
            while not (verifica_nombre(nombret) and len(nombret) != 0):
                nombret = input("Coloca un nombre válido (solo caracteres alfanuméricos y espacios): ")
            
            empresa_cliente = input("Empresa cliente de la nueva tarea: ")
            while not (verifica_nombre(empresa_cliente) and len(empresa_cliente) != 0):
                empresa_cliente = input("Coloca una empresa cliente válida (solo caracteres alfanuméricos y espacios): ")
            
            descripciont = input("Descripción de la nueva tarea: ")
            while not (verifica_nombre(descripciont) and len(descripciont) != 0):
                descripciont = input("Coloca una descripción válida (solo caracteres alfanuméricos y espacios): ")
            
            fecha_iniciot = input("Fecha de inicio de la nueva tarea (formato: año-mes-dia): ")
            while not (verifica_formato_fecha(fecha_iniciot)):
                fecha_iniciot = input("Coloca una fecha válida (formato: año-mes-dia): ")
            fecha_iniciot = datetime.strptime(fecha_iniciot, '%Y-%m-%d')
            
            fecha_vencimientot = input("Fecha de vencimiento de la nueva tarea (formato: año-mes-dia): ")
            while not (verifica_formato_fecha(fecha_vencimientot)):
                fecha_vencimientot = input("Coloca una fecha válida (formato: año-mes-dia): ")
            fecha_vencimientot = datetime.strptime(fecha_vencimientot, '%Y-%m-%d')
            
            estadot = input("Estado de la nueva tarea: ")
            while not (verifica_nombre(estadot) and len(estadot) != 0):
                estadot = input("Coloca un estado válido (solo caracteres alfanuméricos y espacios): ")
            
            porcentaje = input("Porcentaje de la nueva tarea: ")
            while not (es_entero(porcentaje) and 0 <= int(porcentaje) <= 100):
                porcentaje = input("Coloca un porcentaje válido (solo enteros entre 0 y 100): ")
            
            # Crear la lista de subtareas
            subtareas = []
            j = input("Cantidad de subtareas de la nueva tarea: ")
            while not (es_entero(j) and int(j) >= 0):
                j = input("Coloca una opción válida: ")
            
            for k in range(int(j)):
                idsub = input(f"Id de la subtarea {k + 1}: ")
                while not (es_entero(idsub) and int(idsub) >= 1):
                    idsub = input("Coloca un ID válido (solo enteros mayores a cero): ")
                
                nombresub = input(f"Nombre de la subtarea {k + 1}: ")
                while not (verifica_nombre(nombresub) and len(nombresub) != 0):
                    nombresub = input("Coloca un nombre válido (solo caracteres alfanuméricos y espacios): ")
                
                descripcionsub = input(f"Descripción de la subtarea {k + 1}: ")
                while not (verifica_nombre(descripcionsub) and len(descripcionsub) != 0):
                    descripcionsub = input("Coloca una descripción válida (solo caracteres alfanuméricos y espacios): ")
                
                estadosub = input(f"Estado de la subtarea {k + 1}: ")
                while not (verifica_nombre(estadosub) and len(estadosub) != 0):
                    estadosub = input("Coloca un estado válido (solo caracteres alfanuméricos y espacios): ")
                
                # Crear la subtarea y agregarla a la lista de subtareas
                subtarea = Subtarea(int(idsub), nombresub, descripcionsub, estadosub)
                subtareas.append(subtarea)
            
            # Crear la tarea y agregarla al proyecto encontrado
            tarea = Tarea(int(idt), nombret, empresa_cliente, descripciont, fecha_iniciot, fecha_vencimientot, estadot, int(porcentaje))
            tarea.agregar_subtarea(subtareas)
            lista[index].agregar_tarea(tarea)
            
            print("\nTarea agregada correctamente.")

            #verificacr si la tarea se guardo correctamente
            print("\nListado de tareas:")
            for tarea in lista[index].tareas:
                print(f"ID: {tarea.id} - Nombre: {tarea.nombre}")
                
        else:
            print(f"No se encontró ningún proyecto con el ID '{id_proyecto}'.")
        
        opcion_2(lista)

    elif resp == "2":

        # Insertar tarea en posición específica dentro de la lista de tareas de un proyecto
        id_proyecto = input("Ingrese el ID único del proyecto donde desea insertar la tarea: ")
        

        index = -1
        x = 0
        for i in lista:
            if i.id == int(id_proyecto):
                index = x 
                break
            x += 1
        
        if index != -1:
            pos = input("Posición donde desea insertar la tarea (1 para insertar al inicio): ")
            while not (es_entero(pos) and int(pos) >= 1 and int(pos) <= len(lista[index].tareas)):
                pos = input("Coloca una posición válida: ")
            
            idt = input("Id de la nueva tarea: ")
            while not (es_entero(idt) and int(idt) >= 1):
                idt = input("Coloca un ID válido (solo enteros mayores a cero): ")
            
            nombret = input("Nombre de la nueva tarea: ")
            while not (verifica_nombre(nombret) and len(nombret) != 0):
                nombret = input("Coloca un nombre válido (solo caracteres alfanuméricos y espacios): ")
            
            empresa_cliente = input("Empresa cliente de la nueva tarea: ")
            while not (verifica_nombre(empresa_cliente) and len(empresa_cliente) != 0):
                empresa_cliente = input("Coloca una empresa cliente válida (solo caracteres alfanuméricos y espacios): ")
            
            descripciont = input("Descripción de la nueva tarea: ")
            while not (verifica_nombre(descripciont) and len(descripciont) != 0):
                descripciont = input("Coloca una descripción válida (solo caracteres alfanuméricos y espacios): ")
            
            fecha_iniciot = input("Fecha de inicio de la nueva tarea (formato: año-mes-dia): ")
            while not (verifica_formato_fecha(fecha_iniciot)):
                fecha_iniciot = input("Coloca una fecha válida (formato: año-mes-dia): ")
            fecha_iniciot = datetime.strptime(fecha_iniciot, '%Y-%m-%d')
            
            fecha_vencimientot = input("Fecha de vencimiento de la nueva tarea (formato: año-mes-dia): ")
            while not (verifica_formato_fecha(fecha_vencimientot)):
                fecha_vencimientot = input("Coloca una fecha válida (formato: año-mes-dia): ")
            fecha_vencimientot = datetime.strptime(fecha_vencimientot, '%Y-%m-%d')
            
            estadot = input("Estado de la nueva tarea: ")
            while not (verifica_nombre(estadot) and len(estadot) != 0):
                estadot = input("Coloca un estado válido (solo caracteres alfanuméricos y espacios): ")
            
            porcentaje = input("Porcentaje de la nueva tarea: ")
            while not (es_entero(porcentaje) and 0 <= int(porcentaje) <= 100):
                porcentaje = input("Coloca un porcentaje válido (solo enteros entre 0 y 100): ")
            
            # Crear la lista de subtareas
            subtareas = []
            j = input("Cantidad de subtareas de la nueva tarea: ")
            while not (es_entero(j) and int(j) >= 0):
                j = input("Coloca una opción válida: ")
            
            for k in range(int(j)):
                idsub = input(f"Id de la subtarea {k + 1}: ")
                while not (es_entero(idsub) and int(idsub) >= 1):
                    idsub = input("Coloca un ID válido (solo enteros mayores a cero): ")
                
                nombresub = input(f"Nombre de la subtarea {k + 1}: ")
                while not (verifica_nombre(nombresub) and len(nombresub) != 0):
                    nombresub = input("Coloca un nombre válido (solo caracteres alfanuméricos y espacios): ")
                
                descripcionsub = input(f"Descripción de la subtarea {k + 1}: ")
                while not (verifica_nombre(descripcionsub) and len(descripcionsub) != 0):
                    descripcionsub = input("Coloca una descripción válida (solo caracteres alfanuméricos y espacios): ")
                
                estadosub = input(f"Estado de la subtarea {k + 1}: ")
                while not (verifica_nombre(estadosub) and len(estadosub) != 0):
                    estadosub = input("Coloca un estado válido (solo caracteres alfanuméricos y espacios): ")
                
                # Crear la subtarea y agregarla a la lista de subtareas
                subtarea = Subtarea(int(idsub), nombresub, descripcionsub, estadosub)
                subtareas.append(subtarea)
            
            # Crear la tarea y agregarla al proyecto encontrado en la posición especificada
            tarea = Tarea(int(idt), nombret, empresa_cliente, descripciont, fecha_iniciot, fecha_vencimientot, estadot, int(porcentaje))
            tarea.agregar_subtarea(subtareas)
            lista[index].insertar_tarea(int(pos)-1, tarea)  # Restamos 1 para ajustar al índice de Python
            
            print("\nTarea insertada correctamente.")

            # Verificar si la tarea se insertó correctamente
            print("\nListado de tareas actualizado:")
            for tarea in lista[index].tareas:
                print(f"ID: {tarea.id} - Nombre: {tarea.nombre}")
        
        else:
            print(f"No se encontró ningún proyecto con el ID '{id_proyecto}'.")
        
        opcion_2(lista)
        
    elif resp == "3":
        # Eliminar tarea de la lista de tareas de un proyecto específico
        id_proyecto = input("Ingrese el ID único del proyecto donde desea eliminar la tarea: ")
        

        index = -1
        x = 0
        for i in lista:
            if i.id == int(id_proyecto):
                index = x 
                break
            x += 1
        
        if index != -1:
            idt = input("Ingrese el ID de la tarea que desea eliminar: ")
            while not (es_entero(idt) and int(idt) >= 1):
                idt = input("Coloca un ID válido (solo enteros mayores a cero): ")
            
            tarea_encontrada = None
            x = 0
            ind = -1
            for tarea in lista[index].tareas:
                if tarea.id == int(idt):
                    tarea_encontrada = tarea
                    ind = x
                    break
                x += 1
            
            if tarea_encontrada:
                lista[index].eliminar_tarea(tarea_encontrada)
                print("\nTarea eliminada correctamente.")

                # Verificar si la tarea se eliminó correctamente
                print("\nListado de tareas actualizado:")
                for tarea in lista[index].tareas:
                    print(f"ID: {tarea.id} - Nombre: {tarea.nombre}")
            else:
                print(f"No se encontró ninguna tarea con el ID '{idt}'.")
        
        else:
            print(f"No se encontró ningún proyecto con el ID '{id_proyecto}'.")
        
        opcion_2(lista)

    elif resp == "4":
        # Buscar tarea por nombre u otros criterios
        criterio = input("Ingrese el criterio de búsqueda (nombre, empresa cliente, estado): ").strip().lower()
        while criterio not in ['nombre', 'empresa cliente', 'estado']:
            criterio = input("Ingrese un criterio válido (nombre, empresa cliente, estado): ").strip().lower()
        
        valor = input(f"Ingrese el valor del {criterio} para buscar: ")
        while not (verifica_nombre(valor) and len(valor) != 0):
            valor = input(f"Ingrese un {criterio} válido (solo caracteres alfanuméricos y espacios): ")
        
        print(f"\nResultados de la búsqueda por {criterio} '{valor}':")
        encontrado = False
        
        for proyecto in lista:
            for tarea in proyecto.tareas:
                if criterio == 'nombre' and valor.lower() in tarea.nombre.lower():
                    encontrado = True
                    print(f"Tarea encontrada en el proyecto '{proyecto.nombre}':")
                    print(f"""
                            {tarea.id}
                            {tarea.nombre}
                            {tarea.empresa_cliente}
                            {tarea.descripcion}
                            {tarea.fecha_inicio}
                            {tarea.fecha_vencimiento}
                            {tarea.estado}
                            {tarea.porcentaje}

                    """)
                    print("---------------------")
                
                elif criterio == 'empresa cliente' and valor.lower() in tarea.empresa_cliente.lower():
                    encontrado = True
                    print(f"Tarea encontrada en el proyecto '{proyecto.nombre}':")
                    print(f"""
                            {tarea.id}
                            {tarea.nombre}
                            {tarea.empresa_cliente}
                            {tarea.descripcion}
                            {tarea.fecha_inicio}
                            {tarea.fecha_vencimiento}
                            {tarea.estado}
                            {tarea.porcentaje}

                    """)
                    print("---------------------")
                
                elif criterio == 'estado' and valor.lower() in tarea.estado.lower():
                    encontrado = True
                    print(f"Tarea encontrada en el proyecto '{proyecto.nombre}':")
                    print(f"""
                            {tarea.id}
                            {tarea.nombre}
                            {tarea.empresa_cliente}
                            {tarea.descripcion}
                            {tarea.fecha_inicio}
                            {tarea.fecha_vencimiento}
                            {tarea.estado}
                            {tarea.porcentaje}

                    """)
                    print("---------------------")
        
        if not encontrado:
            print(f"No se encontraron tareas con el criterio {criterio} '{valor}'.")

        opcion_2(lista)

    elif resp == "5":
        # Código para actualizar información de tarea existente
        id_proyecto = input("Ingrese el ID único del proyecto donde desea actualizar la tarea: ")
        

        index = -1
        x = 0
        for i in lista:
            if i.id == int(id_proyecto):
                index = x 
                break
            x += 1
        
        if index != -1:
            idt = input("Ingrese el ID de la tarea que desea actualizar: ")
            while not (es_entero(idt) and int(idt) >= 1):
                idt = input("Coloca un ID válido (solo enteros mayores a cero): ")
            
            tarea_encontrada = None
            for tarea in lista[index].tareas:
                if tarea.id == int(idt):
                    tarea_encontrada = tarea
                    break
            
            if tarea_encontrada:
                print("Ingrese los nuevos datos de la tarea (deje en blanco para mantener el valor actual):")
                
                nombret = input(f"Nombre actual: {tarea_encontrada.nombre}. Nuevo nombre (deje en blanco para mantener): ").strip()
                if len(nombret) > 0:
                    while not (verifica_nombre(nombret)):
                        nombret = input("Coloca un nombre válido (solo caracteres alfanuméricos y espacios): ").strip()
                    tarea_encontrada.nombre = nombret
                
                empresa_cliente = input(f"Empresa cliente actual: {tarea_encontrada.empresa_cliente}. Nueva empresa cliente (deje en blanco para mantener): ").strip()
                if len(empresa_cliente) > 0:
                    while not (verifica_nombre(empresa_cliente)):
                        empresa_cliente = input("Coloca una empresa cliente válida (solo caracteres alfanuméricos y espacios): ").strip()
                    tarea_encontrada.empresa_cliente = empresa_cliente
                
                descripciont = input(f"Descripción actual: {tarea_encontrada.descripcion}. Nueva descripción (deje en blanco para mantener): ").strip()
                if len(descripciont) > 0:
                    while not (verifica_nombre(descripciont)):
                        descripciont = input("Coloca una descripción válida (solo caracteres alfanuméricos y espacios): ").strip()
                    tarea_encontrada.descripcion = descripciont
                
                fecha_iniciot = input(f"Fecha de inicio actual: {tarea_encontrada.fecha_inicio.strftime('%Y-%m-%d')}. Nueva fecha de inicio (formato: año-mes-dia, deje en blanco para mantener): ").strip()
                if len(fecha_iniciot) > 0:
                    while not (verifica_formato_fecha(fecha_iniciot)):
                        fecha_iniciot = input("Coloca una fecha válida (formato: año-mes-dia): ").strip()
                    tarea_encontrada.fecha_inicio = datetime.strptime(fecha_iniciot, '%Y-%m-%d')
                
                fecha_vencimientot = input(f"Fecha de vencimiento actual: {tarea_encontrada.fecha_vencimiento.strftime('%Y-%m-%d')}. Nueva fecha de vencimiento (formato: año-mes-dia, deje en blanco para mantener): ").strip()
                if len(fecha_vencimientot) > 0:
                    while not (verifica_formato_fecha(fecha_vencimientot)):
                        fecha_vencimientot = input("Coloca una fecha válida (formato: año-mes-dia): ").strip()
                    tarea_encontrada.fecha_vencimiento = datetime.strptime(fecha_vencimientot, '%Y-%m-%d')
                
                estadot = input(f"Estado actual: {tarea_encontrada.estado}. Nuevo estado (deje en blanco para mantener): ").strip()
                if len(estadot) > 0:
                    while not (verifica_nombre(estadot)):
                        estadot = input("Coloca un estado válido (solo caracteres alfanuméricos y espacios): ").strip()
                    tarea_encontrada.estado = estadot
                
                porcentaje = input(f"Porcentaje actual: {tarea_encontrada.porcentaje}. Nuevo porcentaje (deje en blanco para mantener): ").strip()
                if len(porcentaje) > 0:
                    while not (es_entero(porcentaje) and 0 <= int(porcentaje) <= 100):
                        porcentaje = input("Coloca un porcentaje válido (solo enteros entre 0 y 100): ").strip()
                    tarea_encontrada.porcentaje = int(porcentaje)
                
                # Actualizar subtareas
                if len(tarea_encontrada.subtareas) > 0:
                    print("\nSubtareas actuales:")
                    for subtarea in tarea_encontrada.subtareas:
                        subtarea.mostrar_informacion()
                    
                    opcion_subtareas = input("\nDesea actualizar las subtareas (s/n): ").strip().lower()
                    if opcion_subtareas == 's':
                        nueva_subtareas = []
                        j = input("Cantidad de subtareas actualizada: ")
                        while not (es_entero(j) and int(j) >= 0):
                            j = input("Coloca una opción válida: ")
                        
                        for k in range(int(j)):
                            idsub = input(f"Id de la subtarea {k + 1}: ")
                            while not (es_entero(idsub) and int(idsub) >= 1):
                                idsub = input("Coloca un ID válido (solo enteros mayores a cero): ")
                            
                            nombresub = input(f"Nombre de la subtarea {k + 1}: ")
                            while not (verifica_nombre(nombresub) and len(nombresub) != 0):
                                nombresub = input("Coloca un nombre válido (solo caracteres alfanuméricos y espacios): ")
                            
                            descripcionsub = input(f"Descripción de la subtarea {k + 1}: ")
                            while not (verifica_nombre(descripcionsub) and len(descripcionsub) != 0):
                                descripcionsub = input("Coloca una descripción válida (solo caracteres alfanuméricos y espacios): ")
                            
                            estadosub = input(f"Estado de la subtarea {k + 1}: ")
                            while not (verifica_nombre(estadosub) and len(estadosub) != 0):
                                estadosub = input("Coloca un estado válido (solo caracteres alfanuméricos y espacios): ")
                            
                            # Crear la subtarea y agregarla a la lista de subtareas
                            subtarea = Subtarea(int(idsub), nombresub, descripcionsub, estadosub)
                            nueva_subtareas.append(subtarea)
                        
                        tarea_encontrada.actualizar_subtareas(nueva_subtareas)
                        print("\nSubtareas actualizadas correctamente.")
                
                print("\nInformación de tarea actualizada:")
                

                print(f"""
                            {tarea_encontrada.id}
                            {tarea_encontrada.nombre}
                            {tarea_encontrada.empresa_cliente}
                            {tarea_encontrada.descripcion}
                            {tarea_encontrada.fecha_inicio}
                            {tarea_encontrada.fecha_vencimiento}
                            {tarea_encontrada.estado}
                            {tarea_encontrada.porcentaje}

                """)
                
            else:
                print(f"No se encontró ninguna tarea con el ID '{idt}'.")
        
        else:
            print(f"No se encontró ningún proyecto con el ID '{id_proyecto}'.")
        
        opcion_2(lista)
    
    elif resp == "6":
        # Código para actualizar información de tarea existente
        id_proyecto = input("Ingrese el ID único del proyecto donde desea gestionar las tareas prioritarias:")
        

        index = -1
        x = 0
        for i in lista:
            if i.id == int(id_proyecto):
                index = x 
                break
            x += 1
        
        if index != -1:
            gestionar_tareas_prioritarias(lista[index])
        opcion_2(lista)
    elif resp == "7":
        # Código para actualizar información de tarea existente
        id_proyecto = input("Ingrese el ID único del proyecto donde desea gestionar las tareas próximas a vencer:")
        

        index = -1
        x = 0
        for i in lista:
            if i.id == int(id_proyecto):
                index = x 
                break
            x += 1
        
        if index != -1:
            gestionar_tareas_proximas(lista[index])
        opcion_2(lista)
    elif resp == "8":
        
        print("Saliendo del módulo de gestión de tareas.")

    else:
        print("Opción no válida. Intente de nuevo.")