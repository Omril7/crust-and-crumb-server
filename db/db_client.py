from db.models import Expense, ExpenseType, Salary
from db.session import Session


class DBClient:
    @staticmethod
    def create_expense(data):
        with Session.begin() as session:
            expense = Expense(
                type=ExpenseType(data['type']),
                startDate=data['startDate'],
                endDate=data['endDate'],
                visaDate=data['visaDate'],
                currentCall=data['currentCall'],
                amount=data['amount'],
                payMethod=data['payMethod']
            )
            session.add(expense)
            session.flush()  # ensures expense.id is populated
            return expense.id

    @staticmethod
    def get_expenses():
        with Session.begin() as session:
            expenses = session.query(Expense).all()
            return [
                {
                    'id': e.id,
                    'type': e.type.value,
                    'startDate': str(e.startDate),
                    'endDate': str(e.endDate),
                    'visaDate': str(e.visaDate),
                    'currentCall': e.currentCall,
                    'amount': e.amount,
                    'payMethod': e.payMethod
                } for e in expenses
            ]

    @staticmethod
    def update_expense(expense_id, data):
        with Session.begin() as session:
            expense = session.query(Expense).get(expense_id)
            if not expense:
                return False
            for key, value in data.items():
                if key == 'type':
                    setattr(expense, key, ExpenseType(value))
                else:
                    setattr(expense, key, value)
            return True

    @staticmethod
    def delete_expense(expense_id):
        with Session.begin() as session:
            expense = session.query(Expense).get(expense_id)
            if not expense:
                return False
            session.delete(expense)
            return True

    @staticmethod
    def create_salary(data):
        with Session.begin() as session:
            salary = Salary(**data)
            session.add(salary)
            session.flush()
            return salary.id

    @staticmethod
    def get_salaries():
        with Session.begin() as session:
            salaries = session.query(Salary).all()
            return [
                {
                    'id': s.id,
                    'yearMonth': s.yearMonth,
                    'total': s.total,
                    'masHacknasa': s.masHacknasa,
                    'bituahLeumi': s.bituahLeumi,
                    'masBriut': s.masBriut,
                    'tagmulimOved': s.tagmulimOved,
                    'tagmulimMaasik': s.tagmulimMaasik,
                    'pitzuimMaasik': s.pitzuimMaasik,
                    'differences': s.differences,
                    'neto': s.neto,
                    'netoInAction': s.netoInAction,
                    'paycheckDate': str(s.paycheckDate),
                    'vacationDays': s.vacationDays,
                    'sicknessDays': s.sicknessDays
                } for s in salaries
            ]

    @staticmethod
    def update_salary(salary_id, data):
        with Session.begin() as session:
            salary = session.query(Salary).get(salary_id)
            if not salary:
                return False
            for key, value in data.items():
                setattr(salary, key, value)
            return True

    @staticmethod
    def delete_salary(salary_id):
        with Session.begin() as session:
            salary = session.query(Salary).get(salary_id)
            if not salary:
                return False
            session.delete(salary)
            return True

    @staticmethod
    def create_expenses_bulk(expenses_data):
        with Session.begin() as session:
            expenses = [
                Expense(
                    type=ExpenseType(data['type']),
                    startDate=data['startDate'],
                    endDate=data['endDate'],
                    visaDate=data['visaDate'],
                    currentCall=data['currentCall'],
                    amount=data['amount'],
                    payMethod=data['payMethod']
                )
                for data in expenses_data
            ]
            session.add_all(expenses)
            session.flush()
            return [expense.id for expense in expenses]

    @staticmethod
    def create_salaries_bulk(salaries_data):
        with Session.begin() as session:
            salaries = [
                Salary(**data)
                for data in salaries_data
            ]
            session.add_all(salaries)
            session.flush()
            return [salary.id for salary in salaries]
