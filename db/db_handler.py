from contextlib import contextmanager
from . import SessionLocal
from .client import Client
from .inventory import Inventory
from .recipe import Recipe, RecipeIngredient
from .order import Order, OrderItem


@contextmanager
def get_session():
    """Provide a transactional scope around a series of operations."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()


# -------- Example operations --------

def add_client(name, phone, pickup_place, notes=None):
    with get_session() as session:
        client = Client(name=name, phone=phone, pickup_place=pickup_place, notes=notes)
        session.add(client)
        session.flush()  # ensures ID is available before commit
        return client.id


def list_clients():
    with get_session() as session:
        return session.query(Client).all()


def add_inventory_item(ingredient, qty, unit, low_threshold=0):
    with get_session() as session:
        item = Inventory(ingredient=ingredient, qty=qty, unit=unit, low_threshold=low_threshold)
        session.add(item)
        session.flush()
        return item.id


def update_inventory_qty(ingredient_id, new_qty):
    with get_session() as session:
        item = session.query(Inventory).filter_by(id=ingredient_id).first()
        if not item:
            return None
        item.qty = new_qty
        return item.id


def add_order(client_id, items, pickup_date=None, note=None):
    """
    items = list of dicts like: [{ "recipe_id": 1, "qty": 2 }, ...]
    """
    with get_session() as session:
        order = Order(client_id=client_id, pickup_date=pickup_date, note=note)
        session.add(order)
        session.flush()

        for item in items:
            order_item = OrderItem(order_id=order.id, recipe_id=item["recipe_id"], qty=item["qty"])
            session.add(order_item)

        return order.id
