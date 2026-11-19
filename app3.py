import streamlit as st
import Calculos
import Presupuesto_PDF
st.title("Kiosco Laucha")
fecha = st.date_input("Fecha")
cliente = st.text_input("Ingrese el nombre del cliente:")
cliente = Presupuesto_PDF.limpiar(cliente) 

def aplicar_descuento(total, porcentaje):
    return total - (total * porcentaje / 100)

def calcular_iva(total, porcentaje):
    return total * porcentaje / 100

precio = {
    "Agua": 2500,
    "Gaseosa": 3000,
    "Sanguche de milanesa": 4000,
    "Panchos": 2500,
    "Pizza": 8000,
    "Hamburguesa": 7000
}

st.title("Mi compra")
st.subheader("Elegí los productos")

cantidad_Hamburguesa = st.number_input("Hamburguesa - 7000", min_value=0, step=1)
cantidad_Pizza = st.number_input("Pizza - 8000", min_value=0, step=1)
cantidad_Panchos = st.number_input("Panchos - 2500", min_value=0, step=1)
cantidad_Sanguches_de_milanesa = st.number_input("Sanguche de milanesa - 4000", min_value=0, step=1)
cantidad_Gaseosa = st.number_input("Gaseosa - 3000", min_value=0, step=1)
cantidad_Agua = st.number_input("Agua - 2500", min_value=0, step=1)

subtotal = (
    cantidad_Agua * 2500 + 
    cantidad_Gaseosa * 3000 + 
    cantidad_Sanguches_de_milanesa * 4000 + 
    cantidad_Panchos * 2500 + 
    cantidad_Pizza * 8000 + 
    cantidad_Hamburguesa * 7000
)

forma_pago = st.radio("Forma de pago: ", ["EFECTIVO", "TRANSFERENCIA"])

descuento = (subtotal / 5)
iva = Calculos.calcular_iva(descuento * 21)
total = round(descuento + iva)

st.write(f"Precio: ${precio}")
st.write(f"Subtotal: ${subtotal}")
st.write(f"Descuento: ${descuento}")
st.write(f"IVA 21%: ${iva}")
st.write(f"Total: ${total}")

if cliente == "": 
    st.warning("Escribí el nombre del cliente para armar el presupuesto") 
else: 
    archivo_pdf = Presupuesto_PDF.armar_pdf(
        fecha=fecha,
        cliente=cliente,
        cantidad_Pizza=cantidad_Pizza,
        cantidad_Hamburguesa=cantidad_Hamburguesa,
        cantidad_Panchos=cantidad_Panchos,
        cantidad_Sanguches_de_milanesa=cantidad_Sanguches_de_milanesa,
        cantidad_Gaseosa=cantidad_Gaseosa,
        cantidad_Agua=cantidad_Agua,
        descuento=descuento,
        iva=iva,
        total=total
    )
    st.download_button(
        label="Descargá el archivo (PDF)",
        data=archivo_pdf,
        file_name=f"presupuesto_{fecha}.pdf",
        mime="application/pdf"
    )