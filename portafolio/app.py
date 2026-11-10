from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Datos del estudiante (simulan una base de datos o almacenamiento local)
PERFIL_DATA = {
    "estudiante": {
        "nombre": "Andy Altamirano",
        "rol": "Desarrollador Junior & Estudiante de Tecnología",
        "bio": "Apasionado por la programación en Python, el desarrollo web responsivo y el diseño de videojuegos 2D. Enfocado en construir soluciones de software limpias y funcionales."
    },
    "habilidades": [
        "Python (Scripting & Tablas)",
        "HTML5 & CSS3 Moderno",
        "JavaScript (Vanilla ES6+)",
        "Git & GitHub",
        "Lógica de Programación",
        "Despliegue Web (Vercel)"
    ],
    "proyectos": [
        {
            "titulo": "Enlistador de Datos Python",
            "descripcion": "Programa de consola desarrollado en Python utilizando librerías de formato para estructurar tablas de datos dinámicas.",
            "link": "https://github.com"
        },
        {
            "titulo": "Adaptador Curricular NEE",
            "descripcion": "Aplicación y maquetación web enfocada en adaptar contenidos educativos, desplegada para acceso remoto.",
            "link": "https://vercel.com"
        },
        {
            "titulo": "Prototipo 2D Godot Engine",
            "descripcion": "Diseño de mecánicas básicas, colocación de assets y pixel art para prototipos de videojuegos 2D.",
            "link": "https://github.com"
        }
    ]
}

@app.route('/')
def index():
    # Carga la página principal del portafolio
    return render_template('index.html')

@app.route('/api/perfil', methods=['GET'])
def get_perfil():
    # Endpoint REST que retorna los datos en JSON para consumo del JavaScript en el cliente
    return jsonify(PERFIL_DATA)

if __name__ == '__main__':
    app.run(debug=True, port=5000)