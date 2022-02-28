# devocean-django
SK 그룹사 정보를 기록할 수 있는 Django app입니다. DjangoREST + Bootstrap 으로 이루어져있습니다. Devocean 포스팅용 리포입니다.



## 처음 Setup 과정

1. requirements 설치
   1. `python -m pip install -r requirements.txt`
2. 프로젝트 시작
   1. `django-admin startproject settings`
   2. settings/ 에 있는 파일을 root에 옮겨줍니다. (ex. devocean-django/)
3. 앱 시작
   1. python manage.py startapp company



## Heroku 배포용 환경 설정파일 생성

1. runtime.txt
   1. python-3.8.11
   2. 어떤 Docker 이미지를 베이스로 생성할지 정해줍니다.
2. Procfile
   1. web: gunicorn settings.wsgi --log-file -
   2. gunicorn 을 이용해 앱을 시작합니다.
3. settings/settings.py 수정
   1. 주석을 지우고, STATIC_ROOT 선언을 해줍니다.
   2. DB NAME 경로를 수정해줍니다.
   3. ALLOWED_HOSTS = ["*"] 로 전부 접근 허용해줍니다.



## requirements 설명

1. django, djangorestframework
2. dj-database-url, psycopg2
   1. DB 라이브러리입니다. (postgresql)
3. gunicorn, whitenoise
   1. 서버 관련 라이브러리입니다. 

