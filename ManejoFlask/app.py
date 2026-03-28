from flask import Flask , render_template
from cliente_dao import ClienteDAO
from cliente import Cliente
from cliente_forma import ClienteForma
from flask import redirect, url_for

app=Flask(__name__)#Flask es una clase que se importa del módulo flask, esta clase se utiliza para crear una aplicación web, el argumento __name__ es el nombre del módulo actual, esto le dice a Flask dónde buscar los archivos estáticos y las plantillas.

app.config['SECRET_KEY']= 'llavesecreta123' #SECRET_KEY es una clave secreta que se utiliza para proteger los formularios de ataques CSRF (Cross-Site Request Forgery), esta clave debe ser única y secreta, se recomienda utilizar una cadena aleatoria de caracteres.
titulo_app = 'Zona Fit (GYM)'

@app.route('/') #url http://localhost:5000/
@app.route('/index.html') #url http://localhost:5000/index.html

def inicio():
  app.logger.debug('Se ha accedido a la ruta /') #logger es una herramienta de depuración que nos permite registrar mensajes en la consola, es el nivel debug es el más bajo, es decir, se registrarán todos los mensajes, incluyendo los de depuración.

# Recuperamos clientes en la BD
  clientes_db = ClienteDAO.seleccionar()

  # Creamos un objeto de cliente form vacio
  cliente = Cliente()
  cliente_forma = ClienteForma(obj=cliente)


  return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_forma) #render_template es una función que se importa del módulo flask, esta función se utiliza para renderizar una plantilla HTML, el argumento 'index.html' es el nombre de la plantilla que se va a renderizar, esta plantilla debe estar ubicada en la carpeta templates.

@app.route('/guardar', methods=['POST']) #url http://localhost:5000/guardar, el método POST se utiliza para enviar datos al servidor, en este caso, los datos del formulario.
def guardar():
  # Creamos los objetos de cliente
  cliente = Cliente()
  cliente_forma = ClienteForma(obj=cliente)
  if cliente_forma.validate_on_submit(): #validate_on_submit() es un método que se utiliza para validar el formulario, este método devuelve True si el formulario es válido, es decir, si todos los campos cumplen con las validaciones establecidas, en este caso, si todos los campos no están vacíos.
    cliente_forma.populate_obj(cliente) #populate_obj() es un método que se utiliza para llenar un objeto con los datos del formulario, en este caso, se llena el objeto cliente con los datos del formulario cliente_forma.

  if not cliente.id:
    ClienteDAO.insertar(cliente) #insertar() es un método que se utiliza para insertar un nuevo cliente en la base de datos, este método recibe como argumento el objeto cliente que se va a insertar.
  else:
    ClienteDAO.actualizar(cliente) 
  # redireccionamos al inicio
  return redirect(url_for('inicio')) #redirect() es una función que se importa del módulo flask, esta función se utiliza para redireccionar a otra ruta, en este caso, se redirecciona a la ruta inicio, url_for() es una función que se importa del módulo flask, esta función se utiliza para generar una URL para una función de vista, en este caso, se genera la URL para la función de vista inicio.

@app.route('/limpiar') 
def limpiar():
  return redirect(url_for('inicio'))

@app.route('/editar/<int:id>')
def editar(id):
  cliente = ClienteDAO.seleccionar_por_id(id)
  cliente_forma = ClienteForma(obj=cliente)
  clientes_db = ClienteDAO.seleccionar()
  return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_forma)

@app.route('/eliminar/<int:id>')
def eliminar(id):
  cliente = Cliente(id=id)
  ClienteDAO.eliminar(cliente)
  return redirect(url_for('inicio'))

if __name__ == '__main__':
  app.run(debug=True)