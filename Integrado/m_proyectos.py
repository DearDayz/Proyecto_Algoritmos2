from datetime import datetime
from tareas_prio import Subtarea, Tarea
from pilas_y_colas import Pila,Cola

def verifica_formato_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

class Proyecto:    
    def __init__(self, id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado, empresa, gerente, equipo):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado
        self.empresa = empresa
        self.gerente = gerente
        self.equipo = equipo
        self.tareas = []
        self.pila_prioritarias = Pila()
        self.cola_proximas = Cola()
    
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def insertar_tarea(self, indice, tarea):
        self.tareas.insert(indice, tarea)

    def eliminar_tarea(self, tarea):
        self.tareas.remove(tarea)

    def agregar_tarea_prioritaria(self, tarea):
        self.pila_prioritarias.agregar(tarea)
    
    def agregar_tarea_proxima(self, tarea):
        self.cola_proximas.agregar(tarea)
    
    def eliminar_tarea_prioritaria(self):
        return self.pila_prioritarias.eliminar()
    
    def eliminar_tarea_proxima(self):
        return self.cola_proximas.eliminar()
    
    def consultar_tarea_prioritaria(self):
        return self.pila_prioritarias.ver_tope()
    
    def consultar_tarea_proxima(self):
        return self.cola_proximas.ver_frente()
    
    def mostrar_tiempo_total_tareas_prioritarias(self):
        self.pila_prioritarias.mostrar_tiempo_total()
    
    def mostrar_tiempo_total_tareas_proximas(self):
        self.cola_proximas.mostrar_tiempo_total()

def es_entero(cadena):
    try:
        int(cadena)
        return True
    except ValueError: 
        return False

def verifica_nombre(nombre):
    return all(caracter.isalnum() or caracter.isspace() for caracter in nombre)


def gestion_proyecto(proyectos ,proyecto):
    resp = input("1.Modificar\n2.Consultar\n3.Listar\n4.Eliminar\n¿Que desea hacer?: ")
    while not (es_entero(resp) and 1<= int(resp)<= 4):
        resp = input("Coloca una opcion valida: ")
    if resp == "1":
        resp1 = input("\n1.Id\n2.Nombre\n3.Descripcion\n4.Fecha de inicio\n5.Fecha de vencimiento\n6.Estado\n7.Empresa\n8.Gerente\n9.Equipo\n¿Que desea modificar?: ")
        while not (es_entero(resp1) and 1<= int(resp1)<= 9):
            resp1 = input("Coloca una opcion valida: ")
        if resp1 == "1":
            id = input("\nColoca el nuevo ID: ")
            while not(es_entero(id) and int(id)>= 1):
                id = input("Coloca un ID valido (solo enteros mayores a cero): ")
            proyecto.id = id
        elif resp1 == "3":
            des = input("\nColoca una nueva descripcion: ")
            while not(verifica_nombre(des) and len(des)!= 0):
                des = input("Coloca una descripcion valida (solo caracteres alfanumericos y espacios): ")
            proyecto.descripcion = des
        elif resp1 == "2":
            des = input("\nColoca un nuevo nombre: ")
            while not(verifica_nombre(des) and len(des)!= 0):
                des = input("Coloca un nombre valido (solo caracteres alfanumericos y espacios): ")
            proyecto.nombre = des
        
        elif resp1 == "4":
            fecha = input("\nColoca una nueva fecha de inicio: ")
            while not(verifica_formato_fecha(fecha)):
                fecha = input("Coloca una fecha valida (formato: año-mes-dia): ")
            proyecto.fecha_inicio = fecha
        
        elif resp1 == "5":
            fecha = input("\nColoca una nueva fecha de vencimiento: ")
            while not(verifica_formato_fecha(fecha)):
                fecha = input("Coloca una fecha valida (formato: año-mes-dia): ")
            proyecto.fecha_vencimiento = fecha
        
        elif resp1 == "6":
            estado = input("\nColoca un nuevo estado: ")
            while not(verifica_nombre(estado) and len(estado)!= 0):
                estado = input("Coloca un estado valido (solo caracteres alfanumericos y espacios): ")
            proyecto.estado = estado

        elif resp1 == "7":
            variable = input("\nColoca una nueva empresa: ")
            while not(verifica_nombre(variable) and len(variable)!= 0):
                variable = input("Coloca una empresa valida (solo caracteres alfanumericos y espacios): ")
            proyecto.empresa = variable

        elif resp1 == "8":
            variable = input("\nColoca un nuevo gerente: ")
            while not(verifica_nombre(variable) and len(variable)!= 0):
                variable = input("Coloca un gerente valido (solo caracteres alfanumericos y espacios): ")
            proyecto.gerente = variable

        elif resp1 == "9":
            variable = input("\nColoca un nuevo equipo : ")
            while not(verifica_nombre(variable) and len(variable)!= 0):
                variable = input("Coloca un equipo valido (solo caracteres alfanumericos y espacios): ")
            proyecto.equipo = [variable]
        print("Cambio realizado exitosamente!!")
    elif resp == "2":
        resp1 = input("\n1.Id\n2.Nombre\n3.Descripcion\n4.Fecha de inicio\n5.Fecha de vencimiento\n6.Estado\n7.Empresa\n8.Gerente\n9.Equipo\n¿Que dato desea consultar?: ")
        while not (es_entero(resp1) and 1<= int(resp1)<= 9):
            resp1 = input("Coloca una opcion valida: ")
        print("")
        if resp1 == "1":
            print(f"ID: {proyecto.id}")
        elif resp1 == "2":
            print(f"Nombre: {proyecto.nombre}")
        elif resp1 == "3":
            print(f"Descripcion: {proyecto.descripcion}")
        elif resp1 == "4":
            print(f"Fecha de inicio: {proyecto.fecha_inicio}")
        elif resp1 == "5":
            print(f"Fecha de vencimiento: {proyecto.fecha_vencimiento}")
        elif resp1 == "6":
            print(f"Estado: {proyecto.estado}")
        elif resp1 == "7":
            print(f"Empresa: {proyecto.empresa}")
        elif resp1 == "8":
            print(f"Gerente: {proyecto.gerente}")
        else:
            print(f"Equipo: {proyecto.equipo[0]}")

    elif resp == "3":
        print("\nListado")
        print(f"ID: {proyecto.id}")
        print(f"Nombre: {proyecto.nombre}")
        print(f"Descripcion: {proyecto.descripcion}")     
        print(f"Fecha de inicio: {proyecto.fecha_inicio}")
        print(f"Fecha de vencimiento: {proyecto.fecha_vencimiento}")
        print(f"Estado: {proyecto.estado}")
        print(f"Empresa: {proyecto.empresa}")
        print(f"Gerente: {proyecto.gerente}")   
        print(f"Equipo: {proyecto.equipo[0]}")        
    
    else:
        proyectos = list(proyectos)
        proyectos.remove(proyecto)
        print("\nProyecto eliminado satisfactoriamente")

def opcion_1(lista):
    print("\nGestion de proyectos")
    print("1.Buscar proyecto por nombre")
    print("2.Buscar proyecto por otros criterios")
    print("3.Crear nuevo proyecto")
    print("4.Salir")
    resp = input("Introduce tu opcion: ")
    while not (es_entero(resp) and 1<= int(resp)<= 4):
        resp = input("Coloca una opcion valida: ")
    if resp == "1":
        nombre = input("\nIntroduce el nombre del proyecto: ")
        while not(verifica_nombre(nombre) and len(nombre)!= 0):
            nombre = input("Coloca un nombre valido (solo caracteres alfanumericos y espacios): ")
        for i in range(len(lista)):
            if lista[i].nombre == nombre:
                print(f"\nProyecto `{nombre}` encontrado")
                gestion_proyecto(lista ,lista[i])
                break
        else:
            print("\n"+ f"Proyecto `{nombre}` no existe")
        opcion_1(lista)
    elif resp=="2":
        print("\n1.Buscar por ID")
        print("2.Buscar por Descripcion")
        print("3.Buscar por Fecha de inicio")
        print("4.Buscar por Fecha de vencimiento")
        print("5.Buscar por Estado")
        print("6.Buscar por Empresa")
        print("7.Buscar por Gerente")
        print("8.Buscar por Equipo")
        resp1 = input("¿Por cual criterio desea buscar?: ")
        while not (es_entero(resp1) and 1<= int(resp1)<= 8):
            resp1 = input("Coloca una opcion valida: ")
        if resp1 == "1":
            id = input("\nColoque un ID: ")
            while not(es_entero(id) and int(id)>= 1):
                id = input("Coloca un ID valido (solo enteros mayores a cero): ")
            for i in range(len(lista)):
                if id == lista[i].id:
                    print("\n" + f"Proyecto con id `{id}` es: {lista[i].nombre}")
                    gestion_proyecto(lista , lista[i])
                    break
                else:
                    print("\n" + f"Proyecto con ID `{id}` no existe")
            
        if resp1 == "2":
            variable = input("\nColoque una Descripcion: ")
            while not(verifica_nombre(variable) and len(variable)!= 0):
                variable = input("Coloca una descripcion valida (solo caracteres alfanumericos y espacios): ")
            for i in range(len(lista)):
                if variable == lista[i].descripcion:
                    print("\n" + f"Proyecto con descripcion `{variable}` es: {lista[i].nombre}")
                    gestion_proyecto(lista , lista[i])
                    break
            else:
                print("\n" + f"Proyecto con Descripcion `{variable}` no existe")
        
        if resp1 == "3":
            variable = input("\nColoque una Fecha de inicio: ")
            while not(verifica_formato_fecha(variable)):
                variable = input("Coloca una fecha valida (formato: año-mes-dia): ")
            for i in range(len(lista)):
                if datetime.strptime(variable , '%Y-%m-%d') == lista[i].fecha_inicio:
                    print("\n" + f"Proyecto con Fecha de inicio `{variable}` es: {lista[i].nombre}")
                    gestion_proyecto(lista , lista[i])        
                    break
            else:
                print("\n" + f"Proyecto con fecha de inicio {variable} no existe")
        
        if resp1 == "4":
            variable = input("\nColoque una Fecha de vencimiento: ")
            while not(verifica_formato_fecha(variable)):
                variable = input("Coloca una fecha valida (formato: año-mes-dia): ")
            for i in range(len(lista)):
                if datetime.strptime(variable , '%Y-%m-%d') == lista[i].fecha_vencimiento:
                    print("\n" + f"Proyecto con Fecha de vencimiento `{variable}` es: {lista[i].nombre}")
                    gestion_proyecto(lista , lista[i])    
                    break
            else:
                print("\n" + f"Proyecto con fecha de vencimiento {variable} no existe")
        
        if resp1 == "5":
            variable = input("\nColoque una Estado: ")
            while not(verifica_nombre(variable) and len(variable)!= 0):
                variable = input("Coloca un estado valido (solo caracteres alfanumericos y espacios): ")
            for i in range(len(lista)):
                if variable == lista[i].estado:
                    print("\n" + f"Proyecto con estado `{variable}` es: {lista[i].nombre}")
                    gestion_proyecto(lista , lista[i])    
                    break
            else:
                print("\n" + f"Proyecto con estado `{variable}` no existe")
        
        if resp1 == "6":
            variable = input("\nColoque una Empresa: ")
            while not(verifica_nombre(variable) and len(variable)!= 0):
                variable = input("Coloca una empresa valida (solo caracteres alfanumericos y espacios): ")
            for i in range(len(lista)):
                if variable == lista[i].empresa:
                    print("\n" + f"Proyecto con empresa `{variable}` es: {lista[i].nombre}")
                    gestion_proyecto(lista , lista[i])    
                    break
            else:
                print("\n" + f"Proyecto con empresa `{variable}` no existe")

        if resp1 == "7":
            variable = input("\nColoque un Gerente: ")
            while not(verifica_nombre(variable) and len(variable)!= 0):
                variable = input("Coloca un gerente valido (solo caracteres alfanumericos y espacios): ")
            for i in range(len(lista)):
                if variable == lista[i].gerente:
                    print("\n" + f"Proyecto con gerente `{variable}` es: {lista[i].nombre}")
                    gestion_proyecto(lista , lista[i])    
                    break
            else:
                print("\n" + f"Proyecto con gerente `{variable}` no existe")

        if resp1 == "8":
            variable = input("\nColoque un equipo: ")
            while not(verifica_nombre(variable) and len(variable)!= 0):
                variable = input("Coloca un equipo valido (solo caracteres alfanumericos y espacios): ")
            for i in range(len(lista)):
                if variable == lista[i].equipo[0]:
                    print("\n" + f"Proyecto con equipo `{variable}` es: {lista[i].nombre}")
                    gestion_proyecto(lista , lista[i])    
                    break
            else:
                print("\n" + f"Proyecto con equipo `{variable}` no existe")
        opcion_1(lista)
    elif resp =="3":
        print("\n Carga de datos: ")
        id = input("Id del proyecto: ")
        while not(es_entero(id) and int(id)>= 1):
            id = input("Coloca un ID valido (solo enteros mayores a cero): ")
        nombre = input("Nombre del proyecto: ")
        while not(verifica_nombre(nombre) and len(nombre)!= 0):
            nombre = input("Coloca un nombre valido (solo caracteres alfanumericos y espacios): ")
        descripcion = input("Coloca la descripcion del proyecto: ")
        while not(verifica_nombre(descripcion) and len(descripcion)!= 0):
            descripcion = input("Coloca una descripcion valida (solo caracteres alfanumericos y espacios): ")
        fecha_inicio = input("Coloca la fecha de inicio del proyecto: ")
        while not(verifica_formato_fecha(fecha_inicio)):
                fecha_inicio = input("Coloca una fecha valida (formato: año-mes-dia): ")
        fecha_inicio = datetime.strptime(fecha_inicio , '%Y-%m-%d')
        fecha_vencimiento = input("Coloca la fecha de vencimiento del proyecto: ")
        while not(verifica_formato_fecha(fecha_vencimiento)):
                fecha_vencimiento = input("Coloca una fecha valida (formato: año-mes-dia): ")
        fecha_vencimiento = datetime.strptime(fecha_vencimiento , '%Y-%m-%d')        
        estado = input("Coloca el estado del proyecto: ")
        while not(verifica_nombre(estado) and len(estado)!= 0):
            estado = input("Coloca un estado valido (solo caracteres alfanumericos y espacios): ")
        empresa = input("Coloca la empresa del proyecto: ")
        while not(verifica_nombre(empresa) and len(empresa)!= 0):
            empresa = input("Coloca una empresa valida (solo caracteres alfanumericos y espacios): ")        
        gerente = input("Coloca el gerente del proyecto: ")
        while not(verifica_nombre(gerente) and len(gerente)!= 0):
            gerente = input("Coloca un gerente valido (solo caracteres alfanumericos y espacios) ")      
        equipo = input("Coloca el equipo del proyecto: ")
        while not(verifica_nombre(equipo) and len(equipo)!= 0):
            equipo = input("Coloca un equipo valido (solo caracteres alfanumericos y espacios) ")    

        #tareas    
        tareas = []
        m = input("Colaca la cantidad de tareas que tiene el proyecto: ") 
        while not (es_entero(m) and 0<= int(m)):
            m = input("Coloca una opcion valida: ")
        
        for i in range(int(m)):
            idt = input("Id de la tarea: ")
            while not(es_entero(idt) and int(idt)>= 1):
                idt = input("Coloca un ID valido (solo enteros mayores a cero): ")
            nombret = input("Nombre de la tarea: ")
            while not(verifica_nombre(nombret) and len(nombret)!= 0):
                nombret = input("Coloca un nombre valido (solo caracteres alfanumericos y espacios): ")           
            empresa_cliente = input("Coloque la empresa cliente: ")
            while not(verifica_nombre(empresa_cliente) and len(empresa_cliente)!= 0):
                empresa_cliente = input("Coloca una empresa cliente valida (solo caracteres alfanumericos y espacios): ")        
            descripciont = input("Coloca la descripcion de la tarea: ")
            while not(verifica_nombre(descripciont) and len(descripciont)!= 0):
                descripciont = input("Coloca una descripcion valida (solo caracteres alfanumericos y espacios): ")      
            fecha_iniciot = input("Coloca la fecha de inicio de la tarea: ")
            while not(verifica_formato_fecha(fecha_iniciot)):
                    fecha_iniciot = input("Coloca una fecha valida (formato: año-mes-dia): ")
            fecha_iniciot = datetime.strptime(fecha_iniciot , '%Y-%m-%d')     
            fecha_vencimientot = input("Coloca la fecha de vencimiento de la tarea: ")
            while not(verifica_formato_fecha(fecha_vencimientot)):
                    fecha_vencimientot = input("Coloca una fecha valida (formato: año-mes-dia): ")
            fecha_vencimientot = datetime.strptime(fecha_vencimientot , '%Y-%m-%d')   
            estadot = input("Coloca el estado de la tarea: ")
            while not(verifica_nombre(estadot) and len(estadot)!= 0):
                estadot = input("Coloca un estado valido (solo caracteres alfanumericos y espacios): ")       
            porcentaje = input("Colca el porcentaje de la tarea: ")              
            while not(es_entero(porcentaje) and int(porcentaje)>= 0 and int(porcentaje)<= 100  ):
                porcentaje = input("Coloca un porcentaje valido (solo enteros entre 0 y 100): ")
            
            #subtarea
            subtareas = []
            j = input("Colaca la cantidad de subtareas que tiene la tarea: ") 
            while not (es_entero(j) and 0<= int(j)):
                j = input("Coloca una opcion valida: ")
            for k in range(int(j)):
                idsub = input("Id de la subtarea: ")
                while not(es_entero(idsub) and int(idsub)>= 1):
                    idsub = input("Coloca un ID valido (solo enteros mayores a cero): ")
                nombresub = input("Nombre de la subtarea: ")
                while not(verifica_nombre(nombresub) and len(nombresub)!= 0):
                    nombresub = input("Coloca un nombre valido (solo caracteres alfanumericos y espacios): ") 
                descripcionsub = input("Coloca la descripcion de la subtarea: ")
                while not(verifica_nombre(descripcionsub) and len(descripcionsub)!= 0):
                    descripcionsub = input("Coloca una descripcion valida (solo caracteres alfanumericos y espacios): ")           
                estadosub = input("Coloca el estado de la subtarea: ")
                while not(verifica_nombre(estadosub) and len(estadosub)!= 0):
                    estadosub = input("Coloca un estado valido (solo caracteres alfanumericos y espacios): ")   
                
                #Creamos el objeto subtarea
                subtarea = Subtarea(int(idsub) , nombresub , descripcionsub , estadosub)
                subtareas.append(subtarea)
            #Creamos el objeto tarea
            tarea = Tarea(idt , nombret , empresa_cliente , descripciont , fecha_iniciot , fecha_vencimientot , estadot , porcentaje)
            tarea.agregar_subtarea(subtareas)
            tareas.append(tarea)
        #Creamos el objeto proyecto
        proyec = Proyecto(id , nombre , descripcion , fecha_inicio , fecha_vencimiento , estado , empresa , gerente , [equipo])    
        proyec.agregar_tarea(tareas)
        print("\n Proyecto creado correctamente")
        print("1.Listarlo")
        print("2.No listarlo")
        resp2 = input("¿Desea listarlo o no?: ")
        while not(es_entero(resp2) and int(resp2)>= 1):
            resp2 = input("Coloca una opcion valida")
        if resp2 == "1":
            lista.append(proyec)
            print("\nProyecto listado correctamente")
        else:
            print("\nProyecto no listado") 
        opcion_1(lista)
    else:
        print("Fin del programa")    
