FROM python:3.10-buster

ENV DJANGO_SETTINGS_MODULE='fimeco_backend.settings.prod'
WORKDIR /app
COPY ./requirements.txt /app/
RUN python3 -m pip install -r requirements.txt 
COPY . /app/

EXPOSE 8002

CMD [ "gunicorn", "fimeco_backend.wsgi:app", "--bind 0.0.0.0", "--port 8001" ]