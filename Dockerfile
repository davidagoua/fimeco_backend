FROM python:3.10-buster

ENV DJANGO_SETTINGS_MODULE='fimeco_backend.settings.prod'
WORKDIR /app
COPY ./requirements.txt /app/
RUN python3 -m pip install -r requirements.txt 
COPY . /app/
RUN python3 manage.py collectstatic --noinput
EXPOSE 8002

CMD [ "gunicorn", "fimeco_backend.wsgi:application", "--bind 0.0.0.0:8002" ]