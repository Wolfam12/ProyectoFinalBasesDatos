from tkinter import Tk,Button,Entry,Label,ttk,PhotoImage
from tkinter import StringVar, Scrollbar,Frame,messagebox 
from conexion_sqlite import Comunicacion
from time import strftime
from datetime import datetime
from random import randint

class Envio(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.Direccion = StringVar()
        self.Celular = StringVar()
        self.Correo = StringVar()
        self.NombreCliente = StringVar()
        self.NumeroGuia = StringVar()
        self.EstadoEnvio = StringVar()
        self.FechaEnvio = StringVar()
        self.FechaEntrega = StringVar()

        self.master.columnconfigure(0,weight=1)
        self.master.rowconfigure(0,weight=1)
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

        self.frame_uno.columnconfigure([0,1,2,3,4,5,6], weight=1)
        self.frame_uno.rowconfigure([0,1,2,3,4,5,6,7,8], weight=1)
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.rowconfigure(0, weight=1)

        Label(self.frame_uno, text='Opciones',bg='white',fg='black',font=('Kaufmann BT',13,'bold')).grid(column=2,row=0)
        
        Label(self.frame_uno, text='Agregar y actualizar datos', bg='white', fg='black', font=('Kaufmann BT',13,'bold')).grid(columnspan=2, column=0,row=0,pady=5)
        
        # labels para el envio
        Label(self.frame_uno, text = 'Direccion',bg='white', fg='black', font=('Rockwell',13,'bold')).grid(column=0, row=1, pady=5)
        
        Label(self.frame_uno, text = 'Celular',bg='white', fg='black', font=('Rockwell',13,'bold')).grid(column=0, row=2, pady=5)

        Label(self.frame_uno, text = 'Correo',bg='white', fg='black', font=('Rockwell',13,'bold')).grid(column=0, row=3, pady=5)

        Label(self.frame_uno, text = 'Nombre cliente',bg='white', fg='black', font=('Rockwell',13,'bold')).grid(column=0, row=4, pady=5)

        Label(self.frame_uno, text = 'Numero guia',bg='white', fg='black', font=('Rockwell',13,'bold')).grid(column=0, row=5, pady=5)

        Label(self.frame_uno, text = 'Estado envio',bg='white', fg='black', font=('Rockwell',13,'bold')).grid(column=0, row=6, pady=5)

        Label(self.frame_uno, text = 'Fecha envio',bg='white', fg='black', font=('Rockwell',13,'bold')).grid(column=0, row=7, pady=5)
        
        Label(self.frame_uno, text = 'Fecha entrega',bg='white', fg='black', font=('Rockwell',13,'bold')).grid(column=0, row=8, pady=5)

        # entradas para el envio
        Entry(self.frame_uno, textvariable=self.Direccion, font=('Rockwell',12)).grid(column=1, row=1)

        Entry(self.frame_uno, textvariable=self.Celular, font=('Rockwell',12)).grid(column=1, row=2)
          
        Entry(self.frame_uno, textvariable=self.Correo, font=('Rockwell',12)).grid(column=1, row=3)

        Entry(self.frame_uno, textvariable=self.NombreCliente, font=('Rockwell',12)).grid(column=1, row=4)

        Entry(self.frame_uno, textvariable=self.NumeroGuia, font=('Rockwell',12)).grid(column=1, row=5)

        Entry(self.frame_uno, textvariable=self.EstadoEnvio, font=('Rockwell',12)).grid(column=1, row=6)

        Entry(self.frame_uno, textvariable=self.FechaEnvio, font=('Rockwell',12)).grid(column=1, row=7)

        Entry(self.frame_uno, textvariable=self.FechaEntrega, font=('Rockwell',12)).grid(column=1, row=8)
        
         # Botones principales(¿?)
        Button(self.frame_uno, text='Agregar datos', font=('Rockwell',9,'bold'), command= self.agregar_datos_envio).grid(column=2,row=2,pady=5,padx=5)
        Button(self.frame_uno, text='Limpiar campos', font=('Rockwell',9,'bold'), command= self.limpiar_campos_envio).grid(column=2,row=3,pady=5,padx=5)
        Button(self.frame_uno, text='Eliminar registro', font=('Rockwell',9,'bold'), command= self.eliminar_datos_envio).grid(column=2,row=4,pady=5,padx=5)
        Button(self.frame_uno, text='Actualizar registro', font=('Rockwell',9,'bold'), command= self.actualizar_registro).grid(column=2,row=5,pady=5,padx=5)
        Button(self.frame_uno, text='cerrar', font=('Rockwell',9,'bold')).grid(column=2,row=6,pady=5,padx=5)
        
        #tabla
        self.tabla = ttk.Treeview(self.frame_dos)
        self.tabla.grid(column=0,row=0,sticky='nsew')
        ladox=ttk.Scrollbar(self.frame_dos, orient='horizontal',command=self.tabla.xview)
        ladox.grid(column=0,row=1,sticky='ew')

        ladoy=ttk.Scrollbar(self.frame_dos, orient='vertical',command=self.tabla.yview)
        ladox.grid(column=0,row=1,sticky='ns')
        self.tabla.configure(xscrollcommand=ladox.set,yscrollcommand=ladoy.set)
        datos =(self.base_datos.mostarDatosEnvio())

        for dato in datos: {
            self.tabla.insert('',0, text = dato[0], values= (dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8],dato[9]))
        }
        
        #datos tabla envio
        self.tabla['columns'] = ('Direccion','Celular','Correo','NombreCliente','NumeroGuia','EstadoEnvio','FechaEnvio','FechaEntrega','IdFactura')
        
        self.tabla.column('#0',minwidth=100,width=120,anchor='center')
        self.tabla.column('Direccion',minwidth=100,width=120,anchor='center')
        self.tabla.column('Celular',minwidth=100,width=120,anchor='center')
        self.tabla.column('Correo',minwidth=100,width=120,anchor='center')
        self.tabla.column('NombreCliente',minwidth=100,width=120,anchor='center')
        self.tabla.column('NumeroGuia',minwidth=100,width=120,anchor='center')
        self.tabla.column('EstadoEnvio',minwidth=100,width=120,anchor='center')
        self.tabla.column('FechaEnvio',minwidth=100,width=120,anchor='center')
        self.tabla.column('FechaEntrega',minwidth=100,width=120,anchor='center')
        self.tabla.column('IdFactura',minwidth=100,width=120,anchor='center')

        self.tabla.heading('#0',text='Id',anchor='center')
        self.tabla.heading('Direccion',text='Direccion',anchor='center')
        self.tabla.heading('Celular',text='Celular',anchor='center')
        self.tabla.heading('Correo',text='Correo',anchor='center')
        self.tabla.heading('NombreCliente',text='NombreCliente',anchor='center')
        self.tabla.heading('NumeroGuia',text='NumeroGuia',anchor='center')
        self.tabla.heading('EstadoEnvio',text='EstadoEnvio',anchor='center')
        self.tabla.heading('FechaEnvio',text='FechaEnvio',anchor='center')
        self.tabla.heading('FechaEntrega',text='FechaEntrega',anchor='center')
        self.tabla.heading('IdFactura',text='IdFactura',anchor='center')

        self.tabla.bind("<<TreeviewSelect>>",self.obtener_fila_envio)
        self.tabla.bind("<<Double-1>>", self.eliminar_datos_envio)

    def obtener_fila_envio(self,event):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        self.Direccion.set(self.data['values'][0])
        self.Celular.set(self.data['values'][1])
        self.Correo.set(self.data['values'][2])
        self.NombreCliente.set(self.data['values'][3])
        self.NumeroGuia.set(self.data['values'][4])
        self.EstadoEnvio.set(self.data['values'][5])
        self.FechaEnvio.set(self.data['values'][6])
        self.FechaEntrega.set(self.data['values'][7])

    def eliminar_datos_envio(self):
        self.limpiar_campos_envio()
        item = self.tabla.selection()[0]
        x = messagebox.askquestion('Informacion','¿Está seguro?')
        if x == 'yes':
            self.tabla.delete(item)
            self.base_datos.EliminarDatosEnvio(self.data['text'])

    def limpiar_campos_envio(self):
        self.Direccion.set('')
        self.Celular.set('')
        self.Correo.set('')
        self.NombreCliente.set('')
        self.NumeroGuia.set('')
        self.EstadoEnvio.set('')
        self.FechaEnvio.set('')
        self.FechaEntrega.set('')

    def agregar_datos_envio(self):
        Direccion = self.Direccion.get()
        Celular = self.Celular.get()
        Correo = self.Correo.get()
        NombreCliente = self.NombreCliente.get()
        NumeroGuia = self.NumeroGuia.get()
        EstadoEnvio = self.EstadoEnvio.get()
        FechaEnvio = self.FechaEnvio.get()
        FechaEntrega = self.FechaEntrega.get()
        idFactura = randint(10**(3-1), (10**3)-1)
        datos = (Direccion, Celular, Correo, NombreCliente, NumeroGuia, EstadoEnvio, FechaEnvio, FechaEntrega, idFactura)
        if Direccion and Celular and Correo and NombreCliente and NumeroGuia and EstadoEnvio and FechaEnvio and FechaEntrega and idFactura !='':
            self.base_datos.insertarDatosEnvio(Direccion,Celular,Correo,NombreCliente,NumeroGuia,EstadoEnvio,FechaEnvio,FechaEntrega,idFactura)
            self.datos=(self.base_datos.mostarDatosEnvio())
            self.tabla.insert('',0, text = self.datos[-1][0], values= (Direccion,Celular,Correo,NombreCliente,NumeroGuia,EstadoEnvio,FechaEnvio,FechaEntrega,idFactura))
            self.limpiar_campos_Envio()
            
    def actualizar_tabla(self):
        self.limpiar_campos_envio()
        datos = self.base_datos.mostrarDatosEnvio()
        self.table.delete(*self.tabla.get_children())
        i=-1
        for dato in datos:
            i=i+1
            self.tabla.insert('',i,text=datos[i][1:2][0],values=datos[i][2:5])
            
    def actualizar_datos_envio(self):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        Direccion = self.data['values'][0]
        datos = self.base_datos.mostrarDatosEnvio()
        for fila in datos:
            Id = fila[0]
            Direccion_bd = fila[1]
            if Direccion_bd == Direccion:
                if Id != None:
                    Direccion = self.Direccion.get()
                    Celular = self.Celular.get()
                    Correo = self.Correo.get()
                    NombreCliente = self.NombreCliente.get()
                    NumeroGuia = self.NumeroGuia.get()
                    EstadoEnvio = self.EstadoEnvio.get()
                    FechaEnvio = self.FechaEnvio.get()
                    FechaEntrega = self.FechaEntrega.get()
                    idFactura = self.idFactura.get()
                    if Direccion and Celular and Correo and NombreCliente and NumeroGuia and EstadoEnvio and FechaEnvio and FechaEntrega and idFactura !='':
                        self.base_datos.ActualizaDatosEnvio(Direccion,Celular,Correo,NombreCliente,NumeroGuia,EstadoEnvio,FechaEnvio,FechaEntrega,idFactura)
                        self.tabla.delete(*self.tabla.get_children())
                        datos=self.base_datos.mostarDatosEnvio()
                        i=-1
                        for dato in datos:
                            i=i+1
                            self.tabla.insert('',i,text=datos[i][1:2][0], values=datos[i][2:5])
        
    def actualizar_registro(self):
        
        item = self.tabla.selection()[0]
        x = messagebox.askquestion('Informacion','¿Está seguro?')
        if x == 'yes':
            Direccion = self.Direccion.get()
            Celular = self.Celular.get()
            Correo = self.Correo.get()
            NombreCliente = self.NombreCliente.get()
            NumeroGuia = self.NumeroGuia.get()
            EstadoEnvio = self.EstadoEnvio.get()
            FechaEnvio = self.FechaEnvio.get()
            FechaEntrega = self.FechaEntrega.get()
            idFactura = self.idFactura.get()
            id = self.data['text']
            self.base_datos.ActualizaDatosEnvio(self.data['text'],Direccion,Celular,Correo,NombreCliente,NumeroGuia,EstadoEnvio,FechaEnvio,FechaEntrega,idFactura)
            self.tabla.insert('',0, text = id, values= (Direccion,Celular,Correo,NombreCliente,NumeroGuia,EstadoEnvio,FechaEnvio,FechaEntrega,idFactura))
            self.tabla.delete(item)
            self.actualizar_tabla()
            self.limpiar_campos_inventario()

if __name__ == "__main__":
    ventana = Tk()
    ventana.title('Chapicalzado')
    ventana.minsize(height=400, width=600)
    ventana.geometry('1090x850')
    app = Envio(ventana)
    app.mainloop()
