import os
import shutil
import time
from datetime import datetime
from app import app
from flask_frozen import Freezer

# Configuración
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', 'CNAME', '.nojekyll']
app.config['FREEZER_STATIC_IGNORE'] = ['*.scss', '*.less', '*.js.map']

freezer = Freezer(app)

def clean_docs_folder():
    """Limpia completamente la carpeta docs"""
    print("🧹 Iniciando limpieza de la carpeta docs...")
    
    if os.path.exists('docs'):
        try:
            # Mostrar qué se va a eliminar
            old_files = []
            for root, dirs, files in os.walk('docs'):
                for file in files:
                    old_files.append(os.path.join(root, file))
            
            if old_files:
                print(f"🗑️  Eliminando {len(old_files)} archivos antiguos...")
            
            shutil.rmtree('docs')
            print("✅ Carpeta docs eliminada completamente")
            time.sleep(0.5)
        except Exception as e:
            print(f"❌ Error eliminando docs: {e}")
            return False
    
    # Crear carpeta docs vacía
    try:
        os.makedirs('docs', exist_ok=True)
        print("✅ Carpeta docs creada exitosamente")
        return True
    except Exception as e:
        print(f"❌ Error creando docs: {e}")
        return False

def show_generated_files():
    """Muestra qué archivos se generaron"""
    print("\n📋 ARCHIVOS GENERADOS:")
    print("-" * 50)
    
    file_count = 0
    total_size = 0
    
    for root, dirs, files in os.walk('docs'):
        level = root.replace('docs', '').count(os.sep)
        indent = ' ' * 2 * level
        
        folder_name = os.path.basename(root) if root != 'docs' else 'docs'
        if folder_name:
            print(f"{indent}📁 {folder_name}/")
        
        sub_indent = ' ' * 2 * (level + 1)
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            total_size += file_size
            
            print(f"{sub_indent}📄 {file} ({file_size} bytes)")
            file_count += 1
    
    print("-" * 50)
    size_kb = total_size / 1024
    print(f"📊 TOTAL: {file_count} archivos, {size_kb:.1f} KB")
    return file_count

def main():
    """Función principal"""
    start_time = datetime.now()
    print("🚀 INICIANDO GENERACIÓN DE SITIO ESTÁTICO")
    print(f"⏰ Hora de inicio: {start_time.strftime('%H:%M:%S')}")
    print("=" * 60)
    
    # Paso 1: Limpiar carpeta docs
    if not clean_docs_folder():
        print("❌ No se pudo limpiar la carpeta docs. Abortando...")
        return
    
    # Paso 2: Generar sitio estático
    print("\n🔨 Generando archivos estáticos...")
    try:
        freezer.freeze()
        print("✅ ¡Generación completada exitosamente!")
    except Exception as e:
        print(f"❌ Error durante la generación: {e}")
        print("💡 Posibles soluciones:")
        print("   - Verifica que todas las rutas en app.py sean correctas")
        print("   - Asegúrate de que los templates existan")
        print("   - Cierra programas que usen la carpeta docs")
        return
    
    # Paso 3: Mostrar resultados
    file_count = show_generated_files()
    
    # Paso 4: Estadísticas finales
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    print("\n🎉 GENERACIÓN COMPLETADA")
    print("=" * 60)
    print(f"⏰ Duración: {duration:.2f} segundos")
    print(f"📁 Carpeta destino: docs/")
    print(f"📄 Archivos generados: {file_count}")
    
    # Instrucciones para probar
    print("\n🌐 PARA PROBAR TU SITIO:")
    print("   cd docs")
    print("   python -m http.server 8000")
    print("   Luego visita: http://localhost:8000")
    
    # Instrucciones para GitHub Pages
    print("\n📤 PARA SUBIR A GITHUB PAGES:")
    print("   git add docs/")
    print("   git commit -m 'Actualizar sitio estático'")
    print("   git push origin main")

if __name__ == '__main__':
    main()