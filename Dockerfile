FROM python:3.9-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev build-base linux-headers pcre-dev nginx

RUN mkdir /app
WORKDIR /app
COPY conf/uwsgi.ini /app
COPY conf/uwsgi_params /app
RUN rm -Rf /etc/nginx/conf.d/default.conf
COPY conf/nginx.conf /etc/nginx
COPY conf/nginx-app.conf /etc/nginx/sites-enabled/app.conf

ADD docker .
ADD requirements.txt .
RUN pip install -r /app/requirements.txt
RUN python manage.py collectstatic --clear --traceback --noinput;

CMD python /app/manage.py createcachetable & \
    python /app/manage.py migrate & \
    uwsgi --ini /app/uwsgi.ini & \
    nginx