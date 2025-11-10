import unittest
from maquina_cafe.inventario import Inventario

class TestInventario(unittest.TestCase):
    def test_tiene_vaso(self):
        inv = Inventario(vasos=2, azucar=5, cafe=5, leche=2)
        self.assertTrue(inv.tiene_vaso("mediano"))

    def test_usar_vaso(self):
        inv = Inventario(vasos=1, azucar=5, cafe=5, leche=2)
        inv.usar_vaso("mediano")
        self.assertEqual(inv.vasos, 0)

if __name__ == '__main__':
    unittest.main()
