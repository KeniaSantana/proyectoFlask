from flask import Flask
app=Flask(__name__)
@app.route('/') ##raiz

def hola_mundo():
    return '<h1>¡Hola mundo desde Flask!</h1>'
if __name__=='__main__':
    app.run(debug=True)

def home():
    mensaje='<h1></h1>'