# Django Demo App
 - Python 3.7
 - Django 2.2
 - PostgreSQL 12
 - Postgis 3.0
 - Pytest 6

### Run Demo:
```sh
./demo.sh
```

 - user with edit maps permissions:
    - username: map_editor
    - password: map_editor_password
 - user without edit maps permissions:
    - username: map_viewer
    - password: map_viewer_password
 - superuser:
    - username: admin
    - password: password

### Run project in docker:
```sh
cp src/.env.templ src/.env
docker-compose build
docker-compose up -d
docker-compose exec app python manage.py fake_db
docker-compose exec app python manage.py createsuperuser
```

### Run project locally:
```sh
cp src/.env.templ src/.env
pip-sync requirements.txt dev-requirements.txt
cd src
./manage.py migrate
./manage.py createsuperuser
./manage.py fake_db
./manage.py runserver
```

### Run tests:
```sh
cd src
pytes
```

### Enable S3 upload
1. Uncoment `#DEFAULT_FILE_STORAGE=storages.backends.s3boto3.S3Boto3Storage` in src/.env
2. Specify your AWS keys 
```sh 
#src/.env
AWS_ACCESS_KEY_ID={YOUR_AWS_ACCESS_KEY_ID}
AWS_SECRET_ACCESS_KEY={YOUR_AWS_SECRET_ACCESS_KEY}
AWS_STORAGE_BUCKET_NAME={YOUR_AWS_STORAGE_BUCKET_NAME}
```
3. Restart project

### Admin:
[localhost:8000/admin/](http://localhost:8000/admin/)
 - demo_user: admin
 - demo_password: password

### API:
#### Docs:
[localhost:8000/api/v1/docs/](http://localhost:8000/api/v1/docs/)

#### Employees:
[localhost:8000/api/v1/employees/](http://localhost:8000/api/v1/employees/)

#### Branches:
[localhost:8000/api/v1/branches/](http://localhost:8000/api/v1/branches/)

### Create new db dump:
```sh
docker-compose exec postgres pg_dump --user postgres --if-exists --clean demo_app | gzip -9  > db/db.sql.gz
```

