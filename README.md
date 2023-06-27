# likelion_study

멋사 백엔드 공부입니다  
주차 별로 브랜치 파서 올려놓았습니다 (4주차 이후부터는 계속 추가하는 과정이라 week4+ 브랜치에 계속 추가하였습니다.)  
_이동원 강사님 자료_: https://github.com/3chamchi/project-lion-backend-django

## 1주차 강의 복습 (Web 동작원리 - 클라이언트와 서버의 만남)

### 웹의 탄생

-   전세계를 연결해주는 것이 필요 -> 웹의 탄생

### 클라와 서버

-   클라이언트 -> 서버로 요청(request)
-   서버 -> 클라이언트로 응답(response)

### URL 분석 ( ex) https://www.google.com/search?q=techit)

-   https://
    -   프로토콜 (protocol)
        -   통신규칙
        -   http(https), ftp 등
-   www.google.com
    -   호스트 (host)
        -   서버의 주소
        -   google.com을 호스트 네임이라고 지칭
-   /search
    -   경로 (path)
        -   호스트 내 서비스의 위치
        -   서비스 별로 분할 ex) 검색, 회원 등
-   ?q=techit
    -   쿼리 문자열 (query string)
        -   ? 기호로 시작, & 로 연결
        -   키/값 쌍으로 구성

### 쿠키 & 세션

-   쿠키(cookie): 서버에서 클라이언트로 보내져서 브라우저에 저장되는 작은 데이터
    -   키/값 구조로 되어있고 유효기간 있음
    -   보안 문제가 있음 => 세션 저장소에 중요한 정보를 넣고 쿠키에는 세션 ID를 넣어서 보내줌 -> 클라이언트가 세션 저장소 참조하면서 정보 받아옴

### IP, Port, DNS

-   같은 네트워크 안에서 연결 해주는 것 -> 스위치
-   다른 네트워크 간에 통신 해주는 것 -> 라우터 = 공유기
-   IP(internet protocol): 컴퓨터 간 데이터를 주고받는 네트워크 계층의 규약 -> 데이터 전달에 필요한 목적지 컴퓨터 정보가 필요
-   IPv4, IPv6 -> ip 주소 형식
-   공인 IP, 사설 IP
    -   공인 IP: 전체 인터넷 망에서 고유하게 식별 가능한 주소 (IPv4로 표현하기엔 개수 부족)
    -   사설 IP: 가정의 LAN과 같은 네트워크에서 할당된 주소, 컴퓨터에서 조회되는 IP
    -   하나의 공인ip를 공유기에 주고 공유기가 구성하는 새로운 네트워크의 사설 ip를 할당함
-   127.0.0.1 (localhost): 자기 자신을 가리키는 ip
-   Port: 하나의 컴퓨터에서 실행되는 다양한 서비스를 구분하는 역할
    -   접근하려는 서비스의 목적지 포트를 정확하게 설정
-   DNS(Domain Name Server): url을 해석하여 ip 주소로 반환하는 서버
    -   국가, 기업 등이 운영, 전세계 DNS는 연결되어 있음, 장애 발생 시 큰일남

## 2주차 강의 복습 (DRF로 API 구현하기)

-   DRF(DjangoRestFramework): Django를 기반으로 REST API 서버를 만들기 위한 라이브러리
    -   Django는 자체적인 웹 템플릿에게 데이터를 전달해주고, DRF는 다양한 플랫폼의 클라이언트에게 데이터를 전달해준다는 주 목적에 차이가 있다
-   cors: 외부에서 도메인으로 불러올 수 있게 해주는 패키지
-   serializer: python에서 다뤄지는 객체를 http 통신에서 api로 활용할 수 있는 json 형식으로 변환해주는 것

## 3주차 강의 복습 (백엔드 개발 기초)

### ⦁ 장고 프로젝트 세팅 순서

1.  폴더 열기
2.  python -m venv venv -> 가상환경을 만듬
3.  .\venv\Scripts\activate -> 가상환경 시작
4.  pip install --upgrade pip -> pip 업데이트
5.  pip install django -> 장고 설치
6.  django-admin startproject [장고 프로젝트명] [위치|생략 가능] -> 프로젝트 생성 ex)django-admin startproject config . 권장
   - 폴더 안에서 프로젝트를 하나만 할거면 config .으로 해도 상관없지만 폴더 안에서 여러개 프로젝트를 진행할거면 startproject 플젝명 으로 해주기
8.  django-admin startapp [앱이름(복수형으로)] -> 어떠한 것에 관련된 기능을 수행하는 앱 생성 (여기서 앱이란 부품 같은 거다.)
9.  config에 settings.py 에 들어가서 installed_apps 리스트 안에 새로 만든 앱이름 **"콤마 붙여서"** 넣기

## 4주차 강의 복습 (DB 와 ORM)

-   보기 -> 명령팔레트(ctrl + shift + p) -> python select interpreter -> 경로가 .\venv\Scripts\python.exe 맞는지 확인하고 클릭
    => vs코드가 어떤 파이썬을 사용할지 지정해주기 위함 -> 장고 인식, 노란,빨간 지렁이 안 나오게 함, 디버깅 가능
-   models.py에 class를 만들어줌으로써 테이블을 만들 수 있음 -> 이때, class 안에 여러가지 속성(사용자, 이미지, 생성날짜 등)을 넣을 수 있는데 그에 맞는 필드를 선택해야함
    ex) content = models.TextField(verbose_name="내용")
    -   모델 필드 공식문서 : https://docs.djangoproject.com/en/4.0/ref/models/fields/
    -   모델 필드 유형 공식문서 : https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types
-   python manage.py shell 하면 interative python shell 켜짐
-   from posts.models import Post 후 Post.objects.create(~) 하면 db에 생성됨

## 5주차 강의 복습 (QuerySet Api 와 Admin)

-   query: db에 정보를 요청하는 것
-   queryset: db에서 전달 받은 객체의 목록
-   queryset api: db에 요청하기 위한 인터페이스
-   자주 쓰는 queryset api 함수
    -   새 queryset를 반환하는 매서드: filter(), exclude(), order_by(), select_related(), prefetch_related(), raw()
    -   querysets를 반환하지 않는 매서드: get(), create(), count(), first(), last()
    -   QuerySet API 공식문서 : https://docs.djangoproject.com/en/4.0/ref/models/querysets/
-   python manage.py shell에서 실습한 내용
    -   Post.objects.create(content="~") -> db에 내용 생성
    -   Post.objects.filter(content="aa") -> 전체에서 내용이 "aa" 와 똑같은 것만 가져옴 ('aa'를 포함한 내용은 아님)
    -   Post.objects.all() -> 테이블 내에 있는 내용들의 아이디를 리스트 형태로 가져옴(정확히 아이디만 가져오는건 아니고 <Post: Post object (1)> 이런 식으로)
    -   for post in Post.objects.all(): -> 테이블 내에 있는 모든 내용을 출력해줌
        print(post.content)
    -   Post.objects.order_by('-id') -> '-'를 붙이면 반대로 정렬해줌 (기본은 오름차순) => Post.objects.order_by('-created_at') -> 최신 게시물 순서로 정렬 가능
        -   주의: 출력할 때 반대로 정렬해서 출력하는거지 원래 테이블이 정렬되지는 않음
    -   first_post = Post.objects.first() -> 첫 번째 내용이 변수에 저장
    -   first_post = '수정한 글' -> first_post.save() -> 첫 번째 내용 수정됨 -> Post.objects.first().content 로 확인 가능
    -   Post.objects.update(content='일괄 업데이트') -> 모든 내용이 다 바뀜
-   admin (관리자 페이지)
    -   server 열고 url 끝에 /admin 붙이면 됨
    -   settings.py 밑으로 내려서 language code를 ko-kr로 고치면 한글로 가능
    -   admin.py 에 admin.site.register(models에 있는 클래스 이름) -> 관리자 페이지에 테이블 생김
    -   공식문서 : https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#modeladmin-options

## 6주차 강의 복습 (views 와 templates)

-   FBV: 함수 기반 views -> 일회성, 특수 목적이 있는 view에 적합
-   CBV: 클래스 기반 views -> 일반적인 생성, 조회, 수정, 삭제 등의 view에 적합
-   template 은 서버에서 실행
    -   template이나 앱이 많아질수록 app 안에다가 template을 관리하는 건 한계가 있으므로 최상위 파일 바로 아래에 templates 폴더 만들고 그 안에 앱 폴더를 만든 후 html 파일 만들기
    -   이때, settings.py 안에 templates 리스트에 dirs 부분에 BASE_DIR / 'templates' 를 넣음으로써 templates 경로를 바꿔줘야 함.
    -   app에 urls.py를 만들고 앱 관련된 url을 관리한 후 전체 urls.py 파일에서 include를 해줘야 함.
    -   render의 두번째 인자인 html 폴더를 찾는 순서가 같은 app 폴더 안에 있는 templates를 찾아보고 settings.py에서 설정한 경로로 찾아본다.
        -   그래서 어떤 건 a.html 그대로 쓰고 어떤 건 바깥 templates 하위 app폴더 명을 앞에 경로로 나타내고 씀 ex) view.html , posts/post_list.html 요런 식으로
    -   html에서 링크를 걸 때 templates 태그인 url을 쓴다면 {% url '' %} 이렇게 써야하는데 이때 ''안에 정해진 패턴을 그대로 쓰면 나중에 urlpattern 에서 패턴 바꾸면 다 바꿔야됨
        -   => 그래서 path('', 함수, name = '') 이런식으로 세번째 인자에 이름을 지어준다. 그리고 {% url '이름' %} 이렇게 쓰면 된다.
        -   ex) path(" ", 함수, name="post-list" ) -> {% url 'post-list' %}
        -   그런데 이때 다른 app인데 path의 이름이 같을 수 있다. -> namespace 사용으로 문제해결
        -   문제 해결 순서: app의 urls.py에서 app_name = "앱이름" -> include 할 때 두번째 인자로 namespace="앱이름" -> {% url '앱이름:이름' %}
        -   ex) {% url 'posts:post-list' %}
    -   template 상속: html의 구조 중 반복되는 부분들을 부모에서 자식 html이 받아옴
        - base.html을 만들고 그 안에 {% block title %}{% endblock %}, {% block content %}{% endblock %} 등을 쓴다.
        - 자식 html 최상단에 {% extends 'base.html' %}을 적는다.
        - 자식 html에서 {% block title %}제목{% endblock %}, {% block content %}내용(보통 태그들){% endblock %} 식으로 입력해주면 된다.
    -   static: 서비스를 제공해주는 측(서버)에서 제공하는 이미지, css 등을 담는 폴더
        - settings.py에서 STATIC_URL 밑에 STATICFILES_DIRS = [BASE_DIR / 'static'] 입력
        - static 폴더에서 불러오고 싶으면 {% load static %}을 html 위에 쓰고 link태그 안에 href="{% static 'css/..' %}" or img태그 안에 src="{% static 'image/..' %}" 로 쓰면 됨
        - 주의: 상속 받았다고 {% load static %}이 자식 html에도 전달되는 것은 아님. 자식 html에도 {% extends 'base.html' %} 밑에 {% load static %} 적어줘야 함
    -   template을 작성할 때 아직 데베에서 정보를 받아오지 않는다고 하면 그 정보에 해당하는 부분을 약식으로 확인해볼 필요가 있음
        - 이때 쓸 수 있는 것이 "http://via.placeholder.com/32x32"인데 img태그 src 안에 넣으면 제대로 나오는지 확인해볼 수 있도록 무료로 회색배경 사진을 제공해줌
        - <img src="http://via.placeholder.com/32x32" alt="이미지"> <- 이렇게 나옴
    -   template 필터
        - include -> templates 폴더 안에 반복되는 html을 넣을 폴더 하나를 만든 후 {% include '경로' %}를 부모 html에 넣으면 이 부분만 가져올 수 있다.
        - truncatechars:숫자 -> 글자수 제한을 두어서 그 제한을 넘으면 ...으로 보이게 함

## 7주차 강의 복습 (CRUD)

-
