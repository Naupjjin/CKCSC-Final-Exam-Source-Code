FROM alpine/socat

RUN apk add --no-cache python3 py3-pip


RUN mkdir -p /app
WORKDIR /app

COPY ./src /app/
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

EXPOSE 600001
ENTRYPOINT ["socat", "tcp-listen:20000,fork", "EXEC:'python3 server.py'"]