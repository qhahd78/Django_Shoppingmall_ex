# Django_Shoppingmall 과제 예제


## 서버 실행법 
1) 가상환경 생성 & 실행 
- ```python -m venv [가상환경이름]```
- ```. venv/Scripts/activate```

2) ```pip install pillow ```

3) 모델 생성
- ```python manage.py makemigrations```
- ```python manage.py migrate``` 

4) 관리자 계정 생성
- ``` python manage.py create superuser``` (관리자 계정만 상품을 등록할 수 있습니다.)
