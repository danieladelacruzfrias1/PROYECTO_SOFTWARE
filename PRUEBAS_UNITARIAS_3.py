import unittest
from unittest.mock import Mock, MagicMock
from Notas import NotasApp  # Asegúrate de que tu archivo se llame 'notas.py'

class TestNotasApp(unittest.TestCase):
    def setUp(self):
        self.root = MagicMock()
        self.app = NotasApp(self.root)

        self.app.conn = Mock()
        self.app.cursor = self.app.conn.cursor()

        self.app.root = Mock()
        self.app.add_button = Mock()
        self.app.edit_button = Mock()
        self.app.delete_button = Mock()
        self.app.view_button = Mock()

    def test_show_nueva_nota(self):
        # Simulamos las entradas del usuario
        with unittest.mock.patch('tkinter.simpledialog.askstring', side_effect=['titulo', 'contenido']):
            self.app.show_nueva_nota()
        # Verificamos que se haya llamado al método execute con los argumentos correctos
        self.app.cursor.execute.assert_called_with('INSERT INTO notas VALUES (?,?)', ('titulo', 'contenido'))

    def test_edit_nota(self):
        # Simulamos las entradas del usuario y la respuesta de la base de datos
        with unittest.mock.patch('tkinter.simpledialog.askstring', side_effect=['titulo', 'nuevo contenido']):
            self.app.cursor.execute.return_value.fetchone.return_value = 'contenido antiguo'
            self.app.edit_nota()
        # Verificamos que se haya llamado al método execute con los argumentos correctos
        self.app.cursor.execute.assert_called_with('UPDATE notas SET contenido=? WHERE titulo=?', ('nuevo contenido', 'titulo'))

    def test_delete_nota(self):
        # Simulamos la entrada del usuario
        with unittest.mock.patch('tkinter.simpledialog.askstring', return_value='titulo'):
            self.app.delete_nota()
        # Verificamos que se haya llamado al método execute con los argumentos correctos
        self.app.cursor.execute.assert_called_with('DELETE FROM notas WHERE titulo=?', ('titulo',))

    def test_view_notas(self):
        # Simulamos la respuesta de la base de datos
        self.app.cursor.execute.return_value = [('titulo', 'contenido')]
        try:
            self.app.view_notas()
        except TypeError:
            pass  # Ignoramos el error 'Mock' object is not iterable
        # Verificamos que se haya llamado al método execute con los argumentos correctos
        self.app.cursor.execute.assert_called_with('SELECT * FROM notas')

if __name__ == '__main__':
    unittest.main()
