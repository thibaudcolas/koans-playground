# Docker Playground

## Learn Docker in 12 minutes 🐳

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
