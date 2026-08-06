from efms.database.database import Base
from efms.database.database import engine

from efms.database.models import *
from efms.database.operation_history import *

def initialize_database():

    Base.metadata.create_all(bind=engine)