from sqlalchemy import Column, Integer, String, Date, Enum, Float
from sqlalchemy.orm import relationship
from datetime import date

from . import Base
from .enums import Unit

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ingredient = Column(String(100), nullable=False, unique=True)
    last_update = Column(Date, default=date.today, nullable=False)
    low_threshold = Column(Float, nullable=False)
    qty = Column(Float, nullable=False)
    unit = Column(Enum(Unit), nullable=False)

    recipe_links = relationship("RecipeIngredient", back_populates="ingredient")

    def __repr__(self):
        return f"<Inventory(ingredient={self.ingredient}, qty={self.qty} {self.unit.value})>"
