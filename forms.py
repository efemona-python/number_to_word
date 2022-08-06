from datetime import datetime
from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, URL, Email, Length, InputRequired, ValidationError
from wtforms.widgets import PasswordInput


##WTForm
class ConvertNumber(FlaskForm):
    number = StringField("Number", validators=[DataRequired()])
    submit = SubmitField("Convert")
    symbol_map = {"$": '',
                  "%": '',
                  "-": "0",
                  ",": '',
                  " ": ""
                  }

    def validate_number(self, number):
        number = self.format_func(number.data)
        try:
            int(number) or float(number)
        except ValueError:
            raise ValidationError('Invalid Number')


    def format_func(self, value):
        for symbol in self.symbol_map.keys():
            if symbol in value:
                value = value.replace(symbol, self.symbol_map[symbol])
                self.format_func(value)
        return value
