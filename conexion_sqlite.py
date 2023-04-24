import sqlite3

class Comunicacion():
    def __init__(self):
        self.conexion = sqlite3.connect('Chapicalzado.db')
        print('Me voy a ganar la beca')
    def insertarDatosInventario(self,Referencia,CantidadDisponible,CantidadVendida,FechaActualizacion,Costo,Proveedor,PrecioVenta,Producto): 
        cursor=self.conexion.cursor() 
        bd= ''' INSERT INTO Inventario (Referencia,CantidadDisponible,CantidadVendida,FechaActualizacion,Costo,Proveedor,PrecioVenta,Producto)
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}')'''.format(Referencia,CantidadDisponible,CantidadVendida,FechaActualizacion,Costo,Proveedor,PrecioVenta,Producto)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    def mostarDatosInventario(self):
        cursor=self.conexion.cursor()
        bd="SELECT * FROM Inventario "
        cursor.execute(bd)
        datos=cursor.fetchall()
        print(datos) 
    def EliminarDatosInventario(self,idInventario):
        cursor=self.conexion.cursor()
        bd='''DELETE FROM Inventario WHERE idInventario = '{}' '''.format(idInventario)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    def ActualizaDatosInventario(self,idInventario,Referencia,CantidadDisponible,CantidadVendida,FechaActualizacion,Costo,Proveedor,PrecioVenta,Producto):
         cursor=self.conexion.cursor() 
         bd= ''' UPDATE FROM Inventario  SET Referencia ='{}', Referencia ='{}',CantidadDisponible ='{}',CantidadVendida ='{}',FechaActualizacion ='{}',Costo ='{}',Proveedor ='{}',PrecioVenta ='{}',Producto ='{}' WHERE idInventario ='{}' ''' .format(Referencia,CantidadDisponible,CantidadVendida,FechaActualizacion,Costo,Proveedor,PrecioVenta,Producto,idInventario)
         cursor.execute(bd)
         dato=cursor.rowcount
         self.conexion.commit()
         cursor.close() 
         return dato


my_message = Comunicacion()
my_message.__init__
my_message.insertarDatosInventario("5412",50,2,"12/04/2002",120000,"NIKE",200000,"TENIS WALKING")

