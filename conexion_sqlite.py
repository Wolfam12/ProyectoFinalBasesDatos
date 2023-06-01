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
        return datos
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
        return datos
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
    def insertarDatosEmpleado(self,CedulaEmpleado,Email,Salario,TipoEmpleado): 
        cursor=self.conexion.cursor() 
        bd= ''' INSERT INTO Empleado (CedulaEmpleado,Email,Salario,TipoEmpleado)
        VALUES('{}','{}','{}','{}')'''.format(CedulaEmpleado,Email,Salario,TipoEmpleado)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    def mostarDatosEmpleado(self):
        cursor=self.conexion.cursor()
        bd="SELECT * FROM Empleado "
        cursor.execute(bd)
        datos=cursor.fetchall()
        print(datos)
        return datos
    def EliminarDatosEmpleado(self,idEmpleado):
        cursor=self.conexion.cursor()
        bd='''DELETE FROM Empleado WHERE idEmpleado = '{}' '''.format(idEmpleado)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    def ActualizaDatosEmpleado(self,idEmpleado,CedulaEmpleado,Email,Salario,TipoEmpleado):
         cursor=self.conexion.cursor() 
         bd=''' UPDATE  Empleado  SET  CedulaEmpleado ='{}',Email ='{}',Salario ='{}',TipoEmpleado ='{}' WHERE idEmpleado ='{}' ''' .format(CedulaEmpleado,Email,Salario,TipoEmpleado,idEmpleado)
         cursor.execute(bd)
         dato=cursor.rowcount
         self.conexion.commit()
         cursor.close() 
         return dato
    
    def insertarDatosEnvio(self,Direccion,Celular,Correo,NombreCliente,NumeroGuia,EstadoEnvio,FechaEnvio,FechaEntrega,idFActura): 
        cursor=self.conexion.cursor() 
        bd= ''' INSERT INTO Envio (Direccion,Celular,Correo,NombreCliente,NumeroGuia,EstadoEnvio,FechaEnvio,FechaEntrega,idFActura)
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(Direccion,Celular,Correo,NombreCliente,NumeroGuia,EstadoEnvio,FechaEnvio,FechaEntrega,idFActura)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    def mostarDatosEnvio(self):
        cursor=self.conexion.cursor()
        bd="SELECT * FROM Envio "
        cursor.execute(bd)
        datos=cursor.fetchall()
        print(datos)
        return datos
    def EliminarDatosEnvio(self,idEnvio):
        cursor=self.conexion.cursor()
        bd='''DELETE FROM Envio WHERE idEnvio = '{}' '''.format(idEnvio)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    def ActualizaDatosEnvio(self,idEnvio,Direccion,Celular,Correo,NombreCliente,NumeroGuia,EstadoEnvio,FechaEnvio,FechaEntrega,idFActura):
         cursor=self.conexion.cursor() 
         bd= ''' UPDATE  Envio  SET Direccion ='{}',Celular ='{}',Correo ='{}',NombreCliente ='{}',NumeroGuia ='{}',EstadoEnvio ='{}',FechaEnvio ='{}',FechaEntrega ='{}',idFActura ='{}' WHERE idEnvio ='{}' ''' .format(Direccion,Celular,Correo,NombreCliente,NumeroGuia,EstadoEnvio,FechaEnvio,FechaEntrega,idFActura,idEnvio)
         cursor.execute(bd)
         dato=cursor.rowcount
         self.conexion.commit()
         cursor.close() 
         return dato

    def insertarDatosSede(self,Direccion,Administrador,idAdministrador,CelularSede): 
        cursor=self.conexion.cursor() 
        bd= ''' INSERT INTO Sede (Direccion,Administrador,idAdministrador,CelularSede)
        VALUES('{}','{}','{}','{}')'''.format(Direccion,Administrador,idAdministrador,CelularSede)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    def mostarDatosSede(self):
        cursor=self.conexion.cursor()
        bd="SELECT * FROM Sede "
        cursor.execute(bd)
        datos=cursor.fetchall()
        print(datos)
        return datos
    def EliminarDatosSede(self,idSede):
        cursor=self.conexion.cursor()
        bd='''DELETE FROM Sede WHERE idSede = '{}' '''.format(idSede)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    def ActualizaDatosSede(self,idSede,Direccion,Administrador,idAdministrador,CelularSede):
         cursor=self.conexion.cursor() 
         bd=''' UPDATE  Sede  SET  Direccion ='{}',Administrador ='{}',idAdministrador ='{}',CelularSede ='{}' WHERE idSede ='{}' ''' .format(Direccion,Administrador,idAdministrador,CelularSede,idSede)
         cursor.execute(bd)
         dato=cursor.rowcount
         self.conexion.commit()
         cursor.close() 
         return dato
       



my_message = Comunicacion()
my_message.__init__
my_message.ActualizaDatosSede(1,"4","77",85,741)
my_message.mostarDatosSede





