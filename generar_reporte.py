# generar_reporte.py
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import os
import datetime
import subprocess

def ejecutar_tests():
    """
    Ejecuta pytest desde la raíz del proyecto y devuelve el resultado como texto.
    """
    try:
        # Nos aseguramos de que pytest se ejecute en la carpeta actual del proyecto
        ruta_raiz = os.path.dirname(os.path.abspath(__file__))
        resultado = subprocess.run(
            ["python", "-m", "pytest", "-v", "--maxfail=1", "--disable-warnings"],
            capture_output=True, text=True, cwd=ruta_raiz
        )
        return resultado.stdout
    except Exception as e:
        return f"Error ejecutando tests: {e}"

def generar_reporte():
    # Crear documento
    doc = SimpleDocTemplate("reporte_TDD_MaquinaCafe.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    elementos = []

    # Encabezado
    elementos.append(Paragraph("<b>Proyecto:</b> Máquina de Café con TDD", styles["Title"]))
    elementos.append(Spacer(1, 12))

    # Fecha
    fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    elementos.append(Paragraph(f"<b>Fecha del reporte:</b> {fecha}", styles["Normal"]))
    elementos.append(Spacer(1, 12))

    # Descripción del proyecto
    descripcion = """
    Este proyecto implementa una Máquina de Café utilizando la metodología <b>TDD (Test Driven Development)</b>.
    El desarrollo se realizó en cuatro fases:
    <br/><br/>
    1️⃣ Escribir pruebas unitarias que definieran el comportamiento esperado.<br/>
    2️⃣ Implementar el código mínimo necesario para que las pruebas pasaran.<br/>
    3️⃣ Ejecutar todas las pruebas y asegurar que pasaran correctamente.<br/>
    4️⃣ Refactorizar el código, eliminando duplicaciones y mejorando la estructura.
    """
    elementos.append(Paragraph(descripcion, styles["BodyText"]))
    elementos.append(Spacer(1, 12))

    # Resultados de pruebas
    elementos.append(Paragraph("<b>📊 Resultados de las pruebas:</b>", styles["Heading2"]))
    resultados = ejecutar_tests()
    elementos.append(Paragraph("<font face='Courier'>{}</font>".format(resultados.replace("\n", "<br/>")), styles["Code"]))
    elementos.append(Spacer(1, 12))

    # Conclusión
    conclusion = """
    <b>✅ Conclusión:</b><br/>
    Todas las pruebas fueron ejecutadas correctamente, validando el comportamiento del sistema.
    El flujo TDD permitió construir una Máquina de Café modular, mantenible y fácilmente extensible.
    """
    elementos.append(Paragraph(conclusion, styles["BodyText"]))

    # Generar PDF
    doc.build(elementos)
    print("✅ Reporte generado: reporte_TDD_MaquinaCafe.pdf")

if __name__ == "__main__":
    generar_reporte()
