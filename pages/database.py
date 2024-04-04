from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Integer, String, Date
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

########################################
# TABLE CLASSES  -
########################################

from sqlalchemy import Integer, String

#one table for Spores, Agar, and LC
class Inventory(Base):
    __tablename__ = 'inventory'
    inv_id = SAColumn(Integer, primary_key=True)
    inv_batch = SAColumn(String)
    inv_name = SAColumn(String)
    inv_website = SAColumn(String)
    inv_quantity = SAColumn(Integer)
    inv_date = SAColumn(Date)

class Recipes(Base):
    __tablename__ = 'recipes'
    recipe_id = SAColumn(Integer, primary_key=True)
    recipe_batch = SAColumn(String)
    recipe_name = SAColumn(String)
    recipe_website = SAColumn(String)
    recipe_quantity = SAColumn(Integer)
    recipe_date = SAColumn(Date)

class Spores(Base):
    __tablename__ = 'spores'
    spore_id = SAColumn(Integer, primary_key=True)
    spore_name = SAColumn(String)
    spore_vendor= SAColumn(String)
    spore_website = SAColumn(String)
    spore_date = SAColumn(Date)

class Agar(Base):
    __tablename__ = 'agar'
    agar_id = SAColumn(Integer, primary_key=True)
    agar_batch = SAColumn(String)
    agar_name = SAColumn(String)
    agar_quantity = SAColumn(Integer)
    agar_date = SAColumn(Date)

#one table for grain and bulk spawn.
class Spawn(Base):
    __tablename__ = 'spawn'
    spawn_id = SAColumn(Integer, primary_key=True)
    spawn_batch = SAColumn(String)
    spawn_name = SAColumn(String)
    spawn_quantity = SAColumn(Integer)
    spawn_date = SAColumn(Date)

class Bulk(Base):
    __tablename__ = 'bulk'
    bulk_id = SAColumn(Integer, primary_key=True)
    bulk_batch = SAColumn(String)
    bulk_name = SAColumn(String)
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
