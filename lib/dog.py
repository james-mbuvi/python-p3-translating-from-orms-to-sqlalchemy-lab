from models import Dog

# def create_table(base, engine):
#     __tablename__ = 'dogs'

# dog.py

from models import Base

def create_table(Base, engine):
    Base.metadata.create_all(engine)
    # Debugging line
    print("Database file created:", engine.url.database)



def save(session, dog):
    session.add(dog)
    session.commit()

    pass

def get_all(session):
      return session.query(Dog).all()
    
    
       
pass

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()
    pass

def find_by_id(session, id):
    return session.query(Dog).get(id)
    pass

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()
    pass

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
    pass





