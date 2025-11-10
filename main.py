# main.py
from maquina_cafe import MaquinaCafe
from excepciones import SinVasosError, SinAzucarError, SinCafeError, SeleccionInvalidaError

def menu():
    print("=== Bienvenido a la Máquina de Café ===")
    print("Tipos de café disponibles:")
    print("1. Expreso")
    print("2. Expreso con leche")
    print("3. Americano")
    print("0. Salir")

def seleccionar_tipo(opcion):
    if opcion == "1":
        return "expreso"
    elif opcion == "2":
        return "con leche"
    elif opcion == "3":
        return "americano"
    elif opcion == "0":
        return None
    else:
        raise SeleccionInvalidaError("Opción inválida")

def main():
    maquina = MaquinaCafe(vasos=5, azucar=5, cafe=5, leche=2)

    while True:
        menu()
        opcion = input("Seleccione su café: ")
        if opcion == "0":
            print("Gracias por usar la máquina. ¡Hasta luego!")
            break

        try:
            tipo = seleccionar_tipo(opcion)
            mensaje = maquina.preparar_cafe(tipo=tipo)
            print(mensaje)
            print("Inventario restante:", 
                  f"Vasos={maquina.inventario.vasos}, ",
                  f"Azúcar={maquina.inventario.azucar}, ",
                  f"Café={maquina.inventario.cafe}, ",
                  f"Leche={maquina.inventario.leche}")
        except (SinVasosError, SinAzucarError, SinCafeError) as e:
            print(f"Error: {e}")
        except SeleccionInvalidaError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
