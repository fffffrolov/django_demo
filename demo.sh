#!/bin/bash
cp ./src/.env.templ ./src/.env \
  && docker-compose build \
  && docker-compose up -d \
  && sleep 5 \
  && python -mwebbrowser http://localhost:8000/api/v1/docs/ \
  && python -mwebbrowser http://localhost:8000/admin/
