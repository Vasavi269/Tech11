FROM python:3.9.5
RUN apt-get update -y
#make a directory for our application
WORKDIR /Project

RUN pip install flask
RUN pip install flask-cors
RUN pip install requests
RUN pip install flask_oidc

#copy the source code
COPY api.py .
COPY client_secrets.json .

CMD ["python", "api.py"]