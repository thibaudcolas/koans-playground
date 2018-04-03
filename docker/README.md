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

See [`hello-world/`](hello-world/).

```sh
cd hello-world
# Build the image. giving it a name.
docker build -t hello-world .
```
