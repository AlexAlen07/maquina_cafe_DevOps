import maquina_cafe

def main():
    inventario = Inventario(vasos=5, azucar=5, cafe=5, leche=2)
    maquina = maquina_cafe(inventario=inventario)

# inventario.py
class Inventario:
    def __init__(self, vasos, azucar, cafe, leche):
        self.vasos = vasos
        self.azucar = azucar
        self.cafe = cafe
        self.leche = leche

    def tiene_vaso(self, tamanio):
        return self.vasos > 0

    def usar_vaso(self, tamanio):
        if not self.tiene_vaso(tamanio):
            raise Exception("No hay vasos disponibles")
        self.vasos -= 1

    def tiene_azucar(self, cantidad):
        return self.azucar >= cantidad

    def usar_azucar(self, cantidad):
        if not self.tiene_azucar(cantidad):
            raise Exception("No hay azúcar suficiente")
        self.azucar -= cantidad

    def tiene_cafe(self):
        return self.cafe > 0

    def usar_cafe(self):
        if not self.tiene_cafe():
            raise Exception("No hay café disponible")
        self.cafe -= 1
