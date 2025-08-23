from sqlalchemy import Column, Integer, String, Date, Enum, Text
from sqlalchemy.orm import relationship
from datetime import date

from . import Base
from .enums import PickupPlace


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False, unique=True)
    pickup_place = Column(Enum(PickupPlace), nullable=False)
    joining_date = Column(Date, default=date.today, nullable=False)
    notes = Column(Text)

    orders = relationship("Order", back_populates="client")

    def __repr__(self):
        return f"<Client(name={self.name}, phone={self.phone})>"
