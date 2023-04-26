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
         bd= ''' UPDATE  Inventario  SET Referencia ='{}',CantidadDisponible ='{}',CantidadVendida ='{}',FechaActualizacion ='{}',Costo ='{}',Proveedor ='{}',PrecioVenta ='{}',Producto ='{}' WHERE idInventario ='{}' ''' .format(Referencia,CantidadDisponible,CantidadVendida,FechaActualizacion,Costo,Proveedor,PrecioVenta,Producto,idInventario)
         cursor.execute(bd)
         dato=cursor.rowcount
         self.conexion.commit()
         cursor.close() 
         return dato
    def insertarDatosClientes(self,Cedula,NombreCliente,CorreoElectronico,Celular,FechaNacimiento): 
        cursor=self.conexion.cursor() 
        bd= ''' INSERT INTO Clientes (Cedula,NombreCliente,CorreoElectronico,Celular,FechaNacimiento)
        VALUES('{}','{}','{}','{}','{}')'''.format(Cedula,NombreCliente,CorreoElectronico,Celular,FechaNacimiento)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    def mostarDatosClientes(self):
        cursor=self.conexion.cursor()
        bd="SELECT * FROM Clientes "
        cursor.execute(bd)
        datos=cursor.fetchall()
        print(datos) 
    def EliminarDatosClientes(self,IdCliente):
        cursor=self.conexion.cursor()
        bd='''DELETE FROM Clientes WHERE IdCliente = '{}' '''.format(IdCliente)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    def ActualizaDatosClientes(self,IdCliente,Cedula,NombreCliente,CorreoElectronico,Celular,FechaNacimiento):
         cursor=self.conexion.cursor() 
         bd=''' UPDATE  Clientes  SET Cedula ='{}', NombreCliente ='{}',CorreoElectronico ='{}',Celular ='{}',FechaNacimiento ='{}' WHERE IdCliente ='{}' ''' .format(Cedula,NombreCliente,CorreoElectronico,Celular,FechaNacimiento,IdCliente)
         cursor.execute(bd)
         dato=cursor.rowcount
         self.conexion.commit()
         cursor.close() 
         return dato


my_message = Comunicacion()
my_message.__init__

my_message.mostarDatosClientes()


