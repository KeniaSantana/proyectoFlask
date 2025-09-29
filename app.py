from flask import Flask
app = Flask(__name__)

@app.route('/')  # raiz
def hola_mundo():
    return '<h1>¡Hola mundo desde Flask!</h1>'
if __name__ == '__main__':
    
@app.route('/parrafo')
def parrafo():
    return '''<p>xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</p>'''

@app.route('/Factorial/<v1>')
def factorial(v1):
    f = 1
    for x in range(1, int(v1) + 1):
        f *= x
    return f"El factorial de {v1} es: {f}"

if __name__ == '__main__':
    app.run(debug=True)