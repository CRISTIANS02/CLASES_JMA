#tarea
## crear una lista con 10 objetos que obtenga los adatos de las tiendas comerciales
#ejemplo:
# tiendas=[
#     {
#         'ruc':'10714504431',
#         'nombre': ' the brothers',
#         'categoria':['abarrotes','bodega'],
#         'horario_atencion':{
#              'turno_mañana':7am-12m,
#              'turno_tarde':2pm-8pm
#         },
#         'gerente':'manuel'
#     }
# ]
# observacion1:
# las categorias sera de 4: abarrotes, farmacia,bodega,restaurant.
#Observacion2:
#Los gerentes solo podran ser los siguientes: edwin,china,crhistian,nadine
# realizar los siguientes ejercicios
# crear la clase para tiendas que tenga los siguientes metodoso uso de caso
 #1. crear un metodo que me filtre las tiendas que tiene cada gerente
 #2. crear un metodo que me muestre los negocios que tienen mas de dos categorias
 #3. crear un metodo que me muestre solo el nombre y ruc de las tiendas.
# Ejemplo de uso






class Tienda:
    def __init__(self, ruc, nombre, categorias, horario_atencion, gerente):
        self.ruc = ruc
        self.nombre = nombre
        self.categorias = categorias
        self.horario_atencion = horario_atencion
        self.gerente = gerente

    def filtrar_por_gerente(self, gerente):
        tiendas_gerente = []
        for tienda in tiendas:
            if tienda['gerente'] == gerente:
                tiendas_gerente.append(tienda)
        return tiendas_gerente

    def negocios_con_mas_categorias(self):
        negocios = []
        for tienda in tiendas:
            if len(tienda['categoria']) > 2:
                negocios.append(tienda)
        return negocios

    def mostrar_nombre_ruc(self):
        info_tiendas = []
        for tienda in tiendas:
            info_tiendas.append({'nombre': tienda['nombre'], 'ruc': tienda['ruc']})
        return info_tiendas
    
tiendas = [
#tienda → 1
    {  
        'ruc': '10714504431',
        'nombre': 'The Brothers', 
        'categoria': ['abarrotes', 'bodega'],
        'horario_atencion': 
            {
                'turno_mañana': '7am-12m',
                'turno_tarde': '2pm-8pm'}, 
        'gerente': 'manuel'
    },
#tienda → 2
    {
        'ruc': '12345678901',
        'nombre': 'PharmaPlus',
        'categoria': ['farmacia'],
         'horario_atencion':
             {
                 'turno_mañana': '8am-1pm',
                 'turno_tarde': '3pm-9pm'
             },
         'gerente': 'edwin'
    },
#tienda → 3
    {
        'ruc': '98765432109',
        'nombre': 'AyacuChano', 
        'categoria': 
            [
                'abarrotes',
                'bodega', 
                'restaurant'
            ], 
        'horario_atencion':
            {
                'turno_mañana': '9am-1pm',
                'turno_tarde': '4pm-10pm'
            },
         'gerente': 'china'
    },
#tienda → 4
    {
        'ruc':'10236545896', 
        'nombre': 'IntiPharmha',
        'categoria':
            [
                'farmacia'
            ], 
        'horario_atencion':
            {
                'turno_mañana':'9am-2pm', 
                'turno_tarde':'4pm-9pm'
            }, 
        'gerente':'nadine'
    },
#tienda → 5
    {
        'ruc':'10258963478',
     'nombre': 'Bodega Centralithon', 
     'categoria':
         [
             'bodega'
        ], 
     'horario_atencion':
         {
             'turno_mañana':'8am-1pm',
             'turno_tarde':'2pm-8pm'
         }, 'gerente':'manuel'
    },
#tienda → 6
    {
        'ruc':'10214563201',
        'nombre': 'Minimarket Don Pepe',
        'categoria':
            [
                'abarrotes'
            ],
        'horario_atencion':
         {
             'turno_mañana':'7am-12m',
             'turno_tarde':'1pm-9pm'
         }, 'gerente':'china'
    },
#tienda → 7
    {
        'ruc':'10896325471', 
        'nombre': 'Restaurante Sabor del Mar', 
        'categoria':['restaurant'], 
        'horario_atencion':
            {
                'turno_mañana':'11am-4pm', 
                'turno_tarde':'6pm-11pm'
            },
        'gerente':'edwin'
    }, 
#tienda → 8
    {
        'ruc':'10236587452', 
        'nombre': 'Farmacia Santa Lucia',
        'categoria':['farmacia'], 
        'horario_atencion':
            {
                'turno_mañana':'10am-2pm', 
                'turno_tarde':'5pm-10pm'
            },
        'gerente':'nadine'
    },
#tienda → 19
    {
        'ruc':'10289561743', 
        'nombre': 'Minimarket Abierto 24/7', 
        'categoria':['abarrotes', 'bodega'], 
        'horario_atencion':
            {
                'turno_continuo':'0am-11:59pm'
            },
        'gerente':'christian'
    },
#tienda →10
 {
        'ruc':'10289581740', 
        'nombre': 'The 24/7', 
        'categoria':['abarrotes', 'bodega'], 
        'horario_atencion':
            {
                'turno_mañana':'7am-12m',
                'turno_tarde':'1pm-9pm'
            },
        'gerente':'nadine'
    }
]
 
 
# class Tienda:
#     def __init__(self, ruc, nombre, categorias, horario_atencion, gerente):
#         self.ruc = ruc
#         self.nombre = nombre
#         self.categorias = categorias
#         self.horario_atencion = horario_atencion
#         self.gerente = gerente

#     def filtrar_por_gerente(self, gerente):
#         tiendas_gerente = []
#         for tienda in tiendas:
#             if tienda['gerente'] == gerente:
#                 tiendas_gerente.append(tienda)
#         return tiendas_gerente

#     def negocios_con_mas_categorias(self):
#         negocios = []
#         for tienda in tiendas:
#             if len(tienda['categoria']) > 2:
#                 negocios.append(tienda)
#         return negocios

#     def mostrar_nombre_ruc(self):
#         info_tiendas = []
#         for tienda in tiendas:
#             info_tiendas.append({'nombre': tienda['nombre'], 'ruc': tienda['ruc']})
#         return info_tiendas




tienda_obj = Tienda('', '', [], {}, '')
# tiendas_gerente = tienda_obj.filtrar_por_gerente('edwin')
# print(tiendas_gerente)

# negocios_categorias = tienda_obj.negocios_con_mas_categorias()
# print(negocios_categorias)

nombre_ruc_tiendas = tienda_obj.mostrar_nombre_ruc()
print(nombre_ruc_tiendas)