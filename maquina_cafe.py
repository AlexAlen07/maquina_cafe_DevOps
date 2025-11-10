# maquina_cafe.py
from excepciones import SinVasosError, SinAzucarError, SinCafeError

class MaquinaCafe:
    def __init__(self, inventario):
        """
        Inicializa la máquina de café con un inventario.
        """
        self.inventario = inventario
        self.vaso_seleccionado = None
        self.azucar_seleccionada = 0

    def seleccionar_vaso(self, tamanio):
        """
        Selecciona el vaso deseado (pequeño, mediano o grande).
        """
        if not self.inventario.tiene_vaso(tamanio):
            raise SinVasosError(f"No hay vasos del tamaño '{tamanio}' disponibles.")
        self.vaso_seleccionado = tamanio
        return f"Vaso {tamanio} seleccionado."

    def seleccionar_azucar(self, cucharadas):
        """
        Selecciona la cantidad de azúcar deseada.
        """
        if cucharadas < 0:
            raise ValueError("La cantidad de azúcar no puede ser negativa.")
        if not self.inventario.tiene_azucar(cucharadas):
            raise SinAzucarError("No hay suficiente azúcar disponible.")
        self.azucar_seleccionada = cucharadas
        return f"{cucharadas} cucharadas de azúcar seleccionadas."

    def recoger_vaso(self):
        """
        Prepara el café, valida inventario y entrega el vaso final.
        """
        if self.vaso_seleccionado is None:
            raise ValueError("Debe seleccionar un vaso antes de preparar el café.")

        if not self.inventario.tiene_cafe():
            raise SinCafeError("No hay café disponible.")

        # Si todo está correcto, consumir inventario
        self.inventario.usar_vaso(self.vaso_seleccionado)
        self.inventario.usar_azucar(self.azucar_seleccionada)
        self.inventario.usar_cafe()

        mensaje = (
            f"Café preparado en vaso {self.vaso_seleccionado} "
            f"con {self.azucar_seleccionada} cucharadas de azúcar. ¡Disfrútalo!"
        )

        # Reset para próxima orden
        self.vaso_seleccionado = None
        self.azucar_seleccionada = 0
        return mensaje

    def preparar_cafe(self, tipo):
        """
        Método de alto nivel que prepara el café según el tipo seleccionado.
        """
        tamanio = "mediano"
        azucar = 2

        if tipo == "expreso":
            tamanio = "pequeño"
            azucar = 1
        elif tipo == "con leche":
            tamanio = "mediano"
            azucar = 2
        elif tipo == "americano":
            tamanio = "grande"
            azucar = 3
        else:
            raise ValueError("Tipo de café inválido.")

        self.seleccionar_vaso(tamanio)
        self.seleccionar_azucar(azucar)
        return self.recoger_vaso()

