from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo! Mi primera app de Flask'
@app.route('/Beto')
def Beto():
    return 'Hola estás en la página Beto'

if __name__== '__main__':
    app.run(host='0.0.0.0', port=8888)

