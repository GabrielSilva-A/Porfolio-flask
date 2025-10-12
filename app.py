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
    'name': 'Tu Nombre',
    'title': 'Desarrollador Full Stack',
    'email': 'tu.email@ejemplo.com',
    'phone': '+1234567890',
    'location': 'Tu Ciudad, País',
    'about': 'Soy un apasionado desarrollador con experiencia en tecnologías web modernas. Me encanta crear soluciones innovadoras y aprender nuevas tecnologías.',
    'skills': [
        {'name': 'Python', 'level': 90},
        {'name': 'Flask', 'level': 85},
        {'name': 'JavaScript', 'level': 80},
        {'name': 'HTML/CSS', 'level': 95},
        {'name': 'SQL', 'level': 75},
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
            'title': 'Sistema de Gestión',
            'description': 'Sistema para gestión de tareas y proyectos',
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
            'degree': 'Ingeniería en Sistemas',
            'institution': 'Universidad Ejemplo',
            'period': '2018 - 2022'
        }
    ],
    'social_links': {
        'github': 'https://github.com/tuusuario',
        'linkedin': 'https://linkedin.com/in/tuusuario',
        'twitter': 'https://twitter.com/tuusuario'
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

@app.route('/contact/')
def contact():
    return render_template('contact.html', data=portfolio_data)

# Esta ruta solo funciona en desarrollo
@app.route('/contact', methods=['POST'])
def contact_post():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        print(f"📧 Mensaje de contacto:")
        print(f"De: {name} ({email})")
        print(f"Asunto: {subject}")
        print(f"Mensaje: {message}")
        
        flash('¡Mensaje enviado! (Solo en desarrollo)', 'success')
    
    return redirect('/contact/')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "freeze":
        from flask_frozen import Freezer
        freezer = Freezer(app)
        freezer.freeze()
        print("✅ Sitio estático generado en carpeta 'docs/'")
    else:
        app.run(debug=True)