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
    'email': 'ags0014@ejemplo.com',
    'phone': '2475414146',
    'location': 'Rojas, Argentina',
    'about': 'Soy estudiante en Programacion, creo que mi mayor fortaleza es mi capacidad de aprendizaje y la adaptabilidad. Me tomo con entusiasmo cada nuevo desafio porque creo que es la oportunidad perfecta para aprender algo nuevo.',
    'skills': [
        {'name': 'Python', 'level': 'Avanzado', 'category': 'Backend', 'icon': 'fab fa-python'},
        {'name': 'Flask', 'level': 'Avanzado', 'category': 'Backend', 'icon': 'fas fa-flask'},
        {'name': 'JavaScript', 'level': 'Intermedio', 'category': 'Frontend', 'icon': 'fab fa-js-square'},
        {'name': 'HTML/CSS', 'level': 'Avanzado', 'category': 'Frontend', 'icon': 'fab fa-html5'},
        {'name': 'Git', 'level': 'Intermedio', 'category': 'Herramientas', 'icon': 'fab fa-git-alt'},
        {'name': 'SQL', 'level': 'Intermedio', 'category': 'Base de Datos', 'icon': 'fas fa-database'},
        {'name': 'Bootstrap', 'level': 'Avanzado', 'category': 'Frontend', 'icon': 'fab fa-bootstrap'},
        {'name': 'Node', 'level': 'Básico', 'category': 'Frontend', 'icon': 'fab fa-node' },
        {'name': 'Express', 'level': 'Básico', 'category': 'Backend', 'icon': 'fab fa-express' }
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
            'description': 'API REST desarrollada con Node.js y Express',
            'technologies': ['Python', 'Flask', 'JWT', 'MongoDB'],
            'github_url': 'https://github.com/tuusuario/api-rest',
            'demo_url': '#',
            'image': 'project3.jpg'
        },
        {
            'title': 'Login y Register',
            'description': 'Interfaz de usuario para login y registro creada con React',
            'technologies': ['Node', 'Express', 'PostgreSQL', 'JavaScript'],
            'github_url': 'https://github.com/tuusuario/api-rest',
            'demo_url': '#',
            'image': 'project4.jpg'
        }
    ],
    'experience': [
        {
            'position': 'Desarrollador Full Stack',
            'company': 'Tech Solutions Inc.',
            'period': '2022 - Presente',
            'description': 'Desarrollo de aplicaciones web con Python y JavaScript'
        },
        {
            'position': 'Practicante de Desarrollo',
            'company': 'StartUp Innovadora',
            'period': '2021 - 2022',
            'description': 'Desarrollo de features frontend y backend'
        }
    ],
    'education': [
        {
            'degree': 'Técnico en Programción',
            'institution': 'Instituto Tecnologico Argentino, Teclab',
            'period': '2025 - 2026'
        },
        {
            'degree': 'Python Inicial',
            'institution': 'Codo a Codo 4.0',
            'period': '2024 - 2025'
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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Procesar formulario
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
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