from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship

from . import Base
from .enums import Unit

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    selling_price = Column(Float, nullable=False)
    dough_weight = Column(Float, nullable=False)

    ingredients = relationship("RecipeIngredient", back_populates="recipe")
    order_items = relationship("OrderItem", back_populates="recipe")

    def __repr__(self):
        return f"<Recipe(name={self.name}, price={self.selling_price})>"


class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)
    ingredient_id = Column(Integer, ForeignKey("inventory.id"), nullable=False)

    unit = Column(Enum(Unit), nullable=False)
    weight = Column(Float, nullable=False)
    bakers_percent = Column(Float, nullable=True)

    recipe = relationship("Recipe", back_populates="ingredients")
    ingredient = relationship("Inventory", back_populates="recipe_links")

    def __repr__(self):
        return f"<RecipeIngredient(recipe_id={self.recipe_id}, ingredient_id={self.ingredient_id}, weight={self.weight}{self.unit.value})>"
