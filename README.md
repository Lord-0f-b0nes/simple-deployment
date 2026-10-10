# DevOps pipeline Demo

a minimal flask-management API, containerized and deployed behind an Nginx reverse proxy with HTTPS, orchistrated via docker compose,and tested automatically through a GitHub actions CI pipeline.

This project's focus is the DevOps workflow.

## Stack 

Flask (python) - backend API
Docker + Docker compose - containerization And orchestration
Nginx reverse proxy, TLS termination
GitHub actions - CI pipeline

## What the API does

get /health - checking service avtivity 
get /tasks - lists all tasks 
post /tasks - add a new task 
get /tasks/<id> - search for one task
put /tasks/<id> - update task 

## Running in yourself (this project runs locally)

```bash
docker-compose up --build
```

then visit "https://yourlocalhost" - (self signed certification - browser warning expected)
 

