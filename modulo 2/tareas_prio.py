class Tarea:
    def __init__(self, id, nombre, empresa_cliente, descripcion, fecha_inicio, fecha_vencimiento, estado, porcentaje):
        self.id = id
        self.nombre = nombre
        self.empresa_cliente = empresa_cliente
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado
        self.porcentaje = porcentaje
        self.subtareas = []
    
    def agregar_subtarea(self, subtarea):
        self.subtareas.append(subtarea)
    



class Subtarea:
    def __init__(self, id, nombre, descripcion, estado):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

    def mostrar_informacion(self):
        print(f"""
                {self.id} 
                {self.nombre} 
                {self.descripcion} 
                {self.estado} 
        """)