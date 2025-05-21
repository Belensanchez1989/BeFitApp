from flask import Flask, render_template, url_for, redirect
from cliente import Cliente
from cliente_dao import ClienteDAO
from cliente_forma import ClienteForma

app = Flask(__name__)

app.config['SECRET_KEY'] = ''

titulo_app = 'Be Fit!'


@app.route('/')  # url: http://localhost:5000/
@app.route('/index.html')  # url: http://localhost:5000/index.html
def inicio():
    app.logger.debug('Entramos al path de inicio/')
    # recuperamos los clientes de la bbdd
    personas_db = ClienteDAO.seleccionar()
    # Creamos un objeto de cliente form vacío
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    return render_template('index.html', titulo=titulo_app, clientes=personas_db,
                           forma=cliente_forma)


@app.route('/guardar', methods=['POST'])
def guardar():
    # creamos los objetos de clientes inicialmente objetos vacios
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    if cliente_forma.validate_on_submit():
        # llenamos el objeto cliente con los valores del formulario
        cliente_forma.populate_obj(cliente)  # tambien se recupera el id oculto del pformulario
        if not cliente.id:
        # guardamos el nuevo cliente en la bbdd
             ClienteDAO.insertar(cliente)
        else:
             ClienteDAO.actualizar(cliente)
        # Redireccionar a la pag de inicio
        return redirect(url_for('inicio'))

    return redirect(url_for('inicio'))


@app.route('/limpiar')
def limpiar():
    return redirect(url_for('inicio'))


@app.route('/editar/<int:id>')  # localhost:5000/editar/1
def editar(id):
    cliente = ClienteDAO.seleccionar_por_id(id)
    cliente_forma = ClienteForma(obj=cliente)
    # Recuperar el listado de clientes para volver a mostrarlo en la plantilla
    clientes_db = ClienteDAO.seleccionar()
    return render_template('index.html', titulo=titulo_app,
                           clientes=clientes_db, forma=cliente_forma)

@app.route('/eliminar/<int:id>') #localhost:500/eliminar/1
def eliminar(id):
    cliente = Cliente(id=id)
    ClienteDAO.eliminar(cliente)
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)
