from flask import Flask , render_template
from cliente_dao import ClienteDAO
from cliente import Cliente
from cliente_forma import ClienteForma

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

if __name__ == '__main__':
  app.run(debug=True)