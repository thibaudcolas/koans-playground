# Docker Playground

## Vocabulary

> **Containerization**: the use of Linux containers to deploy applications.
> [Containers are not new, but their use for easily deploying applications is.](https://docs.docker.com/get-started/)
>
> **Image**: an executable package that includes everything needed to run an application – the code, a runtime, libraries, environment variables, and configuration files.
> **Image**: template to create a target container (snapshot)
> Images are defined using a Dockerfile
>
> **Container**: running instance of an image
> **Container**: a runtime instance of an image – what the image becomes in memory when executed (that is, an image with state, or a user process)
>
> **Dockerfile**: defines what goes on in the environment inside your container.
> Access to resources like networking interfaces and disk drives is virtualized inside this environment, which is isolated from the rest of your system, so you need to map ports to the outside world, and be specific about what files you want to “copy in” to that environment.
> However, after doing that, you can expect that the build of your app defined in this Dockerfile behaves exactly the same wherever it runs.
>
> **Repository**: a collection of images – sort of like a GitHub repository, except the code is already built.
>
> **Registry**: a collection of repositories.
>
> **Service**: defines how containers behave in production
> **Service**: really just “containers in production.” A service only runs one image, but it codifies the way that image runs—what ports it should use, how many replicas of the container should run so the service has the capacity it needs, and so on.

---

## [Learn Docker in 12 minutes 🐳](https://www.youtube.com/watch?v=YFl2mCHdv24)

> https://www.youtube.com/watch?v=YFl2mCHdv24

> Docker is a tool for running applications in an isolated environment

### Advantages

1.  Same environment everywhere
2.  Sandbox projects
3.  It just works – makes it easy to use any project

…without the overhead of a virtual machine

Workflow:

1.  Write Dockerfile
2.  Build an image from the Dockerfile
3.  Run the image to get containers

### Hello, World

Docker images hub: https://hub.docker.com/

Official PHP images: https://hub.docker.com/_/php/

See [`hello/`](hello/).

```sh
cd hello
# Build the image. giving it a name (and optionally a tag, name:tag)
docker build -t hello .

# Run the image, forwarding port 80 from the host to port 80 in the container
docker run -p 80:80 hello

# Go to the page, show the container's output.
open http://localhost/
```

### Volumes

Two types:

* Persist / share data between containers
* Share data between the host and container (mount local dir as volume)

```sh
# Same container, but this time mounting a volume – the src dir to the container’s /var/www/html.
# Note: needs the full path, not relative
docker run -p 80:80 -v "$(pwd)/src:/var/www/html" hello
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

## [Official “Get started with Docker”](https://docs.docker.com/get-started)

### Part 1, orientation

```sh
# Execute "hello-world" Docker image
docker run hello-world
# To generate this message, Docker took the following steps:
#  1. The Docker client contacted the Docker daemon.
#  2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
#     (amd64)
#  3. The Docker daemon created a new container from that image which runs the
#     executable that produces the output you are currently reading.
#  4. The Docker daemon streamed that output to the Docker client, which sent it
#     to your terminal.

# List Docker containers (running, all, all in quiet mode)
docker container ls
docker container ls --all
docker container ls -aq
```

### [Part 2, containers](https://docs.docker.com/get-started/part2/)

```sh
cd friendlyhello
# Build the image, giving it a name
docker build -t friendlyhello .

# Local docker image registry
docker image ls
# REPOSITORY                      TAG                 IMAGE ID            CREATED             SIZE
# friendlyhello                   latest              19e1cfe21ac5        6 seconds ago       150MB

# Run the app, mapping your machine’s port 4000 to the container’s published port 80 using -p:
docker run -p 4000:80 friendlyhello

# Run the app in the background (detached mode):
docker run -d -p 4000:80 friendlyhello

# Stop the container (using the right id from docker container ls)
docker container stop 1fa4ab2cf395
```

#### Share your image

```sh
# Log in to the Docker public registry on your local machine.
docker login
# Associates a local image with a repository on a registry.
# Associates the friendlyhello image with the thibaudcolas/get-started repository, currently as tag part2
docker tag friendlyhello thibaudcolas/get-started:part2
# Upload the tagged image to the repository.
docker push thibaudcolas/get-started:part2

# Now runnable from anywhere 🌈
docker run -p 4000:80 thibaudcolas/get-started:part2
```

### [Part 3, services](https://docs.docker.com/get-started/part3/)

> Scaling a service changes the number of container instances running that piece of software, assigning more computing resources to the service in the process.

```sh
cd getstartedlab
docker swarm init
# Swarm initialized: current node () is now a manager.

# Our single service stack is running 5 container instances of our deployed image on one host. Let’s investigate.
docker stack deploy -c docker-compose.yml getstartedlab

# Get the service ID for the one service in our application:
docker service ls

#  List the tasks for your service:
docker service ps getstartedlab_web

# Take down the app and the swarm.
docker stack rm getstartedlab
docker swarm leave --force
```

### [Part 4, swarms](https://docs.docker.com/get-started/part4/)

TODO, maybe later
