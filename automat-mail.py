import pandas as pd
import smtplib
from email.message import EmailMessage
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL_USER")
PASSWORD = os.getenv("EMAIL_PASSWORD")
CUIT = os.getenv("CUIT_EMPRESA")
NOMBRE_EMPRESA = os.getenv("NOMBRE_EMPRESA")


ARCHIVO_EXCEL = 'ordenes_pago_2025.xlsx'  
HOJA = input("Nombre de la hoja a usar: ")
MES_ACTUAL = input("Mes de facturacion): ")
FECHA_LIMITE = input("Fecha límite para recibir facturas: ")

df = pd.read_excel(ARCHIVO_EXCEL, sheet_name=HOJA)

if not {'Nombre', 'Monto', 'CBU/Alias', 'Nro de Factura', 'Observaciones'}.issubset(df.columns):
    raise Exception("Las columnas necesarias no están presentes en la hoja.")

if 'Email' not in df.columns:
    raise Exception("Falta la columna 'Email' en el Excel para poder enviar los correos.")

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(EMAIL, PASSWORD)

for _, row in df.iterrows():
    nombre = row['Nombre']
    monto = row['Monto']
    destinatario = row['Email']

    if pd.isna(destinatario) or pd.isna(monto):
        continue  

    mensaje = EmailMessage()
    mensaje['Subject'] = f"Factura por honorarios - {MES_ACTUAL}"
    mensaje['From'] = EMAIL
    mensaje['To'] = destinatario

    cuerpo = f"""Buen día,

Le indico la información para emitir la factura correspondiente a las derivaciones del mes de {MES_ACTUAL}.

* Total: ${monto:,.2f}
* CUIT: {CUIT}
* Concepto: Honorarios

El plazo para la recepción de facturas vence el {FECHA_LIMITE}.

Saludos cordiales,

{NOMBRE_EMPRESA}
"""
    mensaje.set_content(cuerpo)

    try:
        server.send_message(mensaje)
        print(f"✅ Correo enviado a {nombre} ({destinatario})")
    except Exception as e:
        print(f"❌ Error al enviar a {nombre}: {e}")

server.quit()
print("Todos los correos fueron procesados.")
