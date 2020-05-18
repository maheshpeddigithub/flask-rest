#!/usr/bin/python3
from flask import Flask, jsonify, abort, request, make_response, url_for

app = Flask(__name__, static_url_path = "")
    
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Employee Not found' } ), 404)

employees = [
    {
        'id': 1,
        'name': u'Tom',
        'title': u'developer', 
        'active': True
    },
    {
        'id': 2,
        'name': u'Jim',
        'title': u'manager', 
        'active': False
    }
]

def make_public_employee(employee):
    new_employee = {}
    for field in employee:
        if field == 'id':
            new_employee['uri'] = url_for('get_employee', employee_id = employee['id'], _external = True)
        else:
            new_employee[field] = employee[field]
    return new_employee
    
@app.route('/api/v1.0/employee', methods = ['GET'])
def get_employees():
    return jsonify(list(map(make_public_employee, employees)))

@app.route('/api/v1.0/employee/<int:employee_id>', methods = ['GET'])
def get_employee(employee_id):
    employee = list(filter(lambda t: t['id'] == employee_id, employees))
    if len(employee) == 0:
        abort(404)
    return jsonify(make_public_employee(employee[0]))

@app.route('/api/v1.0/employee', methods = ['POST'])
def create_employee():
    if not request.json or not 'name' in request.json:
        abort(400)
    employee = {
        'id': employees[-1]['id'] + 1,
        'name': request.json['name'],
        'title': request.json.get('title', "NOT_SET"),
        'active': False
    }
    employees.append(employee)
    return jsonify(make_public_employee(employee)), 201

@app.route('/api/v1.0/employee/<int:employee_id>', methods = ['PUT'])
def update_employee(employee_id):
    employee = list(filter(lambda t: t['id'] == employee_id, employees))
    if len(employee) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != str:
        abort(400)
    if 'title' in request.json and type(request.json['title']) is not str:
        abort(400)
    if 'active' in request.json and type(request.json['active']) is not bool:
        abort(400)
    employee[0]['name'] = request.json.get('name', employee[0]['name'])
    employee[0]['title'] = request.json.get('title', employee[0]['title'])
    employee[0]['active'] = request.json.get('active', employee[0]['active'])
    return jsonify(make_public_employee(employee[0]))
    
@app.route('/api/v1.0/employee/<int:employee_id>', methods = ['DELETE'])
def delete_employee(employee_id):
    employee = list(filter(lambda t: t['id'] == employee_id, employees))
    if len(employee) == 0:
        abort(404)
    employees.remove(employee[0])
    return jsonify( { 'employee-deleted': True } )
    
if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')