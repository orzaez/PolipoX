import tkinter as tk
from tkinter import font as tkfont

# Ruta de la imagen del logo (reemplazar con la ruta real)
LOGO_PATH = "images/logo.png"

# Función para iniciar el proceso de registro (a implementar)
def iniciar_registro():
    # Implementar la lógica para iniciar el proceso de registro de voz
    pass

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Registro de voz")
ventana.attributes("-fullscreen", True)
ventana.geometry("+{}+{}".format(0, 0))
ventana.config(background="#ffffff")  # Color de fondo blanco
# width= ventana.winfo_screenwidth()               
# height= ventana.winfo_screenheight()               
# ventana.geometry("%dx%d" % (width, height))

# Carga del logo
logo_img = tk.PhotoImage(file=LOGO_PATH)
logo_label = tk.Label(ventana, image=logo_img, borderwidth=0)
logo_label.pack(pady=20)

# Texto principal
fuente_titulo = tkfont.Font(family="Arial", size=48, weight="bold")
texto_titulo = tk.Label(ventana, text="Preparado para registrar", font=fuente_titulo, foreground="#007bff")
texto_titulo.pack(pady=50)

# Instrucciones de ayuda
fuente_ayuda = tkfont.Font(family="Arial", size=16)
texto_ayuda = tk.Label(ventana, text="Diga \"REGISTRAR\" para comenzar el proceso de registro", font=fuente_ayuda, foreground="#6c757d")
texto_ayuda.pack(pady=20)

# Botón para iniciar registro (opcional)
# boton_iniciar = tk.Button(ventana, text="Iniciar registro", command=iniciar_registro)
# boton_iniciar.pack(pady=20)

# Ejecución de la interfaz
ventana.mainloop()
