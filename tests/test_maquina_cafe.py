import unittest
from maquina_cafe.inventario import Inventario
from maquina_cafe.maquina_cafe import MaquinaCafe

class TestMaquinaCafe(unittest.TestCase):
    def test_preparar_cafe_expresso(self):
        inv = Inventario(vasos=3, azucar=5, cafe=5, leche=2)
        maquina = MaquinaCafe(inventario=inv)
        mensaje = maquina.preparar_cafe("expreso")
        self.assertIn("Café preparado", mensaje)

if __name__ == '__main__':
    unittest.main()
