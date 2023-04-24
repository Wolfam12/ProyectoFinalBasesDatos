from tkinter import Tk,Button,Entry,Label,ttk,PhotoImage
from tkinter import StringVar, Scrollbar,Frame,messagebox
from conexion_sqlite import Comunicacion
from time import strftime



class Ventana(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.Referencia = StringVar()
        self.CantidadDisponible = StringVar()
        self.CantidadVendida = StringVar()
        self.FechaActualizacion = StringVar()
        self.Costo = StringVar()
        self.Proveedor = StringVar()
        self.recioVenta = StringVar()
        self.Producto = StringVar()

        self.master.columnconfigure(0,weight=1)
        self.master.rowconfigure(0,weight=1)
        self.master.columnconfigure(0,weight=1)
        self.master.columnconfigure(1,weight=5)
        self.base_datos=Comunicacion()
        self.widgets()
        


