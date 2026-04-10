
# Manejar PDF's

# Leer PDF's y unirlos

from pypdf import PdfWriter
from pypdf import PdfReader
#import numpy as np


# pdf_writer = PdfWriter()
# pdf_writer.add_blank_page(595.28, 841.89)

# with open("pdf1.pdf", "wb") as f:
#     pdf_writer.write(f)

# with open("pdf2.pdf", "wb") as f:
#     pdf_writer.write(f)

pdf_merger = PdfWriter()

ruta = "./python/"
pd1 = ruta + "pdf1.pdf"
print (pd1)
pd2 = ruta + "pdf2.pdf"
pd_f = ruta +'unidos.pdf'

with open(pd1, 'rb') as file1:
    pdf_merger.append(file1)

with open(pd2, 'rb') as file2:
    pdf_merger.append(file2)

with open(pd_f, 'wb') as output_file:
    pdf_merger.write(output_file)

# Leer contenido del fichero unido

# Ruta a tu archivo PDF
ruta_pdf = './doc/unidos.pdf' # O la ruta completa

# Abrir el archivo en modo lectura binaria ('rb')
with open(pd_f, 'rb') as archivo_pdf:
    lector = PdfReader(archivo_pdf) # Crear un objeto lector
    num_paginas = len(lector.pages) # Obtener número de páginas
    print(f"Número de páginas: {num_paginas}")
    
    texto_completo = ""
    for pagina in range(0, num_paginas):
        cont_pag = lector.pages[pagina]
        texto_completo += cont_pag.extract_text()

    for i in range(1, num_paginas+1):
        print(f"Texto página: {i}: ")
        print(texto_completo)



# from pypdf import PdfReader

# def obtener_numero_paginas(ruta_pdf):
#     """Extrae el número de páginas de un archivo PDF."""
#     try:
#         reader = PdfReader(ruta_pdf)
#         numero_paginas = len(reader.pages) # O reader.numPages en versiones antiguas
#         # print(f"El archivo '{ruta_pdf}' tiene {numero_paginas} páginas.")
#         return numero_paginas
#     except Exception as e:
#         print(f"Error al leer el PDF: {e}")
#         return None

# # Ejemplo de uso
# nombre_archivo = "mi_documento.pdf" # ¡Asegúrate de que este archivo exista!
# paginas = obtener_numero_paginas(nombre_archivo)

# if paginas is not None:
#     print(f"Número de páginas: {paginas}")
