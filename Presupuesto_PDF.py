
from fpdf import FPDF

NOMBRE_KIOSCO = "Kiosco Laucha"
LOGO = "LOGO.LAUCHA.png"


def renglon(pdf, texto, valor):
    pdf.cell(120, 9, texto)
    pdf.cell(0, 9, valor, align="R", ln=1)


def limpiar(texto):
    return texto.encode("latin-1", "ignore").decode("latin-1").strip()


def armar_pdf(fecha, cliente, cantidad_Pizza, cantidad_Hamburguesa,
              cantidad_Panchos, cantidad_Sanguches_de_milanesa,
              cantidad_Gaseosa, cantidad_Agua, descuento, iva, total):

    pdf = FPDF()
    pdf.add_page()

    pdf.image(LOGO, x=10, y=10, w=48)

    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 12, NOMBRE_KIOSCO, align="R", ln=1)

    pdf.set_font("Helvetica", "", 11)
    pdf.cell(0, 7, f"Fecha: {fecha}", align="R", ln=1)

    pdf.ln(15)
    pdf.set_font("Helvetica", "", 12)

    renglon(pdf, "Cliente", limpiar(cliente))
    pdf.ln(4)

    productos_comprados = [
        ("Hamburguesa", cantidad_Hamburguesa, 7000),
        ("Pizza", cantidad_Pizza, 8000),
        ("Panchos", cantidad_Panchos, 2500),
        ("Sanguche de milanesa", cantidad_Sanguches_de_milanesa, 4000),
        ("Gaseosa", cantidad_Gaseosa, 3000),
        ("Agua", cantidad_Agua, 2500)
    ]

    for nombre, cantidad, precio_unitario in productos_comprados:
        if cantidad > 0:
            subtotal_producto = cantidad * precio_unitario
            renglon(
                pdf,
                f"{cantidad} x {nombre} (${precio_unitario} c/u)",
                f"${subtotal_producto}"
            )

    pdf.ln(4)

    renglon(pdf, "Descuento", f"-${descuento}")
    renglon(pdf, "IVA 21%", f"${iva}")

    pdf.set_font("Helvetica", "B", 14)
    renglon(pdf, "TOTAL", f"${total}")

    pdf.set_text_color(0, 0, 0)
    pdf.ln(10)

    pdf.set_font("Helvetica", "I", 9)
    pdf.cell(0, 6, "Presupuesto valido por 7 dias.", ln=1)

    return bytes(pdf.output())
