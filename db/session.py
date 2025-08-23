from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.consts import DATABASE_URL
from db.models import Base


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

