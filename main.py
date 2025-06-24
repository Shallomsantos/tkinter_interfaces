import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame

# Inicializar pygame para reproducir sonido
pygame.mixer.init()

with open("datos_trivia.txt", "r", encoding="utf-8") as file:
    lineas = [line.strip() for line in file.readlines()]
    imagen_nombre = lineas[0]
    opciones = lineas[1:4]
    respuesta_correcta = lineas[4]
    
def verificar_respuesta():
    seleccion = var.get()
    if seleccion == respuesta_correcta:
        pygame.mixer.Sound("sonido_correcto.wav").play()
        messagebox.showinfo("Respuesta", "Correcta.")
        mostrar_emoticono("smile.png")
    else:
        pygame.mixer.Sound("sonido_incorrecto.wav").play()
        messagebox.showinfo("Respuesta", "Incorrecta.")
        mostrar_emoticono("sad.png")
        
def mostrar_emoticono(nombre_archivo):
    emot_img = Image.open(nombre_archivo)
    emot_img = emot_img.resize((100, 100))
    emoticono = ImageTk.PhotoImage(emot_img)
    emoticono_label.config(image=emoticono)
    emoticono_label.image = emoticono

ventana = tk.Tk()

ventana.title("Trivia de ciencias naturales")

#definir tamano ventana
ventana.geometry("40x500+0+0")  
ventana.minsize(400, 500)
ventana.maxsize(400, 500)

#ventana.iconbitmap("icon.ico")
ventana.configure(bg="#fcf3cf")

ventana.attributes("-alpha", 1)  # Transparencia de la ventana

# Frame principal con dos columnas: izquierda (imagen) y derecha (contenido)
frame_principal = tk.Frame(ventana, bg="beige")
frame_principal.grid(row=0, column=0, padx=10, pady=10)

# Frame izquierdo: solo para la imagen
frame_izquierda = tk.Frame(frame_principal, bg="beige")
frame_izquierda.grid(row=0, column=0, padx=100)

# Frame derecho: para el texto, opciones y botón
frame_derecha = tk.Frame(frame_principal, bg="beige")
frame_derecha.grid(row=0, column=1, padx=10)

# Cargar imagen principal
imagen = Image.open(imagen_nombre)
imagen = imagen.resize((150, 150))
imagen_tk = ImageTk.PhotoImage(imagen)
imagen_label = tk.Label(frame_izquierda, image=imagen_tk, bg="beige")
imagen_label.grid()

pregunta = tk.Label(frame_izquierda, text="La imagen corresponde a:", bg="beige", font=("Monospace", 12), pady=20)
pregunta.grid(row=1, column=0, columnspan=3)

#opciones 
#opciones = ["Un piraña mueca", "La ballena Willis", "Un delfín"]
var = tk.StringVar()
var.set(None)  
# Inicializar la variable con un valor vacío
for i, opcion in enumerate(opciones):
    tk.Radiobutton(frame_izquierda, text=opcion, variable=var, value=opcion, bg="beige", font=("Monospace", 12)).grid(row=2+i, column=0, columnspan=3, sticky="w")


# Label para emoticono
emoticono_label = tk.Label(frame_principal, bg="beige")
emoticono_label.grid(row=6, column=0, columnspan=3, pady=10)

#boton verificar
btn_verificar = tk.Button(frame_principal, text="Verificar", command=verificar_respuesta, font=("Monospace", 12))
btn_verificar.grid(row=5, column=0, columnspan=3, pady=10)

ventana.mainloop()