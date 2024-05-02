import unittest
from unittest.mock import MagicMock
from Notas import NotasApp

class TestNotasApp(unittest.TestCase):
    def setUp(self):
        root = MagicMock()  # Crear un objeto simulado para 'root'
        self.app = NotasApp(root)  # Proporcionar el objeto simulado como argumento

    def test_agregar_nota(self):
        self.app.cursor = MagicMock()
        self.app.show_nueva_nota("Título de prueba", "Contenido de prueba")

        self.app.cursor.execute.assert_called_once_with('INSERT INTO notas VALUES (?, ?)', ("Título de prueba", "Contenido de prueba"))

    def test_ver_notas(self):
        self.app.cursor = MagicMock()
        self.app.cursor.fetchall.return_value = [("Nota 1", "Contenido 1"), ("Nota 2", "Contenido 2")]

        notas = self.app.view_notas()

        self.assertEqual(notas, [("Nota 1", "Contenido 1"), ("Nota 2", "Contenido 2")])

if __name__ == '__main__':
    unittest.main()


