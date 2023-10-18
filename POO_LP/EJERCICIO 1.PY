# Crear un sistema par la gestion control de stock de productos
# Entidad→ entitis
# La base de datos sobre la que voy a trabajar
# formas normales  ( normalizacion de  de base de datos )
productos=[{
            'id':1,
            'codigo':'2023-A',
            'nombre':'Arroz',
            'descripcion':'costeño costal x 100 k',
            'stock':5,
            'unidad':'costales',
            'precio':125,
            'moneda':'soles'
        }
        ]
#caso de uso
class Producto:
    # Atributos de instancia
    def __init__(self,nombre,descripcion,stock,unidad,precio,moneda='soles'):
    
        self.nombre=nombre
        self.descripcion=descripcion
        self.stock=stock
        self.unidad=unidad
        self.precio=precio
        self.moneda=moneda
    
    
    # creacion de metodos
    def mostrar_productos(self):
        mensaje=f"""
        tienes {len(productos)} productos
        los productos son:
        {productos}
        """
        return mensaje
    def registrar_producto(self):
        nuevo_id=len(productos)+1
        producto_nuevo={
            'id':nuevo_id,
            'codigo':self.codigo , 
            'nombre':self.nombre,
            'descripcion':self.descripcion,
            'stock':self.tock,
            'unidad':self.unidad,
            'precio':self.recio,
            'moneda':self.moneda 
            
        }
        
        registro_producto=productos.append(producto_nuevo)
        return f" El sigiente producto se registro exitosamente(producto_nuevo)"
       
    def mostrar_producto(self,id):
        producto_buscar=productos(id-1)
        return producto_buscar
    
    def eliminar_producto(self,id):
        producto_eliminar=productos.pop(id-1)
        return  f"El sigiente producto fue eliminada{producto_eliminar}"
    
    def actualizar_producto(self,id,clave,valor):
        ol =valor
        producto_actualizar=list(filter(lambda el : el[clave] == id,productos))[0].update({clave,valor})
        return " se actualizo el producto"
    
    #def actualizar_producto(self,id,clave,valor):
        #producto_actualizar=list(filter(lambda el:el['id']==2,productos))
        #return producto_actualizar
        
        
    # list→ funcion para  crear lista
  # progrmacion funcional en python  retorna una lista nueva con el elemento que sea true
  # metodo funcional filter 
  # funciones anonimas o autoejecutadas en python , se les conoce como funciones → lamda → una funcion anonima
 # su uso lambda a,b:return a+b  # esta funcion no se llama
 # suma=lamdaa,b:return a+b # para ejecutar esta funcion nesesario llamar ala variable suma
 #suma(3,4)## 
  
  
prod=Producto('aceite','extra','2','botella x litro','12.50')
print=(prod.registar_producto())
print=(prod.mostrar_productos())
# print=(prod.registar_producto())
# print=(prod.eliminar_producto())
# print=(prod.mostrar_producto())
print=(prod.actualizar_producto('125','codigo',130))
print=(prod.mostrar_productos())

    
    