from flask import Flask, render_template, request, redirect
from modelos.listas_enlazadas import ListaEnlazada
from modelos.libro import Libro
from modelos.usuario import Usuario
from modelos.operacion import Operacion
from ml.recomendador import Recomendador
from datetime import datetime

app = Flask(__name__)

libros = ListaEnlazada()
usuarios = ListaEnlazada()
operaciones = ListaEnlazada()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/libros', methods=['GET', 'POST'])
def gestionar_libros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        genero = request.form['genero']
        id_libro = len(libros.listar()) + 1
        libros.agregar(Libro(id_libro, titulo, autor, genero))
        return redirect('/libros')
    return render_template('libros.html', libros=libros.listar())

@app.route('/usuarios', methods=['GET', 'POST'])
def gestionar_usuarios():
    if request.method == 'POST':
        nombre = request.form['nombre']
        id_usuario = len(usuarios.listar()) + 1
        usuarios.agregar(Usuario(id_usuario, nombre))
        return redirect('/usuarios')
    return render_template('usuarios.html', usuarios=usuarios.listar())

@app.route('/operaciones', methods=['GET', 'POST'])
def registrar_operacion():
    if request.method == 'POST':
        id_usuario = int(request.form['usuario'])
        id_libro = int(request.form['libro'])
        tipo = request.form['tipo']
        fecha = datetime.now()
        operaciones.agregar(Operacion(id_usuario, id_libro, tipo, fecha))
        return redirect('/operaciones')
    return render_template('operaciones.html',
                           usuarios=usuarios.listar(),
                           libros=libros.listar(),
                           operaciones=operaciones.listar())

@app.route('/recomendaciones')
def recomendaciones():
    recomendador = Recomendador('data/historial.csv')
    recomendador.entrenar()
    usuario_id = request.args.get('usuario')
    if usuario_id:
        resultado = recomendador.recomendar(int(usuario_id))
    else:
        resultado = []
    return render_template('recomendaciones.html',
                           recomendaciones=resultado,
                           usuarios=usuarios.listar())

if __name__ == '__main__':
    app.run(debug=True)
