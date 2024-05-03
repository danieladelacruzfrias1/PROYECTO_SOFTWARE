import sqlite3

class NotasApp:
    def __init__(self):
        self.conn = sqlite3.connect('notas.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS notas(titulo TEXT, contenido TEXT)')

    def show_nueva_nota(self):
        titulo = input("Ingrese el título de la nota: ")
        contenido = input("Ingrese el contenido de la nota: ")

        if titulo and contenido:
            self.cursor.execute('INSERT INTO notas VALUES (?,?)', (titulo, contenido))
            self.conn.commit()
            print("Nota añadida")
        else:
            print("Título y contenido son requeridos")

    def edit_nota(self):
        titulo = input("Ingrese el título de la nota que desea editar: ")
        old_contenido = self.cursor.execute('SELECT contenido FROM notas WHERE titulo=?', (titulo,)).fetchone()
        if old_contenido is None:
            print("No se encontró ninguna nota con ese título")
            return
        new_contenido = input(f"Ingrese el nuevo contenido de la nota (anterior: {old_contenido[0]}): ")
        if new_contenido:
            self.cursor.execute('UPDATE notas SET contenido=? WHERE titulo=?', (new_contenido, titulo))
            self.conn.commit()
            print("Nota actualizada")
        else:
            print("El contenido es requerido")

    def delete_nota(self):
        titulo = input("Ingrese el título de la nota que desea eliminar: ")
        self.cursor.execute('DELETE FROM notas WHERE titulo=?', (titulo,))
        self.conn.commit()
        print("Nota eliminada")

    def view_notas(self):
        self.cursor.execute('SELECT * FROM notas')
        notas = self.cursor.fetchall()
        str_notas = ""
        for nota in notas:
            str_notas += f"Título: {nota[0]}\nContenido: {nota[1]}\n\n"
        if not str_notas:
            str_notas = "No hay notas creadas aún."
        print(str_notas)

def main():
    app = NotasApp()
    while True:
        print("\nAplicación de Notas")
        print("1. Añadir Nota")
        print("2. Editar Nota")
        print("3. Eliminar Nota")
        print("4. Ver Notas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            app.show_nueva_nota()
        elif opcion == '2':
            app.edit_nota()
        elif opcion == '3':
            app.delete_nota()
        elif opcion == '4':
            app.view_notas()
        elif opcion == '5':
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
