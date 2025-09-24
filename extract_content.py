import re
import os

def extract_content_from_prompt(file_path):
    """
    Lee el archivo prompt.md y extrae el contenido para generar archivos .md y .dio
    """
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {file_path}")
        return
    
    # Extraer contenido para Google Slides (Marp)
    slide_pattern = r'## content for the google slide\s*```(?:markdown)?\s*(.*?)```'
    slide_match = re.search(slide_pattern, content, re.DOTALL)
    
    if slide_match:
        slide_content = slide_match.group(1).strip()
        with open('generated_slides.md', 'w', encoding='utf-8') as f:
            f.write(slide_content)
        print("✅ Archivo 'generated_slides.md' creado exitosamente")
    else:
        print("❌ No se encontró contenido para las slides")
    
    # Extraer diagramas DrawIO
    diagram_pattern = r'```(\w+_\w+_[\w\s]+)\s*<(.*?)```'
    diagram_matches = re.findall(diagram_pattern, content, re.DOTALL)
    
    if diagram_matches:
        for i, (diagram_name, xml_content) in enumerate(diagram_matches):
            # Limpiar el nombre del archivo
            clean_name = re.sub(r'[^\w\s-]', '', diagram_name).strip()
            clean_name = re.sub(r'[-\s]+', '_', clean_name)
            filename = f"{clean_name}.dio"
            
            # Asegurarse de que el XML esté bien formateado
            xml_content = xml_content.strip()
            if not xml_content.startswith('<?xml'):
                xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n' + xml_content
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(xml_content)
            print(f"✅ Archivo '{filename}' creado exitosamente")
    else:
        print("❌ No se encontraron diagramas DrawIO")
    
    # Extraer CSV de estimaciones
    csv_pattern = r'## a csv that contains the estimation\s*```csv\s*(.*?)```'
    csv_match = re.search(csv_pattern, content, re.DOTALL)
    
    if csv_match:
        csv_content = csv_match.group(1).strip()
        with open('estimation.csv', 'w', encoding='utf-8') as f:
            f.write(csv_content)
        print("✅ Archivo 'estimation.csv' creado exitosamente")
    else:
        print("❌ No se encontró contenido CSV")
    
    # Extraer "what should be said in each slide"
    speech_pattern = r'## what should be said in each slide\s*```(?:markdown)?\s*(.*?)```'
    speech_match = re.search(speech_pattern, content, re.DOTALL)
    
    if speech_match:
        speech_content = speech_match.group(1).strip()
        with open('presentation_notes.md', 'w', encoding='utf-8') as f:
            f.write(speech_content)
        print("✅ Archivo 'presentation_notes.md' creado exitosamente")
    else:
        print("❌ No se encontró contenido de notas de presentación")

def main():
    """
    Función principal que ejecuta la extracción
    """
    prompt_file = "/workspaces/AI_engineer/prompt.md"
    
    print("🚀 Iniciando extracción de contenido...")
    print(f"📁 Leyendo archivo: {prompt_file}")
    print("-" * 50)
    
    extract_content_from_prompt(prompt_file)
    
    print("-" * 50)
    print("✨ Proceso completado")
    
    # Listar archivos generados
    generated_files = [
        'generated_slides.md',
        'estimation.csv', 
        'presentation_notes.md'
    ]
    
    dio_files = [f for f in os.listdir('.') if f.endswith('.dio')]
    generated_files.extend(dio_files)
    
    print("\n📄 Archivos generados:")
    for file in generated_files:
        if os.path.exists(file):
            size = os.path.getsize(file)
            print(f"  • {file} ({size} bytes)")

if __name__ == "__main__":
    main()