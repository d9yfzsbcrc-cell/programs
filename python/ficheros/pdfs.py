
# Manejar PDF's

# Crear 2 PDF's y unirlos

from pypdf import PdfWriter
from pypdf import PdfReader

pdf_writer = PdfWriter()
pdf_writer.add_blank_page(595.28, 841.89)


with open("pdf1.pdf", "wb") as f:
    pdf_writer.write(f)

with open("pdf2.pdf", "wb") as f:
    pdf_writer.write(f)

pdf_merger = PdfWriter()

with open("pdf1.pdf", 'rb') as file1:
    pdf_merger.append(file1)

with open("pdf2.pdf", 'rb') as file2:
    pdf_merger.append(file2)

with open("unidos.pdf", 'wb') as output_file:
    pdf_merger.write(output_file)

# Leer contenido del fichero unido

# Ruta a tu archivo PDF
ruta_pdf = 'unidos.pdf' # O la ruta completa

# Abrir el archivo en modo lectura binaria ('rb')
with open(ruta_pdf, 'rb') as archivo_pdf:
    lector = PdfReader(archivo_pdf) # Crear un objeto lector
    num_paginas = len(lector.pages) # Obtener número de páginas
    print(f"Número de páginas: {num_paginas}")

    # Leer texto de la primera página
    pagina_uno = lector.pages[0]
    texto = pagina_uno.extract_text()
    print("Texto de la primera página:\n", texto)