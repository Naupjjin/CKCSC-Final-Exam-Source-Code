FROM python:3

WORKDIR /app

COPY app.py /app/app.py
COPY message /app/message
COPY flag.txt /app/flag.txt

RUN apt-get update  \
    && useradd -m ctf-player \
    && chown -R ctf-player /app

USER ctf-player

RUN pip install Flask

EXPOSE 50002

CMD ["python3", "app.py"]
