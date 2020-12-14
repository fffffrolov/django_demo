FROM python:3.7-slim-stretch

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED 1
ENV STATIC_ROOT /static

EXPOSE 8000
RUN echo deb http://deb.debian.org/debian stretch contrib non-free > /etc/apt/sources.list.d/debian-contrib.list \
    && apt-get update \
    && apt-get --no-install-recommends install -y \
      locales-all \
      wget \
      gettext \
      gdal-bin \
      libgdal-dev \
      git \
      build-essential \
      libxml2-dev \
      libxslt1-dev \
      libpq-dev \
      python3-gdal \
    && rm -rf /var/lib/apt/lists/*

VOLUME /src
WORKDIR /src

ADD *requirements.txt ./

ARG REQUIREMETNS=requirements.txt
RUN pip install pip-tools && ls &&  pip-sync $REQUIREMETNS

COPY ./src/ .

RUN python manage.py collectstatic --noinput

HEALTHCHECK CMD wget -q -O /dev/null http://localhost:8000/healthchecks/db/ ||  exit 1

CMD python manage.py migrate && uwsgi --master --http :8000 --module app.wsgi --harakiri 25
