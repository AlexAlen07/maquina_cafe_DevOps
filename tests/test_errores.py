import unittest
from maquina_cafe.excepciones import SinVasosError, SinAzucarError, SinCafeError

class TestErrores(unittest.TestCase):
    def test_tipos_de_errores(self):
        self.assertTrue(issubclass(SinVasosError, Exception))
        self.assertTrue(issubclass(SinAzucarError, Exception))
        self.assertTrue(issubclass(SinCafeError, Exception))

if __name__ == '__main__':
    unittest.main()
