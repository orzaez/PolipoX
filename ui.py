import tkinter as tk
from tkinter import Tk, PhotoImage, Label
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Registro de voz")
window.attributes("-fullscreen", True)
window.geometry("+{}+{}".format(0, 0))
imagen = PhotoImage(file = "images/bg.png")
background = Label(image = imagen, text = "Imagen S.O de fondo")

background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
#window.configure(background="white")


image_logo=Image.open("images/logo.png")
img_logo=image_logo.resize((int(200*1.10), 200))
logo_image = ImageTk.PhotoImage(img_logo)
logo_label = tk.Label(window, image=logo_image)
logo_label.pack()
logo_label.configure(background="white")
#image_logo=Image.open("images/logo.png")
#image_lore=image_logo.resize((10,10))
#imagenicom = ImageTk.PhotoImage(image_lore)



main_text = tk.StringVar()
help_text = tk.StringVar()
example_text = tk.StringVar()
subtitles = tk.StringVar()

state = tk.IntVar(value=0)

main_text_label = tk.Label(window, textvariable=main_text, font=("Inter", 25, "bold"))
main_text_label.pack(pady=20)
main_text_label.configure(background="white")

boton1_text = tk.StringVar()
boton2_text = tk.StringVar()
boton3_text = tk.StringVar()
boton4_text = tk.StringVar()
boton5_text = tk.StringVar()
boton6_text = tk.StringVar()
boton7_text = tk.StringVar()
boton8_text = tk.StringVar()
boton9_text = tk.StringVar()
boton10_text = tk.StringVar()
boton11_text = tk.StringVar()
boton12_text = tk.StringVar()




help_text_label = tk.Label(window, textvariable=help_text, font=("Inter", 12))
help_text_label.pack(pady=20)
help_text_label.configure(background="white")



image=Image.open("images/microphone.png")
img=image.resize((30,30))
microphone_icon = ImageTk.PhotoImage(img)



microphone_label = tk.Label(window, 
                           textvariable=subtitles, 
                           compound=tk.LEFT, 
                           padx=10, 
                           pady=20,
                           font=("Inter", 25),
                           image=microphone_icon)

microphone_label.pack(side=tk.BOTTOM, pady=10)
microphone_label.configure(background="white")

example_text_label = tk.Label(window, textvariable=example_text, font=("Inter", 12))
example_text_label.configure(background="white")
button_frame = tk.Frame(window, bg="white")
button_frame.pack()

boton1 = tk.Button(button_frame, textvariable=boton1_text, bg="white", justify="left",width=30,borderwidth=0.1)
boton2 = tk.Button(button_frame, textvariable=boton2_text, bg="white", justify="left",width=30,borderwidth=0.1)
boton3 = tk.Button(button_frame, textvariable=boton3_text, bg="white", justify="left",width=30,borderwidth=0.1)
boton4 = tk.Button(button_frame, textvariable=boton4_text, bg="white", justify="left",width=30,borderwidth=0.1)
boton5 = tk.Button(button_frame, textvariable=boton5_text, bg="white", justify="left",width=30,borderwidth=0.1)
boton6 = tk.Button(button_frame, textvariable=boton6_text, bg="white", justify="left",width=30,borderwidth=0.1)
boton7 = tk.Button(button_frame, textvariable=boton7_text, bg="white", justify="left",width=30,borderwidth=0.1)
boton8 = tk.Button(button_frame, textvariable=boton8_text, bg="white", justify="left",width=30,borderwidth=0.1)
boton9 = tk.Button(button_frame, textvariable=boton9_text, bg="white", justify="left",width=30,borderwidth=0.1)
boton10 = tk.Button(button_frame, textvariable=boton10_text, bg="white", justify="left",width=30,borderwidth=0.1)
boton11 = tk.Button(button_frame, textvariable=boton11_text, bg="white", justify="left",width=30,borderwidth=0.1)
    
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
    boton1_text.set("")
    boton2_text.set("")
    boton3_text.set("")
    boton4_text.set("")
    boton5_text.set("")
    boton6_text.set("")
    boton7_text.set("")
    boton8_text.set("")
    boton9_text.set("")
    boton10_text.set("")
    boton11_text.set("")
    boton12_text.set("")
    button_frame.pack_forget()
    boton1.grid_forget()
    boton2.grid_forget()
    boton3.grid_forget()
    boton4.grid_forget()
    boton5.grid_forget()
    boton6.grid_forget()
    boton7.grid_forget()
    boton8.grid_forget()
    boton9.grid_forget()
    boton10.grid_forget()
    boton11.grid_forget()
    

    if state == 0:
        main_text.set("Preparado para registrar pólipo")
        help_text.set("Diga 'Si' para comenzar el registro de pólipo")
    
    elif state == 1:
        main_text.set("Localización del pólipo")
        help_text.set("Diga '<MEDIDA> centimetros'")
        example_text.set("Ejemplo: '20 centimetros'")
        # example_text_label.pack(pady=20)

    elif state == 2:
        main_text.set(f"""El polipo esta a {location.get()} cm del margen anal?""")
        help_text.set('Diga "Si" para continuar o "No" para volver a introducir el dato')

    elif state == 3:
        main_text.set("Tamaño en X del pólipo")
        help_text.set("Diga '<MEDIDA> milímetros'")
        example_text.set("Ejemplo: '20 milílimetros'")
        # example_text_label.pack(pady=20)

    elif state == 4:
        main_text.set(f"""El tamaño en x del polipo esta a {size_x.get()} mm?""")
        help_text.set('Diga "Si" para continuar o "No" para volver a introducir el dato')


    elif state == 5:
        main_text.set("¿Desea registrar el tamaño en Y?")
        help_text.set('Diga "Si" para continuar o "No" para volver a introducir el dato')

    elif state == 6:
        main_text.set("Tamaño en Y del pólipo")
        help_text.set("Diga '<MEDIDA> milímetros'")
        example_text.set("Ejemplo: '15 milímetros'")
        # example_text_label.pack(pady=20)
        
    
    elif state == 7:
        main_text.set(f"""El tamaño en y del polipo esta a {size_y.get()} mm?""")
        help_text.set('Diga "Si" para continuar o "No" volver a introducir el dato')

    elif state == 8:
        main_text.set(f"""Los datos recogidos son:""")
        help_text.set(f"""¿Desea agregar más parámetros?""")
        example_text.set('Diga "Si" para introducir parámetros extra o "No" para continuar')
        boton1_text.set(f"""Localización: {location.get()} cm""") 
        boton2_text.set(f"""Tamaño X: {size_x.get()} mm""") 
        boton3_text.set(f"""Tamaño Y: {size_y.get()} mm""")
        button_frame.pack()
        boton1.grid(row=0, column=0, padx=5, pady=5,sticky="w")
        boton2.grid(row=1, column=0, padx=5, pady=5,sticky="w")
        boton3.grid(row=2, column=0, padx=5, pady=5,sticky="w")
        example_text_label.pack(pady=20)


    elif state == 9:
        main_text.set(f"""¿Qué parámetro desea añadir o modificar?""")
        help_text.set("Diga 'Opción <NÚMERO>'.")
        example_text.set("Ejemplo: 'Opción 5'")
        
        boton1_text.set(f"""1. Patrón mucoso NICE: {(mucosal_pattern_nice.get() if mucosal_pattern_nice.get() else "-")}""") 
        boton2_text.set(f"""2. Patrón mucoso JNET: {(mucosal_pattern_jnet.get() if mucosal_pattern_jnet.get() else "-")}""") 
        boton3_text.set(f"""3. Tipo de lesión: {(lesion_type.get() if lesion_type.get() else "-")}""")
        boton4_text.set(f"""4. Clasificación de Paris: {(paris_classification.get() if paris_classification.get() else "-")}""")
        boton5_text.set(f"""5. Continuar""")
        button_frame.pack()
        boton1.grid(row=0, column=0, padx=5, pady=5,sticky="w")
        boton2.grid(row=1, column=0, padx=5, pady=5,sticky="w")
        boton3.grid(row=2, column=0, padx=5, pady=5,sticky="w")
        boton4.grid(row=3, column=0, padx=5, pady=5,sticky="w")
        boton5.grid(row=4, column=0, padx=5, pady=5,sticky="w")
        
        example_text_label.pack(pady=20)

      

    elif state == 10:
        main_text.set(f"""Patrón mucoso""")
        help_text.set("Diga 'Opcion <NÚMERO>'")
        example_text.set("Ejemplo: 'Opción 2'")
        
        boton1_text.set(f"""1. NICE 1""") 
        boton2_text.set(f"""2. NICE 2""") 
        boton3_text.set(f"""3. NICE 3""")
        button_frame.pack()
        boton1.grid(row=0, column=0, padx=5, pady=5,sticky="w")
        boton2.grid(row=1, column=0, padx=5, pady=5,sticky="w")
        boton3.grid(row=2, column=0, padx=5, pady=5,sticky="w")
        example_text_label.pack(pady=20)

    elif state == 11:
        main_text.set("""Patrón mucoso""")
        help_text.set("Diga 'Opcion <NÚMERO>'")
        example_text.set("Ejemplo: 'Opción 1'")
        boton1_text.set(f"""1. JNET 1""") 
        boton2_text.set(f"""2. JNET 2a""") 
        boton3_text.set(f"""3. JNET 2b""")
        boton4_text.set(f"""4. JNET 3""")

        button_frame.pack()

        boton1.grid(row=0, column=0, padx=5, pady=5,sticky="w")
        boton2.grid(row=1, column=0, padx=5, pady=5,sticky="w")
        boton3.grid(row=2, column=0, padx=5, pady=5,sticky="w")
        boton4.grid(row=3, column=0, padx=5, pady=5,sticky="w")
        example_text_label.pack(pady=20)
        # example_text_label.pack(pady=20)

    elif state == 12:
        main_text.set("""Tipo de lesión:""")
        help_text.set("Diga 'Opcion <NÚMERO>'")
        example_text.set("Ejemplo: 'Opción 2'")
        button_frame.pack()
        boton1_text.set(f"""1. Pólipo sesil """) 
        boton2_text.set(f"""2. Lesión de extensión lateral (LST)""")
        boton1.grid(row=0, column=0, padx=5, pady=5,sticky="w")
        boton2.grid(row=1, column=0, padx=5, pady=5,sticky="w")
        # example_text_label.pack(pady=20)

    elif state == 13: 
        main_text.set(f"""Clasificación de Paris:""")
        help_text.set("Diga 'Opción <NÚMERO>'")
        example_text.set("Ejemplo: 'Opción 2'")


        boton1_text.set(f"""1. 0-Is""") 
        boton2_text.set(f""" 2. 0-Ip""") 
        boton3_text.set(f"""3. 0-Isp""")
        boton4_text.set(f"""4. 0-IIa""")
        boton5_text.set(f"""5. 0-IIb""")
        boton6_text.set(f"""6. 0-IIc""")
        boton7_text.set(f"""7. mixto 0-IIa+Is""")
        boton8_text.set(f"""8. mixto 0-IIb+Is""")
        boton9_text.set(f"""9. mixto 0-IIc+Is""")
        boton10_text.set(f""" 10. mixto 0-IIa+IIc""")
        boton11_text.set(f"""11. mixto 0-IIb+IIc""")
        
        button_frame.pack()
        
        boton1.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        boton2.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        boton3.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        boton4.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        boton5.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        boton6.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        boton7.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        boton8.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        boton9.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        boton10.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        boton11.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        example_text_label.pack(pady=20)

    elif state == 14:
        main_text.set("El pólipo ha sido recuperado?")
        help_text.set("Diga Si o No")
        example_text.set("")
        example_text_label.pack(pady=20)

    elif state == 15:
        main_text.set(f"Introduzca que parámetros sobre la extracción\n" 
                      f" desea añadir o modificar")
        boton1_text.set(f"""1. Número de fragmentos:  {(num_fragments.get() if num_fragments.get() else "-")}""")
        boton2_text.set(f"""2. Método de resección: {(resection_method.get() if resection_method.get() else "-")}""")
        boton3_text.set("3. Continuar: ")

        button_frame.pack()
         
        boton1.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        boton2.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        boton3.grid(row=2, column=0, padx=5, pady=5, sticky="w")
       
        
        help_text.set("Diga 'Opcion <NÚMERO>'")
        example_text.set("Ejemplo: 'Opción 3'")
        example_text_label.pack(pady=20)
        
    elif state == 16:
        main_text.set("Número de fragmentos")
        help_text.set("Diga '<NÚMERO> fragmentos'")
        example_text.set("Ejemplo:'2 fragmentos'")
        example_text_label.pack(pady=20)
    
    elif state == 17:
        main_text.set(f"""El número de fragmentos es {num_fragments.get()} ?""")
        help_text.set("Diga Si para continuar o No para volver a introducir el dato")
        example_text.set("")
        example_text_label.pack(pady=20)

    elif state == 18:
        main_text.set("Método de resección:"
        )
        boton1_text.set("1. Pinza fría") 
        boton2_text.set("2. Asa fría") 
        boton3_text.set("3. Inyección y asa caliente")
        boton4_text.set("4. Precorte")
        
        button_frame.pack()


        boton1.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        boton2.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        boton3.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        boton4.grid(row=3, column=0, padx=5, pady=5, sticky="w")

       
        help_text.set("Diga 'Opción <NÚMERO>'")
        example_text.set("Ejemplo: 'Opción 2'")
        example_text_label.pack(pady=20)

    elif state == 19:
        main_text.set("Enviando pólipo...")
        example_text.set("")
        example_text_label.pack(pady=20)






