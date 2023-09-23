![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=300&section=header&text=2023년%20동국대학교%20봄%20축제%20사이트&fontSize=60&animation=fadeIn&fontAlignY=38&desc=다시%20봄&descAlignY=58&descAlign=62)

## 🌠  About 다시 봄
> 2023년 동국대학교 봄 축제, <백상대동제 : 다시, 봄> <br>
> 축제를 더욱 재밌게 즐길 수 있는 축제 사이트! <br>


공연, 부스 정보부터 부스 위치 확인까지 <br>
축제에 관한 모든 공지와 정보를 확인하고 더욱 재밌는 축제를 즐겨보세요! <br><br>


## 👋 About Backend Developer

#### Backend Developer💻(Alphabet Order)
| Name                                         | Major            | Email                |
| -------------------------------------------- | --------------  | ----------------------- |
| [김재니](https://github.com/kmjenny)   | 동국대학교 정보통신공학과  | kjn3008@dgu.ac.kr |
| [박상준](https://github.com/tkdwns414) | 동국대학교 정보통신공학과   | sangjune2000@dgu.ac.kr |
| [박영신](https://github.com/dudtlstm) | 동국대학교 컴퓨터공학전공    | 2022110233@dgu.ac.kr |
| [안유성](https://github.com/ustar1210) | 동국대학교 전자전기공학부    | ustar1210@dgu.ac.kr |




## 🛠️ Tech
Django(DRF)

## How To Use?
#### Create and open your venv
```
python -m venv {가상 환경 이름}

-mac
source venv/bin/activate

-windows
source venv/Scripts/activate
```


#### pip install(라이브러리 설치)
```
pip install -r requirements.txt
-> git pull 후 실행
```

#### Add Library(자신이 설치한 라이브러리 추가)
```
pip freeze > requirements.txt
-> 설치한 라이브러리 있으면 실행
```

#### 서버 실행
```
python manage.py runserver
```

## 💻 Folder

```
📂 2023_spring_festival_back     #  repo root
┣  .gitignore
┣  README.md
┣  📂 booth
┣  📂 core
┣  manage.py
┣  📂 notice
┣  📂 project     #  project root
┃ ┣  __init__.py
┃ ┣  asgi.py
┃ ┣  settings.py
┃ ┣  urls.py
┃ ┣  wsgi.py
┃ ┣  requirements.txt
```

## 🎯 Commit Convention
-   feat : 새로운 기능 추가
-   fix : 버그 수정
-   docs : 문서 수정
-   style : 코드 포맷팅, 세미콜론 누락, 코드 변경이 없는 경우
-   refactor: 코드 리펙토링
-   test: 테스트 코드, 리펙토링 테스트 코드 추가
-   chore : 빌드 업무 수정, 패키지 매니저 수정
