from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave-secreta-temporal'

# Datos del portfolio (personaliza estos datos)
portfolio_data = {
    'name': 'Gabriel Silva',
    'title': 'Desarrollador Full Stack',
    'email': 'tu.email@ejemplo.com',
    'phone': '+1234567890',
    'location': 'Tu Ciudad, País',
    'about': 'Soy un apasionado desarrollador con experiencia en tecnologías web modernas.',
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
            'technologies': ['Python', 'Flask', 'Bootstrap'],
            'github_url': '#',
            'demo_url': '#',
            'image': 'project1.jpg'
        }
    ]
}

@app.route('/')
def index():
    return render_template('index.html', data=portfolio_data)

@app.route('/about')
def about():
    return render_template('about.html', data=portfolio_data)

@app.route('/projects')
def projects():
    return render_template('projects.html', data=portfolio_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        print(f"📧 Mensaje de: {name} ({email})")
        print(f"📝 Asunto: {subject}")
        print(f"💬 Mensaje: {message}")
        
        flash('¡Mensaje enviado! Te contactaré pronto.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)