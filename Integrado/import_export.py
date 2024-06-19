import json
from datetime import datetime
from tareas_prio import Tarea, Subtarea
from m_proyectos import Proyecto , opcion_1
from m_reportes import menu_reportes
from m_tareas import opcion_2
  

#Agrego las rutas a un archivo .txt
ruta_datos = r'C:\Universidad\Semestre 5\Algortimos 2\4ta evauluacion\Integrado\datos.json'
ruta_subtareas = r'C:\Universidad\Semestre 5\Algortimos 2\4ta evauluacion\Integrado\subtareas_modificadas.json'
rutas = open('config.txt','w')
rutas.write(ruta_datos + "\n")
rutas.write(ruta_subtareas + "\n")
# Carga el archivo JSON existente
with open(ruta_datos, 'r') as file:
    data = json.load(file)

# Extrae las subtareas y agrega la informacion del id del proyecto y de la tarea
subtareas_modificadas = []
for proyecto in data['proyectos']:
    for tarea in proyecto['tareas']:
        for subtarea in tarea['subtareas']:
            # Agrega nueva información a la subtarea
            subtarea['id_proyecto'] = proyecto['id']
            subtarea['id_tarea'] = tarea['id']
            subtareas_modificadas.append(subtarea)

# Guarda las subtareas modificadas en un nuevo archivo JSON 
with open(ruta_subtareas, 'w') as file:
    json.dump(subtareas_modificadas, file, indent=4)

#Funcion que me devuelve una lista con todos los proyectos, tareas y subtareas
def cargar_datos_desde_json(nombre_archivo):
    proyectos = []
    with open(nombre_archivo, "r") as archivo:
        datos = json.load(archivo)
        for proyecto_data in datos["proyectos"]:
            proyecto = Proyecto(
                proyecto_data["id"],
                proyecto_data["nombre"],
                proyecto_data["descripcion"],
                datetime.strptime(proyecto_data["fecha_inicio"], "%Y-%m-%d"),
                datetime.strptime(proyecto_data["fecha_vencimiento"], "%Y-%m-%d"),
                proyecto_data["estado"],
                proyecto_data["empresa"],
                proyecto_data["gerente"],
                proyecto_data["equipo"]
            )
            for tarea_data in proyecto_data["tareas"]:
                tarea = Tarea(
                    tarea_data["id"],
                    tarea_data["nombre"],
                    tarea_data["empresa_cliente"],
                    tarea_data["descripcion"],
                    datetime.strptime(tarea_data["fecha_inicio"], "%Y-%m-%d"),
                    datetime.strptime(tarea_data["fecha_vencimiento"], "%Y-%m-%d"),
                    tarea_data["estado"],
                    tarea_data["porcentaje"]
                )
                for subtarea_data in tarea_data.get("subtareas", []):
                    subtarea = Subtarea(
                        subtarea_data["id"],
                        subtarea_data["nombre"],
                        subtarea_data["descripcion"],
                        subtarea_data["estado"]
                    )
                    tarea.agregar_subtarea(subtarea)
                proyecto.agregar_tarea(tarea)
            proyectos.append(proyecto)
    return proyectos

def menu_principal(info):
    print("\nIndique que desea:\n(1) Gestionar Proyectos\n(2) Gestion de tareas\n(3)Visualizar reportes\n(4) Salir del programa")
    opcion = input("Opciones (1/2/3/4): ")
    while opcion!="1" and opcion!="2" and opcion!="3" and opcion!="4":
        opcion = input("Ingrese correctamente su opcion: ")
    print("\n")
    if opcion == "1":
        opcion_1(info)
        menu_principal(info)
    elif opcion == "2":
        opcion_2(info)
        menu_principal(info)
    elif opcion =="3":
        menu_reportes(info)
        menu_principal(info)
    else:
        print("\nFin del programa")

info = cargar_datos_desde_json(ruta_datos)
menu_principal(info)
