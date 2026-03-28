from flask import Flask

app=Flask(__name__)#Flask es una clase que se importa del módulo flask, esta clase se utiliza para crear una aplicación web, el argumento __name__ es el nombre del módulo actual, esto le dice a Flask dónde buscar los archivos estáticos y las plantillas.

@app.route('/') #url http://localhost:5000/
@app.route('/index.html') #url http://localhost:5000/index.html

def inicio():
  app.logger.debug('Se ha accedido a la ruta /') #logger es una herramienta de depuración que nos permite registrar mensajes en la consola, es el nivel debug es el más bajo, es decir, se registrarán todos los mensajes, incluyendo los de depuración.
  return 'Hola Mundo'

if __name__ == '__main__':
  app.run(debug=True)