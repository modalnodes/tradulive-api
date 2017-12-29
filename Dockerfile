FROM python:2.7

# Copy in your requirements file
ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt
# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
RUN mkdir /code/
WORKDIR /code/
ADD . /code/

EXPOSE 80


CMD ["python","manage.py","migrate"]

CMD ["python","manage.py","runserver","0.0.0.0:80"]


