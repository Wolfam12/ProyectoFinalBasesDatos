
from tkinter import Tk,Button,Entry,Label,ttk,PhotoImage
from tkinter import StringVar, Scrollbar,Frame,messagebox 
from conexion_sqlite import Comunicacion
from time import strftime
from datetime import datetime
from random import randint

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.Referencia = StringVar()
        self.CantidadDisponible = StringVar()
        self.CantidadVendida = StringVar()
        self.FechaActualizacion = StringVar()
        self.Costo = StringVar()
        self.Proveedor = StringVar()
        self.PrecioVenta = StringVar()
        self.Producto = StringVar()

        self.master.columnconfigure(0,weight=1)
        self.master.rowconfigure(0,weight=1)
        self.master.columnconfigure(0,weight=1)
        self.master.columnconfigure(1,weight=5)
        self.base_datos=Comunicacion()
        
        self.widgets()

    def widgets(self):
        self.frame_uno = Frame(self.master, bg='white', height=200, width=800)
        self.frame_uno.grid(column =0, row=0, sticky='nsew')
        self.frame_dos = Frame(self.master, bg='white',height=300,width=800)
        self.frame_dos.grid(column=0, row=1, sticky='nsew')

        self.frame_uno.columnconfigure([0,1,2,3,4,5], weight=1)
        self.frame_uno.rowconfigure([0,1,2,3,4,5,6,7], weight=1)
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.rowconfigure(0, weight=1)
        
        Label(self.frame_uno, text='Opciones',bg='white',fg='black',font=('Kaufmann BT',13,'bold')).grid(column=2,row=0)
        
        Label(self.frame_uno, text='Agregar y actualizar datos', bg='white', fg='black', font=('Kaufmann BT',13,'bold')).grid(columnspan=2, column=0,row=0,pady=5)
        
        # labels para el inventario
        Label(self.frame_uno, text = 'Referencia',bg='white', fg='black', font=('Rockwell',13,'bold')).grid(column=0, row=1, pady=5)
        
        Label(self.frame_uno, text = 'Producto',bg='white', fg='black', font=('Rockwell',13,'bold')).grid(column=0, row=2, pady=5)

        Label(self.frame_uno, text = 'Cantidad',bg='white', fg='black', font=('Rockwell',13,'bold')).grid(column=0, row=3, pady=5)

        Label(self.frame_uno, text = 'Cantidad Vendida',bg='white', fg='black', font=('Rockwell',13,'bold')).grid(column=0, row=4, pady=5)

        Label(self.frame_uno, text = 'Costo',bg='white', fg='black', font=('Rockwell',13,'bold')).grid(column=0, row=5, pady=5)

        Label(self.frame_uno, text = 'Precio de venta',bg='white', fg='black', font=('Rockwell',13,'bold')).grid(column=0, row=6, pady=5)

        Label(self.frame_uno, text = 'Proveedor',bg='white', fg='black', font=('Rockwell',13,'bold')).grid(column=0, row=7, pady=5)
        
        # entradas para el inventario
        Entry(self.frame_uno, textvariable=self.Referencia, font=('Rockwell',12)).grid(column=1, row=1)

        Entry(self.frame_uno, textvariable=self.Producto, font=('Rockwell',12)).grid(column=1, row=2)
          
        Entry(self.frame_uno, textvariable=self.CantidadDisponible, font=('Rockwell',12)).grid(column=1, row=3)

        Entry(self.frame_uno, textvariable=self.CantidadVendida, font=('Rockwell',12)).grid(column=1, row=4)

        Entry(self.frame_uno, textvariable=self.Costo, font=('Rockwell',12)).grid(column=1, row=5)

        Entry(self.frame_uno, textvariable=self.PrecioVenta, font=('Rockwell',12)).grid(column=1, row=6)

        Entry(self.frame_uno, textvariable=self.Proveedor, font=('Rockwell',12)).grid(column=1, row=7)


        # Botones principales(¿?)
        Button(self.frame_uno, text='Agregar datos', font=('Rockwell',9,'bold'),command= self.agregar_datos_inventario).grid(column=2,row=2,pady=5,padx=5)
        Button(self.frame_uno, text='Limpiar campos', font=('Rockwell',9,'bold'),command=self.limpiar_campos_inventario).grid(column=2,row=3,pady=5,padx=5)
        Button(self.frame_uno, text='Eliminar registro', font=('Rockwell',9,'bold'),command=self.eliminar_datos_inventario).grid(column=2,row=4,pady=5,padx=5)
        Button(self.frame_uno, text='Actualizar registro', font=('Rockwell',9,'bold'),command=self.actualizar_registro).grid(column=2,row=5,pady=5,padx=5)
        Button(self.frame_uno, text='cerrar', font=('Rockwell',9,'bold'),command=self).grid(column=2,row=6,pady=5,padx=5)
        
        #tabla
        self.tabla = ttk.Treeview(self.frame_dos)
        self.tabla.grid(column=0,row=0,sticky='nsew')
        ladox=ttk.Scrollbar(self.frame_dos, orient='horizontal',command=self.tabla.xview)
        ladox.grid(column=0,row=1,sticky='ew')

        ladoy=ttk.Scrollbar(self.frame_dos, orient='vertical',command=self.tabla.yview)
        ladox.grid(column=0,row=1,sticky='ns')
        self.tabla.configure(xscrollcommand=ladox.set,yscrollcommand=ladoy.set)
        datos =(self.base_datos.mostarDatosInventario())

        for dato in datos: {
            self.tabla.insert('',0, text = dato[0], values= (dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8]))
        }

        
        
        #datos tabla inventario
        self.tabla['columns'] = ('Referencia','CantidadDisponible','CantidadVendida','FechaActualizacion','Costo','Proveedor','PrecioVenta','Producto')
        
        self.tabla.column('#0',minwidth=100,width=120,anchor='center')
        self.tabla.column('Referencia',minwidth=100,width=120,anchor='center')
        self.tabla.column('CantidadDisponible',minwidth=100,width=120,anchor='center')
        self.tabla.column('CantidadVendida',minwidth=100,width=120,anchor='center')
        self.tabla.column('FechaActualizacion',minwidth=100,width=120,anchor='center')
        self.tabla.column('Costo',minwidth=100,width=120,anchor='center')
        self.tabla.column('Proveedor',minwidth=100,width=120,anchor='center')
        self.tabla.column('PrecioVenta',minwidth=100,width=120,anchor='center')
        self.tabla.column('Producto',minwidth=100,width=120,anchor='center')
        
        self.tabla.heading('#0',text='Id',anchor='center')
        self.tabla.heading('Referencia',text='Referencia',anchor='center')
        self.tabla.heading('CantidadDisponible',text='Disponible',anchor='center')
        self.tabla.heading('CantidadVendida',text='Vendido',anchor='center')
        self.tabla.heading('FechaActualizacion',text='Fecha',anchor='center')
        self.tabla.heading('Costo',text='Costo',anchor='center')
        self.tabla.heading('Proveedor',text='Proveedor',anchor='center')
        self.tabla.heading('PrecioVenta',text='PrecioVenta',anchor='center')
        self.tabla.heading('Producto',text='Producto',anchor='center')
        
        self.tabla.bind("<<TreeviewSelect>>",self.obtener_fila_inventario)
        self.tabla.bind("<<Double-1>>", self.eliminar_datos_inventario)

    def obtener_fila_inventario(self,event):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        self.Referencia.set(self.data['values'][0])
        self.Producto.set(self.data['values'][7])
        self.CantidadDisponible.set(self.data['values'][1])
        self.CantidadVendida.set(self.data['values'][2])
        self.FechaActualizacion.set(self.data['values'][3])
        self.Costo.set(self.data['values'][4])
        self.Proveedor.set(self.data['values'][5])
        self.PrecioVenta.set(self.data['values'][6])

    def eliminar_datos_inventario(self):
       
        self.limpiar_campos_inventario()
        item = self.tabla.selection()[0]
        x = messagebox.askquestion('Informacion','¿Está seguro?')
        if x == 'yes':
            self.tabla.delete(item)
            self.base_datos.EliminarDatosInventario(self.data['text'])

    def limpiar_campos_inventario(self):
        self.Referencia.set('')
        self.Producto.set('')
        self.CantidadDisponible.set('')
        self.CantidadVendida.set('')
        self.FechaActualizacion.set('')
        self.Costo.set('')
        self.Proveedor.set('')
        self.PrecioVenta.set('')
    
    def agregar_datos_inventario(self):
        Referencia = self.Referencia.get()
        Producto = self.Producto.get()
        Cantidad = self.CantidadDisponible.get()
        cantidadV = self.CantidadVendida.get()
        Costo = self.Costo.get()
        Proveedor = self.Proveedor.get()
        PrecioVenta = self.PrecioVenta.get()
        if Producto and Cantidad and Costo and Proveedor and PrecioVenta !='':
            self.base_datos.insertarDatosInventario(Referencia,Cantidad,cantidadV,datetime.now().date(),Costo,Proveedor,PrecioVenta,Producto)
            self.datos=(self.base_datos.mostarDatosInventario())
            self.tabla.insert('',0, text = self.datos[-1][0], values= (Referencia,Cantidad,cantidadV,datetime.now().date(),Costo,Proveedor,PrecioVenta,Producto))
            self.limpiar_campos_inventario()
   
        
    def actualizar_tabla(self):
        self.limpiar_campos()
        datos = self.base_datos.mostrarDatosInventario()
        self.table.delete(*self.tabla.get_children())
        i=-1
        for dato in datos:
            i=i+1
            self.tabla.insert('',i,text=datos[i][1:2][0],values=datos[i][2:5])
    
    def actualizar_datos_inventario(self):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        Referencia = self.data['values'][0]
        datos = self.base_datos.mostrarDatosInventario()
        for fila in datos:
            Id = fila[0]
            Referencia_bd = fila[1]
            if Referencia_bd == Referencia:
                if Id != None:
                    Referencia = self.Referencia.get()
                    Producto = self.Producto.get()
                    Cantidad = self.CantidadDisponible.get()
                    cantidadV = self.CantidadVendida.get()
                    Costo = self.Costo.get()
                    Proveedor = self.Proveedor.get()
                    PrecioVenta = self.PrecioVenta.get()
                    if Referencia and Producto and Cantidad and cantidadV and Costo and Proveedor and PrecioVenta != '':
                        self.base_datos.ActualizaDatosInventario(Id,Referencia,Producto,Cantidad,cantidadV,Costo,Proveedor,PrecioVenta)
                        self.tabla.delete(*self.tabla.get_children())
                        datos = self.base_datos.mostrarDatosInventario()
                        i=-1
                        for dato in datos:
                            i=i+1
                            self.tabla.insert('',i,text=datos[i][1:2][0], values=datos[i][2:5])


    def actualizar_registro(self):
        
        item = self.tabla.selection()[0]
        x = messagebox.askquestion('Informacion','¿Está seguro?')
        if x == 'yes':
            Referencia = self.Referencia.get()
            Producto = self.Producto.get()
            Cantidad = self.CantidadDisponible.get()
            cantidadV = self.CantidadVendida.get()
            Costo = self.Costo.get()
            Proveedor = self.Proveedor.get()
            PrecioVenta = self.PrecioVenta.get()
            id = self.data['text']
            self.base_datos.ActualizaDatosInventario(self.data['text'],Referencia,Cantidad,cantidadV,datetime.now().date(),Costo,Proveedor,PrecioVenta,Producto)
            self.tabla.insert('',0, text = id, values= (Referencia,Cantidad,cantidadV,datetime.now().date(),Costo,Proveedor,PrecioVenta,Producto))
            self.tabla.delete(item)
            self.actualizar_datos_inventario()
            self.limpiar_campos_inventario()
        
if __name__ == "__main__":
    ventana = Tk()
    ventana.title('Chapicalzado')
    ventana.minsize(height=400, width=600)
    ventana.geometry('1090x850')
    app = App(ventana)
    app.mainloop()
