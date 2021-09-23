from wtforms import Form, SubmitField,IntegerField,FloatField,StringField,TextAreaField, validators
from flask_wtf.file import FileField,FileRequired,FileAllowed

class Addproducts(Form):
    name = StringField("Name", [validators.DataRequired()])
    price = IntegerField("Price", [validators.DataRequired()])
    discount = IntegerField("Discount", [validators.DataRequired()])
    stock = IntegerField("Stock", [validators.DataRequired()])
    discription = TextAreaField("Discription", [validators.DataRequired()])
    colors = TextAreaField("Colors", [validators.DataRequired()])



    image_1 = FileField("Image_1", validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_2 = FileField("Image_2", validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_3 = FileField("Image_3", validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
