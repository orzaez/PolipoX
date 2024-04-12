import tkinter as tk

window = tk.Tk()
window.title("Registro de voz")
# window.attributes("-fullscreen", True)
window.geometry("+{}+{}".format(0, 0))

logo_image = tk.PhotoImage(file="images/logo.png")
logo_label = tk.Label(window, image=logo_image)
logo_label.pack(pady=20)

main_text = tk.StringVar()
help_text = tk.StringVar()

state = tk.IntVar(value=1)

main_text_label = tk.Label(window, textvariable=main_text, font=("Arial", 16, "bold"))
main_text_label.pack(pady=20)

help_text_label = tk.Label(window, textvariable=help_text, font=("Arial", 12))
help_text_label.pack(pady=20)
location = tk.StringVar()
size_x = tk.StringVar()
size_y = tk.StringVar()
mucosal_pattern = tk.StringVar()
lesion_type = tk.StringVar()
paris_classification = tk.StringVar()
num_fragments = tk.StringVar()
resection_method = tk.StringVar()

location_label = tk.Label(window, textvariable=location, font=("Arial", 12))
size_x_label = tk.Label(window, textvariable=size_x, font=("Arial", 12))
size_y_label = tk.Label(window, textvariable=size_y, font=("Arial", 12))
mucosal_pattern_label = tk.Label(window, textvariable=mucosal_pattern, font=("Arial", 12))
lesion_type_label = tk.Label(window, textvariable=lesion_type, font=("Arial", 12))
paris_classification_label = tk.Label(window, textvariable=paris_classification, font=("Arial", 12))
num_fragments_label = tk.Label(window, textvariable=num_fragments, font=("Arial", 12))
resection_method_label = tk.Label(window, textvariable=resection_method, font=("Arial", 12))

mucosal_pattern_nice_entry = tk.Entry(window)
mucosal_pattern_jnet_entry = tk.Entry(window)
lesion_type_entry = tk.Entry(window)
paris_classification_entry = tk.Entry(window)
num_fragments_entry = tk.Entry(window)
resection_method_entry = tk.Entry(window)

def update_ui(state_value):
    state = state_value

    location_label.pack_forget()
    size_x_label.pack_forget()
    size_y_label.pack_forget()
    mucosal_pattern_label.pack_forget()
    mucosal_pattern_nice_entry.pack_forget()
    mucosal_pattern_jnet_entry.pack_forget()
    lesion_type_label.pack_forget()
    lesion_type_entry.pack_forget()
    paris_classification_label.pack_forget()
    paris_classification_entry.pack_forget()
    num_fragments_entry.pack_forget()
    resection_method_entry.pack_forget()

    if state == 1:
        main_text.set("Preparado para registrar pólipo")
        help_text.set("Diga 'REGISTRAR' para comenzar el registro de pólipo")

    elif state == 2:
        main_text.set("Localización del pólipo")
        help_text.set("Diga los centímetros desde margen anal")
        location_label.pack(pady=10)

    elif state == 3:
        main_text.set("Tamaño en X del pólipo")
        help_text.set("Diga el tamaño estimado en milímetros")
        size_x_label.pack(pady=10)

    elif state == 4:
        main_text.set("¿Desea registrar el tamaño en Y?")
        help_text.set("Diga Si para introducir otra medida o No para continuar")

    elif state == 5:
        main_text.set("Tamaño en Y del pólipo")
        help_text.set("Diga el tamaño estimado en milímetros")
        size_y_label.pack(pady=10)

    elif state == 6:
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
        location_label.pack(pady=10)
        size_x_label.pack(pady=10)
        if size_y.get():
            size_y_label.pack(pady=10)

    elif state == 7:
        main_text.set(
            f"""
            ¿Qué parámetro desea añadir o modificar?
                1. Patrón mucoso: NICE: {(mucosal_pattern_nice_entry.get() if mucosal_pattern_nice_entry.get() else "-")}, JNET: {(mucosal_pattern_jnet_entry.get() if mucosal_pattern_jnet_entry.get() else "-")} 
                2. Tipo de lesión: {(lesion_type_entry.get() if lesion_type_entry.get() else "-")}
                3. Clasificación de París: {(paris_classification_entry.get() if paris_classification_entry.get() else "-")}
                4. Continuar
            """
        )
        help_text.set("Diga el número correspondiente a la opción elegida.")
        mucosal_pattern_label.pack(pady=5)
        mucosal_pattern_nice_entry.pack(pady=5)
        mucosal_pattern_jnet_entry.pack(pady=5)
        lesion_type_label.pack(pady=5)
        lesion_type_entry.pack(pady=5)
        paris_classification_label.pack(pady=5)
        paris_classification_entry.pack(pady=5)

    elif state == 8:
        main_text.set("Patrón mucoso")
        help_text.set("¿Elegir método NICE o JNET?")

    elif state == 9:
        main_text.set("Patrón mucoso NICE")
        help_text.set("Diga un número entre las opciones 1, 2, 3")

    elif state == 10:
        main_text.set("Patrón mucoso JNET")
        help_text.set("Diga un número entre las opciones 1, 2a, 2b, 3")

    elif state == 11:
        main_text.set(
            """
            Tipo de lesión:
                1. Pólipo sesil
                2. Lesión de extensión lateral (LST)
            """
        )
        help_text.set("Diga el número correspondiente a la opción elegida.")

    elif state == 12: 
        main_text.set(
            """
            Clasificación de París:
                1. 0-Is         7. mixto 0-IIa+Is
                2. 0-Ip         8. mixto 0-IIb+Is
                3. 0-Isp        9. mixto 0-IIc+Is
                4. 0-IIa        10. mixto 0-IIa+IIc
                5. 0-IIb        11. mixto 0-IIb+IIc
                6. 0-IIc
            """
        )
        help_text.set("Diga el número correspondiente a la opción elegida.")

    elif state == 13:
        main_text.set("El pólipo ha sido recuperado?")
        help_text.set("Diga Si o No")

    elif state == 14:
        main_text.set(
            f"""
            Introduzca que parametros sobre la extraccion desea añadir o modificar
                1. Numero de fragmentos {(num_fragments_entry.get() if num_fragments_entry.get() else "-")}
                2. Método de resección {(resection_method_entry.get() if resection_method_entry.get() else "-")}
                3. Continuar
            """
        )
        help_text.set("Diga el número correspondiente a la opción elegida.")

        num_fragments_entry.pack(pady=5)
        resection_method_entry.pack(pady=5)

    elif state == 15:
        main_text.set("Número de fragmentos")
        help_text.set("Diga el número de fragmentos extraidos")

    elif state == 16:
        main_text.set(
            """
            Método de resección:
                1. Pinza fría
                2. Asa fría
                3. Inyección y asa caliente
                4. Precorte
                5. Continuar
            """
        )
        help_text.set("Diga el número correspondiente a la opción elegida.")

    elif state == 17:
        main_text.set("Enviando pólipo...")

    elif state == 18:
       main_text.set("Pólipo enviado con éxito.")





