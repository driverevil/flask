import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# ------------------------------------------------------------------------------
# DATABASE SECTION
#-------------------------------------------------------------------------------

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ --> ruta absoluta de basic.py /home/user/etc..etc..

# Crear aplicacion
app = Flask(__name__)

# Conectar app con Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +os.path.join(basedir,'data.sqlite')

# Do not track modifications in Database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#-------------------------------------------------------------------------------
# DATABASE STRUCTURE
#-------------------------------------------------------------------------------
class DragonBall(db.Model):
    # Nombre de base de datos (opcional, por default toma el nombre de la class)
    #__tablename__ = 'Dragonball'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # String representation from the object
    def __repr__(self):
        return (f"{self.name} is a Dragon Ball character is {self.age} years old and its breed is {self.breed}")
    
