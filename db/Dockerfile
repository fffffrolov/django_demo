FROM postgis/postgis:12-3.0-alpine

ADD db/db.sql.gz /docker-entrypoint-initdb.d/

CMD ["postgres"]
