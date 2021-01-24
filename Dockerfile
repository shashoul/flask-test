FROM ubuntu

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install python3 -y 

RUN apt-get install python3-pip -y

RUN pip3 install -r requirements

ENTRYPOINT [ "python3" ]

CMD [ "test1.py" ]