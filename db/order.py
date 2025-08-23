from sqlalchemy import Column, Integer, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import date

from . import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    order_date = Column(Date, default=date.today, nullable=False)
    pickup_date = Column(Date, nullable=True)
    note = Column(Text)

    client = relationship("Client", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")

    @hybrid_property
    def total(self):
        return sum(item.qty * item.recipe.selling_price for item in self.items)

    def __repr__(self):
        return f"<Order(id={self.id}, client_id={self.client_id}, total={self.total})>"


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)
    qty = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="items")
    recipe = relationship("Recipe", back_populates="order_items")

    def __repr__(self):
        return f"<OrderItem(order_id={self.order_id}, recipe_id={self.recipe_id}, qty={self.qty})>"
