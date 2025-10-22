from flask import Flask, render_template, request, flash, redirect, url_for
import os
import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave-secreta-temporal'

# Configuración para Frozen-Flask
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'

# Datos del portfolio - ¡PERSONALIZA ESTOS DATOS!
portfolio_data = {
    'name': 'Gabriel Silva',
    'title': 'Desarrollador Full Stack (Junior)',
    'email': 'ags0014@gmail.com',
    'phone': '2475 - 414146',
    'location': 'Rojas, Argentina',
    'about': 'Soy estudiante en Programación, creo que mi mayor fortaleza es mi capacidad de aprendizaje y la adaptabilidad. Me tomo con entusiasmo cada nuevo desafio porque creo que es la oportunidad perfecta para aprender algo nuevo.',
    'skills': [
        {'name': 'Python', 'level': ' Intermedio', 'category': 'Backend', 'icon': 'fab fa-python'},
        {'name': 'Flask', 'level': ' Intermedio', 'category': 'Backend', 'icon': 'fas fa-flask'},
        {'name': 'JavaScript', 'level': ' Intermedio', 'category': 'Frontend', 'icon': 'fab fa-js-square'},
        {'name': 'HTML/CSS', 'level': ' Avanzado', 'category': 'Frontend', 'icon': 'fab fa-html5'},
        {'name': 'Git', 'level': ' Intermedio', 'category': 'Herramientas', 'icon': 'fab fa-git-alt'},
        {'name': 'SQL', 'level': ' Intermedio', 'category': 'Base de Datos', 'icon': 'fas fa-database'},
        {'name': 'Bootstrap', 'level': ' Básico', 'category': 'Frontend', 'icon': 'fab fa-bootstrap'},
        {'name': 'Node.js', 'level': ' Básico', 'category': 'Backend', 'icon': 'fab fa-node-js'},
        {'name': 'Express', 'level': ' Intermedia', 'category': 'Backend', 'icon': 'fas fa-server'}
    ],
    'projects': [
        {
            'title': 'Portfolio Personal',
            'description': 'Portfolio desarrollado con Flask y Bootstrap',
            'technologies': ['Python', 'Flask', 'Bootstrap', 'Git'],
            'github_url': 'https://github.com/tuusuario/portfolio',
            'demo_url': '#',
            'image': 'project1.jpg'
        },
        {
            'title': 'Sistema de Gestión de Tareas',
            'description': 'Sistema para gestión de tareas y proyectos para la empresa Cargill',
            'technologies': ['Python', 'Django', 'PostgreSQL', 'React'],
            'github_url': 'https://github.com/tuusuario/sistema-gestion',
            'demo_url': '#',
            'image': 'project2.jpg'
        },
        {
            'title': 'API REST',
            'description': 'API REST desarrollada con Flask',
            'technologies': ['Python', 'Flask', 'JWT', 'MongoDB'],
            'github_url': 'https://github.com/tuusuario/api-rest',
            'demo_url': '#',
            'image': 'project3.jpg'
        },
        {
            'title': 'Login y Register',
            'description': 'Interfaz de usuario para login y registro creada con React',
            'technologies': ['React', 'Node.js', 'Express', 'MongoDB'],
            'github_url': 'https://github.com/tuusuario/login-register',
            'demo_url': '#',
            'image': 'project4.jpg'
        }
    ],
    'experience': [
        {
            'position': 'Estudiante Autónomo',
            'company': 'FreeCodeCamp',
            'period': '2023 - 2024',
            'description': 'Certificacion en HTML y CSS'
        },
        {
            'position': 'Estudiante de la provincia de Bs.As',
            'company': 'Codo a Codo 4.0',
            'period': '02/2024 - 08/2024',
            'description': 'Python'
        }
    ],
    'education': [
        {
            'degree': 'Python Inicial',
            'institution': 'Codo a Codo 4.0',
            'period': '2024 - 2025'
        },
        {
            'degree': 'Tecnico en Programación',
            'institution': 'Techlabs',
            'period': '2025 - 2026'
        }
    ],
    'social_links': {
        'github': 'https://github.com/GabrielSilva-A',
        'linkedin': 'https://www.linkedin.com/in/gabriel-silva-75341a219/',
    }
}

@app.route('/')
def index():
    return render_template('index.html', data=portfolio_data)

@app.route('/about/')
def about():
    return render_template('about.html', data=portfolio_data)

@app.route('/projects/')
def projects():
    return render_template('projects.html', data=portfolio_data)

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Procesar formulario con validación básica
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()
        
        # Validación de campos obligatorios
        if not name or not email or not message:
            flash('Por favor, completa todos los campos obligatorios.', 'error')
            return render_template('contact.html', data=portfolio_data)
        
        print(f"📧 Nuevo mensaje de contacto:")
        print(f"   De: {name} ({email})")
        print(f"   Asunto: {subject}")
        print(f"   Mensaje: {message}")
        
        flash('¡Mensaje recibido! Te contactaré pronto.', 'success')
        return redirect(url_for('contact'))
    
    # Mostrar formulario (GET request)
    return render_template('contact.html', data=portfolio_data)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "freeze":
        from flask_frozen import Freezer
        freezer = Freezer(app)
        freezer.freeze()
        print("✅ Sitio estático generado en carpeta 'docs/'")
    else:
        app.run(debug=True)