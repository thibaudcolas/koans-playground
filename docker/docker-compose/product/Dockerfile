# https://hub.docker.com/_/python/

# Python image, 3-onbuild tag - automatically installs requirements on build.
FROM python:3-onbuild

# Copy current dir to where the onbuild image expects the code to be.
COPY . /usr/src/app

# Run a command, with arguments
CMD ["python", "api.py"]
