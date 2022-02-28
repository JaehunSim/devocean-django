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

https://github.com/JaehunSim/devocean-django/tree/f630e7d5e4618cf2554648967a0345e24f67b723



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

https://github.com/JaehunSim/devocean-django/tree/d379d4bb908cf7fa8c6cabb1248d163171837aa2



## App 추가

settings/settings.py INSTALLED_APPS 에 사용할 앱을 추가합니다

1. company
2. rest_framework

https://github.com/JaehunSim/devocean-django/tree/8b628401b20c760bd75fa718a7fed8336d007a7e



## REST API Setup

1. company/models.py
   1. 모델을 정의해줍니다. DB와 연동되며, 엑셀의 column 부분을 정의해주는 것과 비슷합니다. 
2. company/serializers.py
   1. python과 DB가 원활히 연결될 수 있도록 명시해주는 부분입니다. rest_framework를 이용해서 쉽게 구현가능합니다.
3. company/views.py
   1. 로직을 처리해주는 부분입니다. REST API를 가볍게 구현할 수 있습니다.
4. settings/urls.py
   1. 어떤 url 경로로 접근할지 명시해주는 부분입니다. CompanyList, CompanyDetail 연결을 해줍니다.
5. settings/settings.py
   1. DB를 postgresql로 바꿔야 합니다. (기본DB인 sqlite3는 heroku에서 증발해버립니다..)
      1. db_database_url 설정도 해줍니다.
   2. css를 제대로 적용하기위해 whitenoise 미들웨어를 추가합니다.



Model을 만들었으면 DB에 연동을 해야합니다. Heroku에서 아래 명령어를 입력하면 됩니다.

1. Heroku console을 열고 

2. `heroku run bash` 을 입력합니다. bash 창에서 3,4번 진행합니다.

3. `python manage.py makemigrations`

4. `python manage.py migrate`

https://github.com/JaehunSim/devocean-django/tree/0aeb59f726bf02e3578120852cf4e7b4c318de6e



## 탐험해보기

https://devoceansk.herokuapp.com/api/company/

끝났습니다~

여기서 REST API 실험을 해볼 수 있습니다!

Heroku가 아니라면 `python manage.py runserver` 로 확인할 수 있습니다. 

이럴경우 기본 sqlite3 DB를 쓰면 되고, `127.0.0.1:8000` 으로 접근해보세요.



### 데이터 넣기

HTTP API를 이용해 데이터를 넣을 수 있습니다.

python requests 를 이용해 넣어보겠습니다.

```python
import requests

url = r"https://devoceansk.herokuapp.com/api/company/"
data = {"name": "SK하이닉스",
        "field": "반도체",
        "address": "경기도 이천시 부발읍 경충대로 2091",
        "latitude": 37.2497159,
        "longitude": 127.4825281,
        "total_employees": 22254,
        "revenue": 429978,
        "operating_income": 124103,
        "net_income": 96162}
requests.post(url, data=data)
```



## 결과

https://devoceansk.herokuapp.com/api/company/

https://devoceansk.herokuapp.com/api/company/1







## requirements 설명

1. django, djangorestframework
2. dj-database-url, psycopg2
   1. DB 라이브러리입니다. (postgresql)
3. gunicorn, whitenoise
   1. gunicorn: 서버 관련 라이브러리입니다. 
   2. whitenoise: static file 관련 라이브러러입니다.

