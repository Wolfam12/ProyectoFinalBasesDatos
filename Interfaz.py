
from tkinter import *
import subprocess


class Principal(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.columnconfigure(0,weight=1)
        self.master.rowconfigure(0,weight=1)
        self.master.columnconfigure(0,weight=1)
        self.master.columnconfigure(0,weight=1)
    
        self.widgets()

    def widgets(self):
        self.frame_uno = Frame(self.master, bg='white', height=200, width=800)
        self.frame_uno.grid(column =0, row=0, sticky='nsew') 
        self.frame_uno.columnconfigure([0,1,2,3,4,5], weight=1)
        self.frame_uno.rowconfigure([0,1,2,3,4,5,6,7], weight=1)

        Label(self.frame_uno, text='Pagina Principal',bg='white',fg='black',font=('Kaufmann BT',13,'bold')).grid(column=2,row=1)
        Label(self.frame_uno, text='Escoja una opcion',bg='white',fg='black',font=('Kaufmann BT',10,'bold')).grid(column=2,row=2)
        Button(self.frame_uno,text='Gestionar Inventario', font=('Rockwell',9,'bold'), command= self.abrir_inventario).grid(column=1,row=1,)
        Button(self.frame_uno,text='Gestionar Clientes', font=('Rockwell',9,'bold'),command= self.abrir_clientes).grid(column=1,row=2)
        Button(self.frame_uno,text='Gestionar Empleados', font=('Rockwell',9,'bold'),command= self.abrir_empleados).grid(column=1,row=3)
        Button(self.frame_uno,text='Gestionar Envios', font=('Rockwell',9,'bold'), command= self.abrir_envios).grid(column=1,row=4)
        Button(self.frame_uno,text='Gestionar Sede', font=('Rockwell',9,'bold'),command= self.abrir_sede).grid(column=1,row=5)


    def abrir_inventario(self):
        subprocess.call(['python', 'ProyectoFinalBasesDatos-main/main.py'])
    
    def abrir_clientes(self):
        subprocess.call(['python', 'ProyectoFinalBasesDatos-main/GUI_TCliente.py'])
    
    def abrir_empleados(self):
        subprocess.call(['python', 'ProyectoFinalBasesDatos-main/GUI_TEmpleado.py'])

    def abrir_envios(self):
        subprocess.call(['python', 'ProyectoFinalBasesDatos-main/GUI_TEnvio.py'])
    
    def abrir_sede(self):
        subprocess.call(['python', 'ProyectoFinalBasesDatos-main/GUI_TSede.py'])

        
        

if __name__ == "__main__":
    ventana = Tk()
    ventana.title('Chapicalzado')
    ventana.minsize(height=360, width=285)
    ventana.geometry('360x285')
    app = Principal(ventana)
    
    
    

app.mainloop()