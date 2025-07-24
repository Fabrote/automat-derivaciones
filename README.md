# Automatización de Derivaciones Médicas

Este proyecto automatiza la gestión de pagos mensuales por derivaciones médicas. Se compone de dos funcionalidades principales:

1. 📊 Generación automática de un Excel con los datos de pago por profesional.
2. 📧 Envío automatizado de correos electrónicos a cada profesional con el detalle de facturación.

---

## 🛠️ Tecnologías utilizadas

- Python 3.11+
- pandas
- openpyxl
- smtplib (envío de mails)
- dotenv (`python-dotenv`)
- Formato `.env` para configuración sensible
- Excel `.xlsx` como entrada y salida de datos

---


✅ ¿Cómo funciona?
---

1- Generación del Excel

Ejecutá:

python automat-excel.py
Este script:

Lee los archivos origen.xlsx y profesionales.xlsx.

Matchea por nombre.

Crea o actualiza ordenes_pago.xlsx, agregando una hoja nueva con los datos del mes.

Deja columnas vacías para Nº de factura y observaciones.

2- Envío de emails

Ejecutá:

python automat-mail.py

Este script:

Lee ordenes_pago.xlsx.

Envía un correo personalizado a cada profesional, con el monto, CUIT y fecha límite.

Usa los datos del archivo .env.


🔐 Seguridad
---

Nunca compartas tu archivo .env.

Está en el .gitignore para evitar que se suba a GitHub.

No incluyas credenciales en el código fuente.


🧠 Ideas a futuro
---

Leer facturas PDF automáticamente y completar el campo "N° de factura".

Subida de archivos adjuntos por email.

Interfaz gráfica para facilitar su uso.

Exportación a PDF del resumen mensual.


🤟 Autor
---
Fabrizio

Hecho para uso interno de Empresa de Salud.

