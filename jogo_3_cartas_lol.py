
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

# Lista de cartas
cartas = [
    "cartas_lol/ahri.png",
    "cartas_lol/jinx.png",
    "cartas_lol/yasuo.png"
]
favoritas = set()
indice = 0

def toggle_favorito():
    global indice
    if indice in favoritas:
        favoritas.remove(indice)
        favorito_btn.config(text="☆")
    else:
        favoritas.add(indice)
        favorito_btn.config(text="★")

def mostrar_carta():
    global indice, img_label, carta_img
    img = Image.open(cartas[indice])
    img = img.resize((500, 350), Image.LANCZOS)
    carta_img = ImageTk.PhotoImage(img)
    img_label.config(image=carta_img)
    favorito_btn.config(text="★" if indice in favoritas else "☆")
    status_label.config(text=f"Carta {indice+1} de {len(cartas)}")

def proxima():
    global indice
    if indice < len(cartas) - 1:
        indice += 1
        mostrar_carta()

def anterior():
    global indice
    if indice > 0:
        indice -= 1
        mostrar_carta()

root = tk.Tk()
root.title("Cartas LoL - Ahri, Jinx e Yasuo")
root.geometry("600x500")

img_label = tk.Label(root)
img_label.pack(pady=10)

favorito_btn = ttk.Button(root, text="☆", command=toggle_favorito)
favorito_btn.pack()

nav_frame = tk.Frame(root)
nav_frame.pack(pady=5)

btn_ant = ttk.Button(nav_frame, text="⬅️ Anterior", command=anterior)
btn_ant.grid(row=0, column=0, padx=10)

btn_prox = ttk.Button(nav_frame, text="Próxima ➡️", command=proxima)
btn_prox.grid(row=0, column=1, padx=10)

status_label = tk.Label(root, text="")
status_label.pack()

mostrar_carta()
root.mainloop()
