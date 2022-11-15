<h2>path 등록</h2>
1. 주소를 지정

2. 어떤 view를 실행할건지 지정


<h2>업로드 최적화 하기</h2>
1. venv 폴데 있는 폴더에 ```.gitignore``` 생성
2.  .gitignore에 ```venv/``` 입력
3. ```pip -r requirements.txt```
4. ```pip freeze > requirements.txt```
2. ```rm -r .git```

<다시 환경 다운 받을 경우>

```pip install -r requirements.txt```



<h2>협업 업로드</h2>

1.  ```git checkout -b 새로운 브랜치``` 새로운 브랜치 생성
2.  작업
3.  ```git add .``` 깃에 작업한 것 추가
4.  ```git commit -m '메세지'``` 작업한 것 메세지로 입력
5.  ```git push origin 1번에서 만든 브랜치``` 작업한 것 Push
6.  ```git checkout  **master**```  브랜치 **master**로 변경
7.  ```git pull origin master```  작업한 목록 받기
8.  ```git branch -d 1번에서 만든 브랜치``` 생성한 브랜치 삭제
