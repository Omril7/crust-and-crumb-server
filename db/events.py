from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
import datetime

from . import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False, default=datetime.date.today)

    items = relationship("EventItem", back_populates="event", cascade="all, delete-orphan")


class EventItem(Base):
    __tablename__ = "event_items"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)
    qty = Column(Integer, nullable=False)

    event = relationship("Event", back_populates="items")
    recipe = relationship("Recipe")
