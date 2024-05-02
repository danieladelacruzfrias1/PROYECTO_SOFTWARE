import unittest
from unittest.mock import Mock, MagicMock
from Notas import NotasApp  # Asegúrate de que tu archivo se llame 'notas.py'

class TestNotasApp(unittest.TestCase):
    def setUp(self):
        self.root = MagicMock()
        self.app = NotasApp(self.root)

        # Mocking the database
        self.app.conn = Mock()
        self.app.cursor = self.app.conn.cursor()

        # Mocking the GUI
        self.app.root = Mock()
        self.app.add_button = Mock()
        self.app.edit_button = Mock()
        self.app.view_button = Mock()

    def test_show_nueva_nota(self):
        # Simulamos las entradas del usuario
        with unittest.mock.patch('tkinter.simpledialog.askstring', side_effect=['titulo', 'contenido']):
            self.app.show_nueva_nota()
        self.app.cursor.execute.assert_called_with('INSERT INTO notas VALUES (?,?)', ('titulo', 'contenido'))

    def test_edit_nota(self):
        # Simulamos las entradas del usuario y la respuesta de la base de datos
        with unittest.mock.patch('tkinter.simpledialog.askstring', side_effect=['titulo', 'nuevo contenido']):
            self.app.cursor.execute.return_value.fetchone.return_value = 'contenido antiguo'
            self.app.edit_nota()
        self.app.cursor.execute.assert_called_with('UPDATE notas SET contenido=? WHERE titulo=?', ('nuevo contenido', 'titulo'))

    def test_view_notas(self):
        # Simulamos la respuesta de la base de datos
        self.app.cursor.execute.return_value = [('titulo', 'contenido')]
        try:
            self.app.view_notas()
        except TypeError:
            pass 
        self.app.cursor.execute.assert_called_with('SELECT * FROM notas')

if __name__ == '__main__':
    unittest.main()
