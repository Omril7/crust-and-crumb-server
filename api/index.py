from flask import Flask, request, jsonify
from flask_cors import CORS

from api.consts import ERROR_REDIRECT_HTML
from db.db_client import DBClient

app = Flask(__name__)
origins = ["http://localhost:3000", "https://crust-and-crumb.vercel.app", "https://omri-site.vercel.app"]
CORS(app, origins=origins)

db = DBClient()


@app.route('/')
def home():
    return ERROR_REDIRECT_HTML


@app.route('/expenses', methods=['POST'])
def create_expense():
    expense_id = db.create_expense(request.json)
    return jsonify({'message': 'Expense created', 'id': expense_id}), 201


@app.route('/expenses', methods=['GET'])
def get_expenses():
    return jsonify(db.get_expenses())


@app.route('/expenses/<int:expense_id>', methods=['PUT'])
def update_expense(expense_id):
    success = db.update_expense(expense_id, request.json)
    if not success:
        return jsonify({'error': 'Expense not found'}), 404
    return jsonify({'message': 'Expense updated'})


@app.route('/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    success = db.delete_expense(expense_id)
    if not success:
        return jsonify({'error': 'Expense not found'}), 404
    return jsonify({'message': 'Expense deleted'})


@app.route('/expenses/bulk', methods=['POST'])
def create_expenses_bulk():
    ids = db.create_expenses_bulk(request.json)
    return jsonify({'message': 'Expenses created', 'ids': ids}), 201


@app.route('/salaries', methods=['POST'])
def create_salary():
    salary_id = db.create_salary(request.json)
    return jsonify({'message': 'Salary created', 'id': salary_id}), 201


@app.route('/salaries', methods=['GET'])
def get_salaries():
    return jsonify(db.get_salaries())


@app.route('/salaries/<int:salary_id>', methods=['PUT'])
def update_salary(salary_id):
    success = db.update_salary(salary_id, request.json)
    if not success:
        return jsonify({'error': 'Salary not found'}), 404
    return jsonify({'message': 'Salary updated'})


@app.route('/salaries/<int:salary_id>', methods=['DELETE'])
def delete_salary(salary_id):
    success = db.delete_salary(salary_id)
    if not success:
        return jsonify({'error': 'Salary not found'}), 404
    return jsonify({'message': 'Salary deleted'})


@app.route('/salaries/bulk', methods=['POST'])
def create_salaries_bulk():
    ids = db.create_salaries_bulk(request.json)
    return jsonify({'message': 'Salaries created', 'ids': ids}), 201
