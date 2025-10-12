import os
import shutil
from app import app
from flask_frozen import Freezer

# Configuración adicional para Frozen-Flask
app.config['FREEZER_DESTINATION'] = 'docs/'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', 'CNAME']
app.config['FREEZER_STATIC_IGNORE'] = ['*.scss', '*.less']

freezer = Freezer(app)

def clean_docs_folder():
    """Limpiar la carpeta docs antes de generar"""
    if os.path.exists('docs'):
        try:
            shutil.rmtree('docs')
            print("🗑️  Carpeta docs eliminada")
        except Exception as e:
            print(f"⚠️  No se pudo eliminar docs: {e}")
    
    # Crear carpeta docs vacía
    os.makedirs('docs', exist_ok=True)
    print("📁 Carpeta docs creada")

if __name__ == '__main__':
    print("🚀 Preparando generación de sitio estático...")
    
    # Limpiar carpeta docs
    clean_docs_folder()
    
    try:
        print("🔨 Generando archivos estáticos...")
        freezer.freeze()
        print("✅ ¡Sitio estático generado exitosamente!")
        print("📂 Archivos guardados en: docs/")
        
        # Mostrar qué se generó
        print("\n📋 Archivos generados:")
        count = 0
        for root, dirs, files in os.walk('docs'):
            for file in files:
                path = os.path.join(root, file)
                relative_path = os.path.relpath(path, 'docs')
                print(f"   📄 {relative_path}")
                count += 1
        
        print(f"\n🎉 Total: {count} archivos generados")
        print("\n🌐 Para ver tu sitio:")
        print("   cd docs && python -m http.server 8000")
        print("   Luego visita: http://localhost:8000")
        
    except Exception as e:
        print(f"❌ Error durante la generación: {e}")
        print("💡 Solución: Cierra cualquier programa que esté usando la carpeta 'docs'")