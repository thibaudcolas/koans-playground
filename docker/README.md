# Docker Playground

## [Learn Docker in 12 minutes 🐳](https://www.youtube.com/watch?v=YFl2mCHdv24)

> https://www.youtube.com/watch?v=YFl2mCHdv24

> Docker is a tool for running applications in an isolated environment

### Advantages

1.  Same environment everywhere
2.  Sandbox projects
3.  It just works – makes it easy to use any project

…without the overhead of a virtual machine

### Vocabulary

> Container: running instance of an image
>
> Image: template to create a target container (snapshot)
> Images are defined using a Dockerfile

Workflow:

1.  Write Dockerfile
2.  Build an image from the Dockerfile
3.  Run the image to get containers

### Hello, World

Docker images hub: https://hub.docker.com/

Official PHP images: https://hub.docker.com/_/php/

See [`hello-world/`](hello-world/).

```sh
cd hello-world
# Build the image. giving it a name (and optionally a tag, name:tag)
docker build -t hello-world .

# Run the image, forwarding port 80 from the host to port 80 in the container
docker run -p 80:80 hello-world

# Go to the page, show the container's output.
open http://localhost/
```

### Volumes

Two types:

*   Persist / share data between containers
*   Share data between the host and container (mount local dir as volume)

```sh
# Same container, but this time mounting a volume – the src dir to the container’s /var/www/html.
# Note: needs the full path, not relative
docker run -p 80:80 -v "$(pwd)/src:/var/www/html" hello-world
```

### Stopping containers

`Ctrl + C` …or when the container's main process stops. Do not run background processes.

---

## [Docker Compose in 12 Minutes](https://www.youtube.com/watch?v=Qw9zlE3t8Ko)

> An image is a template for the environment you want to run.

Run an image -> get a container.

> Docker compose: lets us define all our services in a configuration file, spin up all the containers with one command.

`docker-compose.yml`: the stuff we would have specified in the `docker run` command.

```sh
# Build and run all the containers defined in the docker-compose.yml file.
docker-compose up

# Product service
open http://localhost:5001/
# Website
open http://localhost:5000/
```

Docker-compose creates a virtual network for all of the containers, where the container hostname matches the service name.

```sh
# Detached mode.
docker-compose up -d

# See running containers.
docker ps

$ docker ps
CONTAINER ID        IMAGE                           COMMAND                  CREATED              STATUS              PORTS                                            NAMES
61d7f20c403e        php:apache                      "docker-php-entrypoi…"   About a minute ago   Up 14 seconds       0.0.0.0:5000->80/tcp                             dockercompose_website_1
2788f427d122        dockercompose_product-service   "python api.py"          44 minutes ago       Up 15 seconds       0.0.0.0:5001->80/tcp                             dockercompose_product-service_1

# Stop detached containers.
docker-compose stop
```
