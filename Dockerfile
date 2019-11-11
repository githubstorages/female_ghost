FROM python:3.8.0
WORKDIR /usr/src/app
EXPOSE 8000


RUN apt-get update &&  \
    apt-get install vim -y

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
