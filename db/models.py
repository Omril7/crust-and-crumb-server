from sqlalchemy import Column, Integer, String, Float, Date, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()


class ExpenseType(enum.Enum):
    INTERNET = "אינטרנט"
    ARNONA = "ארנונה"
    GAS = "גז"
    VAAD_BAIT = "ועד בית"
    ELECTRICITY = "חשמל"
    WATER = "מים"
    RENT = "שכר דירה"


class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    type = Column(Enum(ExpenseType), nullable=False)
    startDate = Column(Date)
    endDate = Column(Date)
    visaDate = Column(Date)
    currentCall = Column(String)
    amount = Column(Float)
    payMethod = Column(String)


class Salary(Base):
    __tablename__ = 'salaries'
    id = Column(Integer, primary_key=True)
    yearMonth = Column(String)
    total = Column(Float)
    masHacknasa = Column(Float)
    bituahLeumi = Column(Float)
    masBriut = Column(Float)
    tagmulimOved = Column(Float)
    tagmulimMaasik = Column(Float)
    pitzuimMaasik = Column(Float)
    differences = Column(Float)
    neto = Column(Float)
    netoInAction = Column(Float)
    paycheckDate = Column(Date)
    vacationDays = Column(Float)
    sicknessDays = Column(Float)

    pdf_url = Column(String)
