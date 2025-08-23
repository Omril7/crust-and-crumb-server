import enum


class PickupPlace(enum.Enum):
    STORE = "Store"
    HOME = "Home"
    LOCKER = "Locker"
    OTHER = "Other"


class Unit(enum.Enum):
    KG = "קג"
    GRAM = "גרם"
    LITER = "ליטר"
    ML = "מ\"ל"
    UNIT = "יחידה"
