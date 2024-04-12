import tkinter as tk
from main import grabar_audio,transcode_audio, decode_transcription, check_there_is_command


# Define window properties
window = tk.Tk()
window.title("Registro de voz")
window.attributes("-fullscreen", True)
window.geometry("+{}+{}".format(0, 0))

# Define logo image (replace with your actual logo path)
logo_image = tk.PhotoImage(file="images/logo.png")
logo_label = tk.Label(window, image=logo_image)
logo_label.pack(pady=20)

# Define text variables
main_text = tk.StringVar()
help_text = tk.StringVar()

# Define state variables
state = tk.IntVar(value=1)  # Initialize state to 1

# Define text labels
main_text_label = tk.Label(window, textvariable=main_text, font=("Arial", 16, "bold"))
main_text_label.pack(pady=20)

help_text_label = tk.Label(window, textvariable=help_text, font=("Arial", 12))
help_text_label.pack(pady=20)

# Define data variables
location = tk.StringVar()
size_x = tk.StringVar()
size_y = tk.StringVar()

# Define data labels (initially hidden)
location_label = tk.Label(window, textvariable=location, font=("Arial", 12))
size_x_label = tk.Label(window, textvariable=size_x, font=("Arial", 12))
size_y_label = tk.Label(window, textvariable=size_y, font=("Arial", 12))

# Define additional parameter entry fields (initially hidden)
mucosal_pattern_label = tk.Label(window, text="Patrón mucoso:")
mucosal_pattern_entry = tk.Entry(window)

lesion_type_label = tk.Label(window, text="Tipo de lesión:")
lesion_type_entry = tk.Entry(window)

paris_classification_label = tk.Label(window, text="Clasificación de París:")
paris_classification_entry = tk.Entry(window)

def add_parameter_handle():
    state.set(5.1)
    update_ui(state.get())

# Define additional parameter buttons
add_parameter_button = tk.Button(window, text="Añadir Parámetro", command=add_parameter_handle)

def continue_handle():
    state.set(state.get() + 1)
    update_ui(state.get())

# Define continue button
continue_button = tk.Button(window, text="Continuar", command=continue_handle)


# Define function to update UI based on state
def update_ui(state_value):
    state = state_value

    # Hide all labels and entry fields
    location_label.pack_forget()
    size_x_label.pack_forget()
    size_y_label.pack_forget()
    mucosal_pattern_label.pack_forget()
    mucosal_pattern_entry.pack_forget()
    lesion_type_label.pack_forget()
    lesion_type_entry.pack_forget()
    paris_classification_label.pack_forget()
    paris_classification_entry.pack_forget()
    add_parameter_button.pack_forget()

    # Set main text and help text based on state
    if state == 1:
        main_text.set("Preparado para registrar pólipo")
        help_text.set("Diga 'REGISTRAR' para comenzar el registro de pólipo")
        continue_button.pack(pady=10)

    elif state == 2:
        main_text.set("Localización del pólipo")
        help_text.set("Diga los centímetros desde margen anal")
        location_label.pack(pady=10)  # Show location label

    elif state == 3:
        main_text.set("Tamaño en X del pólipo")
        help_text.set("Diga el tamaño estimado en milímetros")
        size_x_label.pack(pady=10)  # Show size_x label

    elif state == 4:
        main_text.set("¿Desea registrar el tamaño en Y?")
        help_text.set("Diga Si para introducir otra medida o No para continuar")

    elif state == 4.2:
        main_text.set("Tamaño en Y del pólipo")
        help_text.set("Diga el tamaño estimado en milímetros")
        size_y_label.pack(pady=10)  # Show size_y label

    elif state == 5:
        main_text.set(
            f"""
            Los datos recogidos son:
                - Localización: {location.get()} cm
                - Tamaño X: {size_x.get()} mm
                (- Tamaño Y: {size_y.get()} mm)
            ¿Desea agregar más parámetros?
            """
        )
        help_text.set("Diga Si para introducir parámetros extra o No para continuar")
        location_label.pack(pady=10)  # Show location label
        size_x_label.pack(pady=10)  # Show size_x label
        if size_y.get():  # Show size_y label if data exists
            size_y_label.pack(pady=10)

    elif state == 5.1:
        main_text.set(
            """
            ¿Qué parámetro desea añadir o modificar?
                1. Patrón mucoso: {(mucosal_pattern_entry.get() if mucosal_pattern_entry.get() else "-")}
                2. Tipo de lesión: {(lesion_type_entry.get() if lesion_type_entry.get() else "-")}
                3. Clasificación de París: {(paris_classification_entry.get() if paris_classification_entry.get() else "-")}
                4. Continuar
            """
        )
        help_text.set("Diga el número correspondiente a la opción elegida.")
        mucosal_pattern_label.pack(pady=5)
        mucosal_pattern_entry.pack(pady=5)
        lesion_type_label.pack(pady=5)
        lesion_type_entry.pack(pady=5)
        paris_classification_label.pack(pady=5)
        paris_classification_entry.pack(pady=5)
        add_parameter_button.pack(pady=10)

# Update UI based on initial state
update_ui(state.get())

# (Rest of the code for button clicks and application logic)

        
window.mainloop()

address = "C8:9B:D7:DD:B0:E8"  
filename = "./temp/grabacion.wav"
duration = 5



import threading
import watchdog.observers
import watchdog.events
import datetime
import time

def generar_timestamp():
    """
    Genera un timestamp en formato YYYYMMDDHHMMSS.

    :return: Timestamp como string.
    """
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    return timestamp

class Productor(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            timestamp = generar_timestamp()
            grabar_audio(address, "./temp/" + timestamp + ".wav", duration)

class Consumidor(threading.Thread):
    def __init__(self, carpeta):
        super().__init__()
        self.carpeta = carpeta

    def run(self):
        event_handler = Handler()
        observer = watchdog.observers.Observer()
        observer.schedule(event_handler, self.carpeta, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            observer.join()

class Handler(watchdog.events.FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        filepath = event.src_path
        if filepath.endswith('.wav'):
            while True:
                try:
                    with open(filepath, 'rb') as f:
                        pass
                    break
                except IOError:
                    time.sleep(1)

            transcription = transcode_audio(filepath)
            decoded_transcription = decode_transcription(transcription)
            if(check_there_is_command("REGISTRAR", decoded_transcription)):
                state.set(state.get() + 1)
                update_ui(state.get())
            


