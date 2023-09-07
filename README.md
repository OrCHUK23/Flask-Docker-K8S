# Basic Flask Application

This is a basic Flask application that displays a greeting along with the pod name from which the server is responding.

## Prerequisites

Before you begin, ensure you have the following requirements in place:

- Docker installed on your system.
- Kubernetes cluster.

## Getting Started

Follow these steps to run the Flask application locally:

1. Clone this repository to your local machine:

`git clone https://github.com/OrCHUK23/Flask-Docker-K8S.git`
`cd Flask-Docker-K8S`

2. Build the Docker image for the Flask application:

`docker build -t my-flask-app .`

3. Run the Docker container:

`docker run -p 5000:5000 my-flask-app

## Kubernetes Deployment

1. Apply the Kubernetes deployment and service YAML files:

`kubectl apply -f app-deployment.yaml`

`kubectl apply -f app-service.yaml`

2. To access the application within the cluster, use the NodePort service. Get the NodePort by running:

`kubectl get svc my-flask-app-service`

- You can access the application using the NodePort on any of your cluster nodes.

## Accessing the Application

- Once the application is running, open a web browser and access the URL: http://localhost:5000 (if running locally).
