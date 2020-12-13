# Demo app
 - python 3.7
 - Django 2.2
 - PostgreSQL 12
 - Postgis 3.0

### Run project in docker:
```sh
cp src/.env.templ src/.env
docker-compose up -d
```

### Run localy:
```sh
cp src/.env.templ src/.env
pip-sync requirements.txt dev-requirements.txt
cd src
./manage.py migrate
./manage.py createsuperuser
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


### TODO:
1. REST API
2. fixtures
3. Tests
4. Role based permissions
