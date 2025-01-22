# base image  
FROM python:3.10
# setup environment variable  
ENV DockerHOME=/home/app/webapp  

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# Copy the current directory contents into the container
ADD . $DockerHOME

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
# install dependencies  
RUN pip install --upgrade pip

ADD ./requirements.txt $DockerHOME/requirements.txt

# copy whole project to your docker home directory. COPY . $DockerHOME  
# run this command to install all dependencies 
RUN pip install -r requirements.txt
# RUN python manage.py migrate

# #run this command to make migrations to new db changes
# RUN python manage.py migrate
# CMD ["python", "manage.py", "migrate"]

# port where the Django app runs  
EXPOSE 80  
# start server  
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
# CMD ["sh", "-c","python manage.py migrate && python manage.py runserver 0.0.0.0:80"]
