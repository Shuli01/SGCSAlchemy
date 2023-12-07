from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#DB_URL = "mysql+pymysql://adminsgc:C0c41n4@localhost/sgc"
#engine = create_engine(DB_URL)


Base = declarative_base()

class Producto(Base):
    __tablename__ = "productos"

    id = Column("id", Integer, primary_key=True)
    nombre = Column("nombre", String)
    tipo = Column("tipo", String)
    cuantos = Column("cuantos", Integer)

    def __init__(self, id, nombre, tipo, cuantos):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.cuantos = cuantos

    def __repr__(self):
        return f"({self.id}) {self.nombre} {self.tipo} ({self.cuantos})"
    
class Proovedores(Base):
    __tablename__ = "proovedor"

    id = Column("id", Integer, primary_key=True)
    nombre = Column("nombre", String)
    ubicacion = Column("ubicacion", String)
    clasificacion = Column("clasificacion", String)

    def __init__(self, id, nombre, ubicacion, clasificacion):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.clasificacion = clasificacion

    def __repr__(self):
        return f"({self.id}) {self.nombre} {self.ubicacion} ({self.clasificacion})"
    
class Distribuidores(Base):
    __tablename__ = "Distribudor"

    id = Column("id", Integer, primary_key=True)
    nombre = Column("nombre", String)
    ubicacion = Column("ubicacion", String)
    clasificacion = Column("clasificacion", String)

    def __init__(self, id, nombre, ubicacion, clasificacion):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.clasificacion = clasificacion

    def __repr__(self):
        return f"({self.id}) {self.nombre} {self.ubicacion} ({self.clasificacion})"

engine = create_engine("sqlite:///mydb.db", echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
session.commit()

producto1 = Producto(100, "Coca","polvo", 500)
proovedor1 = Proovedores(500, "Chapo", "CO", "A")
distrubuidor1 = Distribuidores(1, "Escobar", "MX", "C")

session.add(producto1)
session.add(distrubuidor1)
session.add(proovedor1)
session.commit()

results = session.query(Producto).all()
results = session.query(Proovedores).all()
results = session.query(Distribuidores).all()

print(results)
session.close()