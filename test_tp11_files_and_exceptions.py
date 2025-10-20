import unittest
from files_and_exceptions import read_file_to_dict, process_dict
import os

class FilesAndExceptionsTest(unittest.TestCase):
    def setUp(self):
        # Creo un archivo temporal para las pruebas
        with open('test_datos.txt', 'w') as f:
            f.write('producto1:100;producto2:200;producto1:150;producto3:50;producto2:100;')

    def tearDown(self):
        # Elimino el archivo temporal
        if os.path.exists('test_datos.txt'):
            os.remove('test_datos.txt')

    def test_read_file_to_dict(self):
        result = read_file_to_dict('test_datos.txt')
        self.assertEqual(result, {
            'producto1': [100.0, 150.0],
            'producto2': [200.0, 100.0],
            'producto3': [50.0]
        })

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_file_to_dict('no_existe.txt')

    def test_process_dict_prints_totales_y_promedio(self):
        # Capturo la salida de process_dict
        import io
        import sys
        data = {
            'producto1': [100.0, 150.0],
            'producto2': [200.0, 100.0],
            'producto3': [50.0]
        }
        captured_output = io.StringIO()
        sys.stdout = captured_output
        process_dict(data)
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        # Verifica el formato y el orden natural
        lines = output.strip().split('\n')
        self.assertEqual(lines[0], 'producto1: ventas totales $250.00, promedio $125.00')
        self.assertEqual(lines[1], 'producto2: ventas totales $300.00, promedio $150.00')
        self.assertEqual(lines[2], 'producto3: ventas totales $50.00, promedio $50.00')

if __name__ == "__main__":
    unittest.main() 
