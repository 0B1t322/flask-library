from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    submit = SubmitField('Add')