import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()

ventana.title("Trivia de ciencias naturales")

#definir tamano ventana
ventana.geometry("600x500+0+0")
ventana.minsize(600, 500)
ventana.maxsize(600, 500)

#ventana.iconbitmap("icon.ico")
ventana.configure(bg="#fcf3cf")

ventana.attributes("-alpha", 0.9)  # Transparencia de la ventana


frame = tk.Frame(ventana, bg="lightblue")
frame.configure(width=100, height=100)
frame.grid(row=0, column=0)
frame.pack(pady=5, padx=15)


tk.Label(ventana, text="Bienvenido a la trivia de ciencias naturales", font=("Arial", 16)).pack(pady=20)

image = Image.open("./images_nature.jpeg")
imagen = ImageTk.PhotoImage(image)

label = tk.Label(ventana, image=imagen)

#tk.Image.(file="images.jpeg")
tk.Checkbutton(ventana, text="Si", font=("Arial", 12)).pack(pady=10)
tk.Checkbutton(ventana, text="No", font=("Arial", 12)).pack(pady=10)
tk.Button(ventana, text="Verificar", command=lambda: print("Comenzando la trivia..."), bg="white", font=("Arial", 14)).pack(pady=10)

ventana.mainloop()