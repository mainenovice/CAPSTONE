from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Integer, String, Date,ForeignKey
from sqlalchemy import Column as SAColumn
# Define the base class
Base = declarative_base()

class CRUD:
    def __init__(self):
        self.url='sqlite:///capstone.db'
        # Create an engine
        self.engine = create_engine(self.url)
        # Bind the engine to the metadata of the base class so that the
        # declaratives can be accessed through a DBSession instance
        Base.metadata.bind = self.engine
        Base.metadata.create_all(self.engine)
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()

    def create(self, obj):
        self.session.add(obj)
        self.session.commit()

    def read(self, model, **kwargs):
        return self.session.query(model).filter_by(**kwargs).all()

    def update(self, obj, **kwargs):
        for key, value in kwargs.items():
            setattr(obj, key, value)
        self.session.commit()

    def delete(self, obj):
        self.session.delete(obj)
        self.session.commit()
    def fetch_for_dropdown(self, model, text_column, value_column):
        records = self.session.query(model).all()
        options = [
            {"text": getattr(record, text_column), "value": str(getattr(record, value_column))}
            for record in records
        ]
        return options

########################################
# TABLE CLASSES  -

# ALL Quantities measured in metric units when possible.
########################################

from sqlalchemy import Integer, String

#one table for Spores, Agar, and LC
class InvTable(Base):
    __tablename__ = 'inventory'
    inv_batch = SAColumn(String, primary_key=True)
    inv_name = SAColumn(String)
    inv_vendor = SAColumn(String)
    inv_website = SAColumn(String)
    inv_quantity = SAColumn(Integer)
    inv_units= SAColumn(String)
    inv_date = SAColumn(Date)

## I would like the recipe
class Recipes(Base):
    __tablename__ = 'recipes'
    rec_id = SAColumn(Integer, primary_key=True)
    rec_name = SAColumn(String)
    rec_website = SAColumn(String)
    rec_quantity = SAColumn(Integer,ForeignKey('inventory.inv_quantity'))
    rec_date = SAColumn(Date)

class Spores(Base):
    __tablename__ = 'spores'
    spore_batch = SAColumn(Integer, primary_key=True)
    spore_name = SAColumn(String)
    spore_vendor= SAColumn(String)
    spore_website = SAColumn(String)
    spore_date = SAColumn(Date)

class AgarTable(Base):
    __tablename__ = 'agartable'
    aga_batch = SAColumn(String, primary_key=True)
    aga_recipe= SAColumn(String,ForeignKey('recipes.rec_id'))
    aga_name = SAColumn(String,ForeignKey('spores.spore_name'))
    aga_notes = SAColumn(String)
    aga_date = SAColumn(Date)
class LiquidTable(Base):
    __tablename__ = 'liquidtable'
    liqui_batch = SAColumn(String, primary_key=True)
    liqui_recipe = SAColumn(String, ForeignKey('agartable.aga_batch'))
    liqui_name = SAColumn(String, ForeignKey('agartable.aga_name'))
    liqui_notes = SAColumn(String)
    liqui_date = SAColumn(Date)

#one table for grain and bulk spawn.
class GrainTable(Base):
    __tablename__ = 'graintable'
    gra_batchid = SAColumn(String, primary_key=True)
    gra_name = SAColumn(String, ForeignKey('agartable.aga_name'))
    gra_inventory_batch= SAColumn(String, ForeignKey('inventory.inv_batch'))
    gra_parent_culture = SAColumn(String,ForeignKey('liquidtable.liqui_name'))
    gra_quantity= SAColumn(Integer)
    gra_unit= SAColumn(String)
    gra_date = SAColumn(Date)

class Bulk(Base):
    __tablename__ = 'bulk'
    bulk_batch = SAColumn(String,primary_key=True)
    bulk_name = SAColumn(String,ForeignKey('graintable.gra_name'))
    #bulk_
    bulk_quantity = SAColumn(Integer)
    bulk_date = SAColumn(Date)

class Fruit(Base):
    __tablename__ = 'fruit'
    fruit_id = SAColumn(Integer, primary_key=True)
    fruit_batch = SAColumn(String)
    fruit_name = SAColumn(String)
    fruit_quantity = SAColumn(Integer)
    fruit_date = SAColumn(Date)




###### TESTING ######

#db_url = 'sqlite:///yourdatabase.db'
#self.crud = CRUD()

# Creating a new user
#new_user = User(name='John Doe', email='john@example.com')
#crud.create(new_user)

# Reading users
#users = crud.read(User, name='John Doe')

# Updating a user
#user = users[0]
#crud.update(user, email='newemail@example.com')

# Deleting a user
#crud.delete(user)
