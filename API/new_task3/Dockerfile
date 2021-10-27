FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
COPY /api.py .

RUN pip install flask
RUN pip install flask-cors
RUN pip install requests

ENTRYPOINT ["python"]
CMD ["api.py"]