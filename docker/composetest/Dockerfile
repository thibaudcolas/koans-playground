# Build an image starting with the Python 3.4 image.
FROM python:3.4-alpine
# Add the current directory . into the path /code in the image.
ADD . /code
# Set the working directory to /code.
WORKDIR /code
# Install the Python dependencies.
RUN pip install -r requirements.txt
# Set the default command for the container to python app.py.
CMD ["python", "app.py"]
