./employee-api.py

curl -i http://localhost:5000/api/v1.0/employee

curl -i http://localhost:5000/api/v1.0/employee/2

curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Dan"}' http://localhost:5000/api/v1.0/employee

curl -i -H "Content-Type: application/json" -X PUT -d '{"title": "tester", "active": true}' http://localhost:5000/api/v1.0/employee/3

curl -i -X DELETE http://localhost:5000/api/v1.0/employee/2


Docker:
=======

docker image build -t flask-rest .

docker run -p 5001:5000 flask-rest

docker tag flask-rest eu.gcr.io/ssil1-258911/flask-rest:v1

docker push eu.gcr.io/ssil1-258911/flask-rest:v1

gcloud container clusters create --machine-type n1-standard-2 --num-nodes 2  --zone europe-west2-b --cluster-version latest test-cluster

kubectl create deployment flask-rest --image=eu.gcr.io/ssil1-258911/flask-rest:v1

kubectl expose deployment flask-rest --type LoadBalancer --port 5000 --target-port 5000

kubectl apply -f k8s-flask-rest.yml

kubectl get deployments

kubectl get services

kubectl delete -f k8s-flask-rest.yml