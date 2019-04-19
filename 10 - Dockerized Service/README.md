## Creating a Docker container for your service

We will build a personalized docker container for our service that is based on the `continuumio/miniconda3/` base image. Below are the detailed steps.

### Install Docker

Follow the instructions here to install Docker on your local machine: 
* For Mac: https://docs.docker.com/install/
* For Windows: https://docs.docker.com/docker-for-windows/install/

### Build your Docker image

1) With Docker running, navigate to this folder (where your `Dockerfile` is located) in your terminal
2) Run `docker build . -t cs6220/docker-demo`
3) Check that your image was built sucessfully by running `docker images` and verifying that it is listed there

### Run your container

1) Start a container using that image, appropriately routing the required port to your localhost: `docker run -d -p 8080:8080 --name iris-classifier cs6220/docker-demo:latest`
2) Check that your container is running: `docker ps`

### Access your service

Using a browser, navigate to `localhost:8080/ui` to access the Swagger interface of your service.

### Stop your container

Once you're done, you can stop your container by running `docker stop CONTAINER_ID`. To retrieve the container_id, reference the output of `docker ps`.

### Miscellaneous commands

* Save Docker image: `docker save cs6220/docker-demo:latest > demo.tar`
* Load Docker image: `docker load < demo.tar`
