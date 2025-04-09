import xml.etree.ElementTree as ET
import os
import shutil

# Cargar el XML
def load_data_from_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    data = {child.tag: child.text for child in root}
    return data

# Cargar el template HTML y reemplazar campos
def render_template(template_path, output_path, data):
    with open(template_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Reemplazo de todas las variables con formato ###variable###
    for key, value in data.items():
        html = html.replace(f'###{key}###', value)

    # Guardar el resultado
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

import os
import shutil

def copiar_archivos(origen, destino):
    # Crea la carpeta destino si no existe
    if not os.path.exists(destino):
        os.makedirs(destino)

    # Recorre todos los archivos de la carpeta origen
    for archivo in os.listdir(origen):
        ruta_origen = os.path.join(origen, archivo)
        ruta_destino = os.path.join(destino, archivo)

        # Solo copia si es un archivo (no carpetas)
        if os.path.isfile(ruta_origen):
            shutil.copy2(ruta_origen, ruta_destino)
            print(f"Copiado: {archivo}")

# Ejemplo de uso:
# copiar_archivos("carpeta_origen", "carpeta_destino")


# Archivos
xml_file = './ironer/example.xml'
template_file = './ironer/template.html'
output_file = './ironer/output.html'

# Ejecutar
data = load_data_from_xml(xml_file)
render_template(template_file, output_file, data)