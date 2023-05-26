
from tkinter import Tk,Button,Entry,Label,ttk,PhotoImage
from tkinter import StringVar, Scrollbar,Frame,messagebox 
from conexion_sqlite import Comunicacion
from time import strftime
from datetime import datetime
from random import randint

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.cedula= StringVar()
        self.Nombre = StringVar()
        self.Correo = StringVar()
        self.Celular = StringVar()
        self.FechaN = StringVar()
       

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
        Label(self.frame_uno, text = 'Cedula',bg='white', fg='black', font=('Rockwell',13,'bold')).grid(column=0, row=1, pady=5)
        
        Label(self.frame_uno, text = 'Nombre',bg='white', fg='black', font=('Rockwell',13,'bold')).grid(column=0, row=2, pady=5)

        Label(self.frame_uno, text = 'Correo',bg='white', fg='black', font=('Rockwell',13,'bold')).grid(column=0, row=3, pady=5)

        Label(self.frame_uno, text = 'celular',bg='white', fg='black', font=('Rockwell',13,'bold')).grid(column=0, row=4, pady=5)

        Label(self.frame_uno, text = 'Fecha de nacimiento',bg='white', fg='black', font=('Rockwell',13,'bold')).grid(column=0, row=5, pady=5)

        # entradas para el inventario
        
        Entry(self.frame_uno, textvariable=self.cedula, font=('Rockwell',12)).grid(column=1, row=1)

        Entry(self.frame_uno, textvariable=self.Nombre, font=('Rockwell',12)).grid(column=1, row=2)
          
        Entry(self.frame_uno, textvariable=self.Correo, font=('Rockwell',12)).grid(column=1, row=3)

        Entry(self.frame_uno, textvariable=self.Celular, font=('Rockwell',12)).grid(column=1, row=4)

        Entry(self.frame_uno, textvariable=self.FechaN, font=('Rockwell',12)).grid(column=1, row=5)

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
        datos =(self.base_datos.mostarDatosClientes())

        for dato in datos: {
            self.tabla.insert('',0, text = dato[0], values= (dato[1],dato[2],dato[3],dato[4],dato[5]))
        }
            
        #datos tabla inventario
        self.tabla['columns'] = ('Cedula','Nombre','Correo','Celular','Fecha')
        
        self.tabla.column('#0',minwidth=100,width=120,anchor='center')
        self.tabla.column('Cedula',minwidth=100,width=120,anchor='center')
        self.tabla.column('Nombre',minwidth=100,width=120,anchor='center')
        self.tabla.column('Correo',minwidth=100,width=120,anchor='center')
        self.tabla.column('Celular',minwidth=100,width=120,anchor='center')
        self.tabla.column('Fecha',minwidth=100,width=120,anchor='center')
        
        self.tabla.heading('#0',text='IdCliente',anchor='center')
        self.tabla.heading('Cedula',text='Cedula',anchor='center')
        self.tabla.heading('Nombre',text='Nombre',anchor='center')
        self.tabla.heading('Correo',text='Correo',anchor='center')
        self.tabla.heading('Celular',text='Celular',anchor='center')
        self.tabla.heading('Fecha',text='Fecha Nacimiento',anchor='center')

        self.tabla.bind("<<TreeviewSelect>>",self.obtener_fila_inventario)
        self.tabla.bind("<<Double-1>>", self.eliminar_datos_inventario)

    def obtener_fila_inventario(self,event):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        self.cedula.set(self.data['values'][0])
        self.Nombre.set(self.data['values'][1])
        self.Correo.set(self.data['values'][2])
        self.Celular.set(self.data['values'][3])
        self.FechaN.set(self.data['values'][4])

    def eliminar_datos_inventario(self):
       
        
        item = self.tabla.selection()[0]
        x = messagebox.askquestion('Informacion','¿Está seguro?')
        if x == 'yes':
            self.limpiar_campos_inventario()
            self.tabla.delete(item)
            self.base_datos.EliminarDatosClientes(self.data['text'])

    def limpiar_campos_inventario(self):
        self.cedula.set('')
        self.Nombre.set('')
        self.Correo.set('')
        self.Celular.set('')
        self.FechaN.set('')
    
    def agregar_datos_inventario(self):
        cedula = self.cedula.get()
        nombre = self.Nombre.get()
        correo = self.Correo.get()
        celular = self.Celular.get()
        fecha = self.FechaN.get()
        if cedula and nombre and correo and celular and fecha != '':
            self.base_datos.insertarDatosClientes(cedula,nombre,correo,celular,fecha)
            self.datos=(self.base_datos.mostarDatosClientes())
            self.tabla.insert('',0, text = self.datos[-1][0], values= (cedula,nombre,correo,celular,fecha))
            self.limpiar_campos_inventario()
   
        
    def actualizar_tabla(self):
        self.limpiar_campos()
        datos = self.base_datos.mostrarDatosClientes()
        self.table.delete(*self.tabla.get_children())
        i=-1
        for dato in datos:
            i=i+1
            self.tabla.insert('',i,text=dato[i][1:2][0],values=dato[i][2:5])
    
    def actualizar_datos_inventario(self):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        cedula= self.data['values'][0]
        datos = self.base_datos.mostarDatosClientes()
        for fila in datos:
            Id = fila[0]
            Cedula_bd= fila[1]
            if Cedula_bd == cedula:
                if Id != None:
                    cedula = self.cedula.get()
                    nombre = self.Nombre.get()
                    correo = self.Correo.get()
                    celular = self.Celular.get()
                    fecha = self.FechaN.get()
                    if cedula and nombre and correo and celular and fecha != '':
                        self.base_datos.ActualizaDatosClientes(Id,cedula,nombre,correo,celular,fecha)
                        self.tabla.delete(*self.tabla.get_children())
                        datos = self.base_datos.mostrarDatosclientes()
                        i=-1
                        for dato in datos:
                            i=i+1
                            self.tabla.insert('',i,text=datos[i][1:2][0], values=datos[i][2:5])


    def actualizar_registro(self):
        
        item = self.tabla.selection()[0]
        x = messagebox.askquestion('Informacion','¿Está seguro?')
        if x == 'yes':
            cedula = self.cedula.get()
            nombre = self.Nombre.get()
            correo = self.Correo.get()
            celular = self.Celular.get()
            fecha = self.FechaN.get()
            id = self.data['text']
            self.limpiar_campos_inventario()
            self.base_datos.ActualizaDatosClientes(self.data['text'],cedula,nombre,correo,celular,fecha)
            self.tabla.insert('',0, text = id, values= (cedula,nombre,correo,celular,fecha))
            self.tabla.delete(item)
            self.actualizar_tabla()
            
        
if __name__ == "__main__":
    ventana = Tk()
    ventana.title('Chapicalzado')
    ventana.minsize(height=400, width=600)
    ventana.geometry('1090x850')
    app = App(ventana)
    app.mainloop()
