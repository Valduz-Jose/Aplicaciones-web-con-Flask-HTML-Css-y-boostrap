from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField ,IntegerField, HiddenField
from wtforms.validators import DataRequired

class ClienteForma(FlaskForm):
  id = HiddenField('Id') #Campo oculto para almacenar el id del cliente, este campo no se muestra en el formulario, pero se utiliza para almacenar el id del cliente que se va a editar.
  nombre = StringField('Nombre', validators=[DataRequired()])
  apellido = StringField('Apellido', validators=[DataRequired()])
  membresia = IntegerField('Membresia', validators=[DataRequired()])
  guardar = SubmitField('Guardar')
  # El campo nombre es un campo de texto, el campo apellido es un campo de texto, el campo membresia es un campo de número entero, el campo guardar es un botón de submit. El validator DataRequired() se utiliza para validar que el campo no esté vacío.