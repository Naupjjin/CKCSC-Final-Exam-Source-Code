FROM alpine

RUN apk add --no-cache python3 py3-pip


RUN mkdir -p /app
WORKDIR /app

COPY ./src /app/
RUN pip3 install --upgrade pip && pip3 install -r requirement.txt

EXPOSE 50001
ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "-p", "50001"]