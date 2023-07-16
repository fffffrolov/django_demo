#!/bin/bash
cp .env.templ .env \
  && docker-compose build \
  && docker-compose up -d \
  && sleep 6 \
  && python -mwebbrowser http://localhost:8000/api/v1/docs/ \
  && python -mwebbrowser http://localhost:8000/admin/
