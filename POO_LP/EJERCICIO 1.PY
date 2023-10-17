# Crear un sistema par la gestion control de stock de productos
# Entidad→ entitis
# La base de datos sobre la que voy a trabajar
# formas normales  ( normalizacion de  de base de datos )
productos=[{'id':1,
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
            'id:nuevo_id',
            'nombre:self_nombre',
            'descripcion:self_descripcion'
            'stock:self_stock',
            'unidad:self_unidad',
            'precio:self_precio',
            'moneda:self_moneda'   
            
        }
        
        registro_producto=productos.append(producto_nuevo)
        return f" El sigiente producto se registro exitosamente(producto_nuevo)"
       
    def mostrar_producto(self,id):
        producto_buscar=productos(id-1)
        return producto_buscar
    
    def eliminar_producto(self,id):
        producto_eliminar=productos.pop(id-1)
        return  f"El sigiente producto fue eliminada{producto_eliminar}"
    
    
    def actualizar_producto(self,id):
     pass
    
prod=Producto('aceite','extra','2','botella x litro','12.50')
print=(prod.registar_producto())
print=(prod.mostrar_producto())
print=(prod.registar_producto())
print=(prod.eliminar_producto())
print=(prod.mostrar_producto())


    
    