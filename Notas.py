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

        self.edit_button = tk.Button(root, text="Editar Nota", command=self.edit_nota)
        self.edit_button.pack()

        self.delete_button = tk.Button(root, text="Eliminar Nota", command=self.delete_nota)
        self.delete_button.pack()

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

    def edit_nota(self):
        titulo = simpledialog.askstring("Editar Título", "Ingrese el título de la nota que desea editar:")
        old_contenido = self.cursor.execute('SELECT contenido FROM notas WHERE titulo=?', (titulo,)).fetchone()
        if old_contenido is None:
            messagebox.showinfo("Error", "No se encontró ninguna nota con ese título")
            return
        new_contenido = simpledialog.askstring("Editar Contenido", "Ingrese el nuevo contenido de la nota:", initialvalue=old_contenido[0])
        if new_contenido:
            self.cursor.execute('UPDATE notas SET contenido=? WHERE titulo=?', (new_contenido, titulo))
            self.conn.commit()
            messagebox.showinfo("Hecho", "Nota actualizada")
        else:
            messagebox.showinfo("Error", "El contenido es requerido")

    def delete_nota(self):
        titulo = simpledialog.askstring("Eliminar Nota", "Ingrese el título de la nota que desea eliminar:")
        self.cursor.execute('DELETE FROM notas WHERE titulo=?', (titulo,))
        self.conn.commit()
        messagebox.showinfo("Hecho", "Nota eliminada")

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




