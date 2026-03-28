from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField ,IntegerField
from wtforms.validators import DataRequired

class ClienteForma(FlaskForm):
  nombre = StringField('Nombre', validators=[DataRequired()])
  apellido = StringField('Apellido', validators=[DataRequired()])
  membresia = IntegerField('Membresia', validators=[DataRequired()])
  guardar = SubmitField('Guardar')
  # El campo nombre es un campo de texto, el campo apellido es un campo de texto, el campo membresia es un campo de número entero, el campo guardar es un botón de submit. El validator DataRequired() se utiliza para validar que el campo no esté vacío.