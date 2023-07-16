FROM python:3.11-slim-bullseye

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED 1
ENV STATIC_ROOT /static
ENV POETRY_VIRTUALENVS_CREATE=false

EXPOSE 8000
RUN echo deb http://deb.debian.org/debian bullseye contrib non-free > /etc/apt/sources.list.d/debian-contrib.list \
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

VOLUME /backend
WORKDIR /backend

ADD pyproject.toml ./

RUN pip install -U pip poetry && ls &&  poetry install --no-root --without dev

COPY ./backend/ .

RUN export SECRET_KEY=x DATABASE_URL=y\
    && python manage.py collectstatic --noinput

HEALTHCHECK CMD wget -q -O /dev/null http://localhost:8000/healthchecks/db/ ||  exit 1

CMD gunicorn --bind 0.0.0.0:8000 app.asgi:application -k uvicorn.workers.UvicornWorker
