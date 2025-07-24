import pandas as pd
from openpyxl import load_workbook 

df_montos = pd.read_excel('montos.xlsx')
df_profesionales = pd.read_excel('profesionales.xlsx')

df_merge =pd.merge(df_montos, df_profesionales, on='nombres', how='left') #probar con 'right', 'outer', 'inner'.

df_final = pd.DataFrame({
    'Nombre': df_merge['nombres'],
    'Nro de Factura': '',
    'CBU/Alias': df_merge['cbu/alias'],
    'CUIT': df_merge['cuit'],
    'Monto': df_merge['monto'],
    'Email' : df_merge['mail'],
    'Observaciones': ''
})

df_final['Monto'] = (
    df_final['Monto'].astype(str).str.strip().str.replace(",", "", regex=False)
)
df_final['Monto'] = pd.to_numeric(df_final['Monto'], errors='coerce')


archivo_final = 'ordenes_pago_2025.xlsx'

nombre_hoja = input("Nombre de la hoja para este mes: ")

try:
    with pd.ExcelWriter(archivo_final, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df_final.to_excel(writer, sheet_name=nombre_hoja, index=False)
except FileNotFoundError:
    with pd.ExcelWriter(archivo_final, engine='openpyxl') as writer:
        df_final.to_excel(writer, sheet_name=nombre_hoja, index=False)

print(f"Hoja '{nombre_hoja}' agregada exitosamente a {archivo_final}")