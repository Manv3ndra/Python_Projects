from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class RegisterForm(FlaskForm):
    email = StringField(label='Email Address')
    nft_collection = StringField(label='Collection Name')
    nft_name = StringField(label='Serial Number of NFT')
    stop_price = StringField(label='Cutoff Price')
    submit = SubmitField(label='SUBMIT')