from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms.validators import InputRequired

class Quadraticform(FlaskForm):
    a = FloatField("a", validators=[InputRequired()])
    b = FloatField("b", validators=[InputRequired()])
    c = FloatField("c", validators=[InputRequired()])