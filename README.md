# Django Demo App
 - Python 3.7
 - Django 2.2
 - PostgreSQL 12
 - Postgis 3.0

### Run Demo:
```sh
./demo.sh
```

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
demo_user: admin
demo_password: password

### API:
####docs:
[localhost:8000/api/v1/docs/](http://localhost:8000/api/v1/docs/)

#### Employees:
[localhost:8000/api/v1/employees/](http://localhost:8000/api/v1/employees/)

#### Branches:
[localhost:8000/api/v1/branches/](http://localhost:8000/api/v1/branches/)

### TODO:
1. Role based permissions
