#-------------------------------------------------------------------------------
# CRUD Script - You can not use this script twice
#-------------------------------------------------------------------------------
from basic import db, DragonBall

#-------------------------------------------------------------------------------
# Setup fo DATABASE
#-------------------------------------------------------------------------------

db.create_all() # Create all the tables model --> Db Table

goku = DragonBall('Goku','150','Saiyajin')
kr = DragonBall('Krillin','40','Humano')

db.session.add_all([goku,kr]) # Adding
db.session.commit() # Escribir en base de datos
