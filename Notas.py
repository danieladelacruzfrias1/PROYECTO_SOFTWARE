import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog

class NotasApp:
    def __init__(self, root):
        self.conn = sqlite3.connect('notas.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS notas(titulo TEXT, contenido TEXT)')

        self.root = root
        self.root.title("Aplicación de Notas")

        self.add_button = tk.Button(root, text="Añadir Nota", command=self.show_nueva_nota)
        self.add_button.pack()

        self.view_button = tk.Button(root, text="Ver Notas", command=self.view_notas)
        self.view_button.pack()

    def show_nueva_nota(self):
        titulo = simpledialog.askstring("Nuevo Título", "Ingrese el título de la nota:")
        contenido = simpledialog.askstring("Nuevo Contenido", "Ingrese el contenido de la nota:")

        if titulo and contenido:
            self.cursor.execute('INSERT INTO notas VALUES (?,?)', (titulo, contenido))
            self.conn.commit()
            messagebox.showinfo("Hecho", "Nota añadida")
        else:
            messagebox.showinfo("Error", "Título y contenido son requeridos")

    def view_notas(self):
        self.cursor.execute('SELECT * FROM notas')
        notas = self.cursor.fetchall()
        str_notas = ""
        for nota in notas:
            str_notas += f"Título: {nota[0]}\nContenido: {nota[1]}\n\n"
        if not str_notas:
            str_notas = "No hay notas creadas aún."
        messagebox.showinfo("Notas", str_notas)

root = tk.Tk()
app = NotasApp(root)
root.mainloop()
