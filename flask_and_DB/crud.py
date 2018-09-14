from basic import db, DragonBall
# Will be errors if you try to run this two times without delete prev DB
#-------------------------------------------------------------------------------
# Create
#-------------------------------------------------------------------------------
my_char = DragonBall('Bulma','35','Human')
db.session.add(my_char)
db.session.commit()

#-------------------------------------------------------------------------------
# Read
#-------------------------------------------------------------------------------
all_chars = DragonBall.query.all() # List all objects in the table!
print(all_chars)

#-------------------------------------------------------------------------------
# Select
#-------------------------------------------------------------------------------
# By ID
char_one = DragonBall.query.get(1)
print(char_one.name)
# Filters - Generate SQL quey code - Print a list
char_goku = DragonBall.query.filter_by(name='Goku')
print(char_goku.all())

#-------------------------------------------------------------------------------
# Update
#-------------------------------------------------------------------------------
first_char = DragonBall.query.get(1)
first_char.age = 28
db.session.add(first_char)
db.session.commit()

#-------------------------------------------------------------------------------
# Delete
#-------------------------------------------------------------------------------
second_char = DragonBall.query.get(2)
db.session.delete(second_char)
db.session.commit()

#-- See again changes
all_chars = DragonBall.query.all() # List all objects in the table!
print(all_chars)
