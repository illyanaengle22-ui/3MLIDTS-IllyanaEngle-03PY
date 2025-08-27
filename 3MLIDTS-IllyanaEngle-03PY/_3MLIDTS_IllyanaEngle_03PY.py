import tkinter as tk
from tkinter import messagebox

def calcular_temps():
    print("Calculando")
    if txtCelsius.get() or txtFahrenheit.get() or txtKelvin.get():
        #print("Se cumple la condicional")
         try:
            if txtCelsius.get():
                ce = float(txtCelsius.get())
                fa = (ce * 9/5) + 32
                kel = ce + 273.15
                txtFahrenheit.delete(0, tk.END)
                txtFahrenheit.insert(0, str(round(fa,2)))
                txtKelvin.delete(0, tk.END)
                txtKelvin.insert(0, str(round(kel,2)))

            elif txtFahrenheit.get():
                fa = float(txtFahrenheit.get())
                ce = (fa - 32)*5/9
                kel = ce + 273.15
                txtCelsius.delete(0, tk.END)
                txtCelsius.insert(0, str(round(ce,2)))
                txtKelvin.delete(0, tk.END)
                txtKelvin.insert(0, str(round(kel,2)))

            elif txtKelvin.get():
                kel = float(txtKelvin.get())
                ce = kel - 273.15
                fa = (ce * 9/5) + 32
                txtFahrenheit.delete(0, tk.END)
                txtFahrenheit.insert(0, str(round(fa,2)))
                txtCelsius.delete(0, tk.END)
                txtCelsius.insert(0, str(round(ce,2)))

         except ValueError:
             messagebox.showwarning("Advertencia", "Ingrese valores para el calculo de temperatura")
        
    else:
        messagebox.showwarning("Advertencia", "Ingrese los valores para el calculo de valores")
            
def limpiar():
    print("Limpiando")
    txtCelsius.delete(0, tk.END)
    txtFahrenheit.delete(0, tk.END)
    txtKelvin.delete(0, tk.END)
    #messagebox.showinfo("Limpar", "Se borraron los valores de los campos")
    messagebox.showinfo(message="Limpiar", title="Se borraron los valores de las entradas")


#Ventana
ventana = tk.Tk()
ventana.title("Conversor Basico de Temperaturas")

#Etiquetas
#tk.Label(ventana, text = "Celsius").grid(row = 0, column=0,padx=10,pady=10)
lbCelsius = tk.Label(ventana, text = "Celsius")
lbCelsius.grid(row = 0, column=0, padx=10,pady=10)

#tk.Label(ventana, text = "Fahrenheit").grid(row=1, column=0, padx=10, pady=10)
lbFahrenheit = tk.Label(ventana, text = "Fahrenheit")
lbFahrenheit.grid(row =1, column=0, padx=10,pady=10)

#tk.Label(ventana, text = "Kelvin").grid(row=2, column=0, padx=10, pady=10)
lbKelvin = tk.Label(ventana, text = "Kelvin")
lbKelvin.grid(row =2, column=0, padx=10,pady=10)

#Entradas
txtCelsius = tk.Entry(ventana)
txtFahrenheit = tk.Entry(ventana)
txtKelvin = tk.Entry(ventana)

#celsius_entry = tk.Entry(ventana)
#fahrenheit_entry = tk.Entry(ventana)
#kelvin_entry = tk.Entry(ventana)

txtCelsius.grid(row=0, column=1, padx=10, pady=10)
txtFahrenheit.grid(row=1, column=1, padx=10, pady=10)
txtKelvin.grid(row=2, column=1, padx=10, pady=10)

#Botones
btn_calcular = tk.Button(ventana, text = "Calcular", command= calcular_temps)
btn_limpiar = tk.Button(ventana, text = "Limpiar", command= limpiar)

btn_calcular.grid(row=3, column=0, columnspan = 2, pady = 10)
btn_limpiar.grid(row=4, column=0, columnspan = 2, pady = 10)

#Ejecucion de ventana
ventana.mainloop()
