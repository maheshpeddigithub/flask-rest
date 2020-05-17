./employee-api.py

curl -i http://localhost:5000/api/v1.0/employee

curl -i http://localhost:5000/api/v1.0/employee/2

curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Dan"}' http://localhost:5000/api/v1.0/employee

curl -i -H "Content-Type: application/json" -X PUT -d '{"title": "tester", "active": true}' http://localhost:5000/api/v1.0/employee/3

curl -i -X DELETE http://localhost:5000/api/v1.0/employee/2