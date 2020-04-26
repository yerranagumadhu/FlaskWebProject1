FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python3-pip  python3-dev python3-virtualenv
  

WORKDIR /app

COPY . /app

RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 3978

ENTRYPOINT  ["python3"]
CMD ["runserver.py"]
