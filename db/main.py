from db import Base, engine
from db.client import Client
from db.inventory import Inventory
from db.recipe import Recipe, RecipeIngredient
from db.order import Order, OrderItem

# create all tables
Base.metadata.create_all(bind=engine)
