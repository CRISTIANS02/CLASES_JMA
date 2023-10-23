tiendas = [
  {'ruc':'10714504431',
   'nombre': 'The Brothers',
   'categoria':['abarrotes','bodega'], 
   'horario_atencion':{
       'turno_mañana':'7am-12m',
       'turno_tarde':'2pm-8pm'},
   'gerente':'manuel'},
  
  {'ruc':'10785236952', 
   'nombre': 'Farmacia Cruz Verde',
   'categoria':['farmacia'],
   'horario_atencion':{
       'turno_mañana':'8am-1pm',
        'turno_tarde':'3pm-9pm'},
   'gerente':'china'},
   
  {'ruc':'10204589632', 
   'nombre': 'Minimarket 24 horas', 
   'categoria':['abarrotes','bodega'],
   'horario_atencion':{'turno_mañana':'6am-12m',
                       'turno_tarde':'1pm-11pm'},
   'gerente':'edwin'},
   
  {'ruc':'10658921574',
   'nombre': 'Restaurant Sabor Peruano',
   'categoria':['restaurant'],
   'horario_atencion':{'turno_mañana':'10am-3pm',
                  'turno_tarde':'6pm-11pm'}, 
   'gerente':'crhistian'},
   
  {'ruc':'10236545896', 'nombre': 'Farmacia la Economica', 'categoria':['farmacia'],
   'horario_atencion':{'turno_mañana':'9am-2pm', 'turno_tarde':'4pm-9pm'}, 'gerente':'nadine'},
   
  {'ruc':'10258963478', 'nombre': 'Bodega Central', 'categoria':['bodega'],
   'horario_atencion':{'turno_mañana':'8am-1pm', 'turno_tarde':'2pm-8pm'}, 'gerente':'manuel'},
   
  {'ruc':'10214563201', 'nombre': 'Minimarket Don Pepe', 'categoria':['abarrotes'],
   'horario_atencion':{'turno_mañana':'7am-12m', 'turno_tarde':'1pm-9pm'}, 'gerente':'china'},
   
  {'ruc':'10896325471', 'nombre': 'Restaurante Sabor del Mar', 'categoria':['restaurant'],
   'horario_atencion':{'turno_mañana':'11am-4pm', 'turno_tarde':'6pm-11pm'}, 'gerente':'edwin'},
   
  {'ruc':'10236587452', 'nombre': 'Farmacia Santa Lucia', 'categoria':['farmacia'],
   'horario_atencion':{'turno_mañana':'10am-2pm', 'turno_tarde':'5pm-10pm'}, 'gerente':'nadine'},
   
  {'ruc':'10289561743', 'nombre': 'Minimarket Abierto 24/7', 'categoria':['abarrotes', 'bodega'],
   'horario_atencion':{'turno_mañana':'0am-12pm', 'turno_tarde':'1pm-12am'}, 'gerente':'crhistian'}
]

class Tienda:

  def __init__(self, tiendas):
    self.tiendas = tiendas

  def filtrar_por_gerente(self, gerente):
    return [tienda for tienda in self.tiendas if tienda['gerente'] == gerente]
tiendas_obj = Tienda(tiendas)

tiendas_obj.filtrar_por_gerente('manuel')
tiendas_obj.mas_de_dos_categorias() 
tiendas_obj.solo_nombre_y_ruc()
  
def mas_de_dos_categorias(self):
    return [tienda for tienda in self.tiendas if len(tienda['categoria']) > 2]
  
def solo_nombre_y_ruc(self):
    return [{k: v for k, v in tienda.items() if k in ['nombre', 'ruc']} 
            for tienda in self.tiendas]