# Git Branch 사용법

## Git branch (1인)

##### 통합브랜치

기능별로 완성되면 통합 브랜치 ver 1.0 , 1.1, 1,2

##### 토픽브랜치

기능 추가, 버그

**토픽브랜치에서 특정 작업 완료되면 통합브랜치로 병합**

​    

#### 처음 code

``` 
$ git init = > master 브랜치 생성
$ git add .
$ git commit -m "~~~~(ex. first commit)"
```



branch는 단순한 포인터다

HEAD는 단순한 포인터(포인터의 포인터의 경우가 많다.)

HEAD는 현재 내가 작업중인 commit을 의미

HEAD가 master에 있다 == 현재 master에서 작업중이다.



##### 브랜치 생성

```
$ git branch b1(브랜치 명)
```

내가 현재 있는 곳에서  브랜치 생성됨



##### 브랜치 전환

```
$ git switch b1(브랜치 명)
```



부모 커밋밖에 보지 못한다.

브랜치는 파일저장이 아니라 커밋이 저장의 기준이 된다.

##### 

##### 브랜치 병합

병합시키고 싶은 브랜치(더 큰)로 이동하기(나아가야할 포인터)

```
$ git merge 흡수당할브랜치 명
```



##### 병합 종류 세가지

1. master가 branch에서 여러 커밋을 해왔는데 그냥 이동만 해온 것 ?(Fast-Foward)

2. 알아서 Merge branch되는 경우(Auto Merge), 새로운 커밋을 동반함

3.  똑같은 파일이나 내용이 겹쳐서 Auto Merger Conflict 되는 경우, vs code에서 수정하라고 알려줌

   

#### 기타

```
$ git log --oneline (git 히스토리?를 한줄로 보는거)
$ git log --oneline --graph (git 히스토르 그래프까지 보여줌)
$ git branch (현재 사용하고 작업하고 있는 모든 브랜치들)
$ git switch -c 브랜치명 (브랜치를 생성하면서 거기로 스위치)
$ git branch -d 브랜치명 (브랜치명 삭제)
```



## Git branch (협업)

맨처음 git clone 주소  폴더 이름

git 

git push origin 브랜치명

merge request (내 로컬저장소 있던 것들 리모트 저장소에 합치기)

git pull origin master(저장소합치고 내 로컬에서도 통일화)

그다음 새 로컬 브랜치 생성 후 이동 git switch -c 브랜치명

