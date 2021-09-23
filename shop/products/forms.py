from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, validators, IntegerField, StringField
from wtforms.fields.simple import TextAreaField 


class Addproducts(Form):
    name = StringField("Name", [validators.DataRequired()])
    price = IntegerField("Price", [validators.DataRequired()])
    discount = IntegerField("Discount", [validators.DataRequired()])
    stock = IntegerField("Stock", [validators.DataRequired()])
    discription = TextAreaField("Discription", [validators.DataRequired()])
    colors = TextAreaField("Colors", [validators.DataRequired()])



    image_1 = FileRequired("Image_1", validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), 'image only please'])
    image_2 = FileRequired("Image_2", validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), 'image only please'])
    image_3 = FileRequired("Image_3", validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), 'image only please'])
