FROM ubuntu:20.04

LABEL maintainer="j.romero11@uniandes.edu.co"
LABEL version="1.0"
LABEL description="Docker image for the surfi project"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && apt dist-upgrade -y && apt install -y python python3 python3-pip git nano vim
RUN mkdir "/home/surfi-services"
ADD store /home/surfi-services/store
ADD SurfiBack /home/surfi-services/SurfiBack
ADD users /home/surfi-services/users
ADD manage.py /home/surfi-services/manage.py
ADD requirements.txt /home/surfi-services/requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8000

ENTRYPOINT python3 /home/surfi-services/manage.py runserver