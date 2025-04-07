import xml.etree.ElementTree as ET

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

# Archivos
xml_file = './ironer/example.xml'
template_file = './ironer/template.html'
output_file = './ironer/output.html'

# Ejecutar
data = load_data_from_xml(xml_file)
render_template(template_file, output_file, data)