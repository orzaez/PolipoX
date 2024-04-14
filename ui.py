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

state = tk.IntVar(value=0)

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
mucosal_pattern_nice = tk.StringVar()
mucosal_pattern_jnet = tk.StringVar()

def update_ui(state_value):
    state = state_value


    if state == 0:
        main_text.set("Preparado para registrar pólipo")
        help_text.set("Diga 'REGISTRAR' para comenzar el registro de pólipo")

    elif state == 1:
        main_text.set("Localización del pólipo")
        help_text.set("Diga los centímetros desde margen anal")

    elif state == 2:
        main_text.set(f"""El polipo esta a {location.get()} cm del margen anal?""")
        help_text.set("Diga Si para continuar o No volver a introducir el dato")

    elif state == 3:
        main_text.set("Tamaño en X del pólipo")
        help_text.set("Diga el tamaño estimado en milímetros")

    elif state == 4:
        main_text.set(f"""El tamaño en x del polipo esta a {size_x.get()} mm?""")
        help_text.set("Diga Si para continuar o No volver a introducir el dato")


    elif state == 5:
        main_text.set("¿Desea registrar el tamaño en Y?")
        help_text.set("Diga Si para introducir otra medida o No para continuar")

    elif state == 6:
        main_text.set("Tamaño en Y del pólipo")
        help_text.set("Diga el tamaño estimado en milímetros")
        
    
    elif state == 7:
        main_text.set(f"""El tamaño en y del polipo esta a {size_y.get()} mm?""")
        help_text.set("Diga Si para continuar o No volver a introducir el dato")

    elif state == 8:
        main_text.set(
            f"""
            Los datos recogidos son:
                - Localización: {location.get()} cm
                - Tamaño X: {size_x.get()} mm
                - Tamaño Y: {size_y.get()} mm
            ¿Desea agregar más parámetros?
            """
        )
        help_text.set("Diga Si para introducir parámetros extra o No para continuar")
        

    elif state == 9:
        main_text.set(
            f"""
            ¿Qué parámetro desea añadir o modificar?
                1. Patrón mucoso NICE: {(mucosal_pattern_nice.get() if mucosal_pattern_nice.get() else "-")} 
                2. Patrón mucoso JNET: {(mucosal_pattern_jnet.get() if mucosal_pattern_jnet.get() else "-")} 
                3. Tipo de lesión: {(lesion_type.get() if lesion_type.get() else "-")}
                4. Clasificación de París: {(paris_classification.get() if paris_classification.get() else "-")}
                5. Continuar
            """
        )
        help_text.set("Diga el número correspondiente a la opción elegida.")
      

    elif state == 10:
        main_text.set("""
                      Patrón mucoso
                        1. NICE 1    
                        2. NICE 2
                        3. NICE 3
                      """)
        help_text.set("Diga el número correspondiente a la opción elegida")

    elif state == 11:
        main_text.set("""
                      Patrón mucoso
                        1. JNET 1    
                        2. JNET 2a
                        3. JNET 2b
                        4. JNET 3
                      """)
        help_text.set("Diga el número correspondiente a la opción elegida")

    elif state == 12:
        main_text.set(
            """
            Tipo de lesión:
                1. Pólipo sesil
                2. Lesión de extensión lateral (LST)
            """
        )
        help_text.set("Diga el número correspondiente a la opción elegida.")

    elif state == 13: 
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

    elif state == 14:
        main_text.set("El pólipo ha sido recuperado?")
        help_text.set("Diga Si o No")

    elif state == 15:
        main_text.set(
            f"""
            Introduzca que parametros sobre la extraccion desea añadir o modificar
                1. Numero de fragmentos {(num_fragments.get() if num_fragments.get() else "-")}
                2. Método de resección {(resection_method.get() if resection_method.get() else "-")}
                3. Continuar
            """
        )
        help_text.set("Diga el número correspondiente a la opción elegida.")

    elif state == 16:
        main_text.set("Número de fragmentos")
        help_text.set("Diga el número de fragmentos extraidos")
    
    elif state == 17:
        main_text.set(f"""El número de fragmentos es {num_fragments.get()} ?""")
        help_text.set("Diga Si para continuar o No volver a introducir el dato")

    elif state == 18:
        main_text.set(
            """
            Método de resección:
                1. Pinza fría
                2. Asa fría
                3. Inyección y asa caliente
                4. Precorte
            """
        )
        help_text.set("Diga el número correspondiente a la opción elegida.")

    elif state == 19:
        main_text.set("Enviando pólipo...")

    elif state == 20:
       main_text.set("Pólipo enviado con éxito.")





