import tkinter as tk

# Función para iniciar el registro
def iniciar_registro():
  # Acciones para iniciar el registro del polipo
  print("Iniciando registro...")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("UWU")

# Crear un widget de marco para contener la pantalla de inicio
marco_inicio = tk.Frame(ventana)
marco_inicio.pack(padx=10, pady=10)

# Crear una etiqueta con el mensaje de bienvenida
etiqueta_bienvenida = tk.Label(marco_inicio, text="UWUSSSSSSSSSSSSSSS")
etiqueta_bienvenida.pack()

# Crear un botón para iniciar el registro
boton_iniciar = tk.Button(marco_inicio, text="Iniciar registro", command=iniciar_registro)
boton_iniciar.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()
