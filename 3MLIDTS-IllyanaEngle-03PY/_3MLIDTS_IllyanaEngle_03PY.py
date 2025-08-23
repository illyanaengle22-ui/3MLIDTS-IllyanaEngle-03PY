
import tkinter as tk
from tkinter import messagebox

def calcular_temps():
    print("Calculando")
    if celsius_entry.get() or fahrenheit_entry.get() or kelvin_entry.get():
        #print("Se cumple la condicional")
         try:
            if celsius_entry.get():
                ce = float(celsius_entry.get())
                fa = (ce * 9/5) + 32
                kel = ce + 273.15
                fahrenheit_entry.delete(0, tk.END)
                fahrenheit_entry.insert(0, str(round(fa,2)))
                kelvin_entry.delete(0, tk.END)
                kelvin_entry.insert(0, str(round(kel,2)))

            elif fahrenheit_entry.get():
                fa = float(fahrenheit_entry.get())
                ce = (fa - 32)*5/9
                kel = ce + 273.15
                celsius_entry.delete(0, tk.END)
                celsius_entry.insert(0, str(round(ce,2)))
                kelvin_entry.delete(0, tk.END)
                kelvin_entry.insert(0, str(round(kel,2)))

            elif kelvin_entry.get():
                kel = float(kelvin_entry.get())
                ce = kel - 273.15
                fa = (ce * 9/5) + 32
                fahrenheit_entry.delete(0, tk.END)
                fahrenheit_entry.insert(0, str(round(fa,2)))
                celsius_entry.delete(0, tk.END)
                celsius_entry.insert(0, str(round(ce,2)))

         except ValueError:
             messagebox.showwarning("Advertencia", "Ingrese valores para el calculo de temperatura")
        
    else:
        messagebox.showwarning("Advertencia", "Ingrese los valores para el calculo de valores")
            
def limpiar():
    print("Limpiando")
    celsius_entry.delete(0, tk.END)
    fahrenheit_entry.delete(0, tk.END)
    kelvin_entry.delete(0, tk.END)
    messagebox.showinfo("Limpar", "Se borraron los valores de los campos")


#Ventana
ventana = tk.Tk()
ventana.title("Conversor Basico de Temperaturas")

#Etiquetas
tk.Label(ventana, text = "Celsius").grid(row = 0, column=0,padx=10,pady=10)
tk.Label(ventana, text = "Fahrenheit").grid(row=1, column=0, padx=10, pady=10)
tk.Label(ventana, text = "Kelvin").grid(row=2, column=0, padx=10, pady=10)

#Entradas
celsius_entry = tk.Entry(ventana)
fahrenheit_entry = tk.Entry(ventana)
kelvin_entry = tk.Entry(ventana)

celsius_entry.grid(row=0, column=1, padx=10, pady=10)
fahrenheit_entry.grid(row=1, column=1, padx=10, pady=10)
kelvin_entry.grid(row=2, column=1, padx=10, pady=10)

#Botones
btn_calcular = tk.Button(ventana, text = "Calcular", command= calcular_temps)
btn_limpiar = tk.Button(ventana, text = "Limpiar", command= limpiar)

btn_calcular.grid(row=3, column=0, columnspan = 2, pady = 10)
btn_limpiar.grid(row=4, column=0, columnspan = 2, pady = 10)

#Ejecucion de ventana
ventana.mainloop()
