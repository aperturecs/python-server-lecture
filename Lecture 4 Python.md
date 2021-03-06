# Python #4 - 파일 입출력, MD5, 모듈 심화

## 파일 입출력

#### 파일 열기 / 생성
다음을 에디터로 작성해서 실행해 보면 프로그램을 실행한 디렉토리에 새로운 파일이 하나 생성되는 것을 확인할 수 있을 것이다.

```python
f = open("새파일.txt", 'w') 
f.close()
```

파일을 생성하기 위해서 우리는 open이란 파이썬 내장 함수를 썼다.  
open함수는 다음과 같이 파일이름과 파일열기모드를 입력으로 받고 리턴값으로 파일 객체를 돌려준다.

 파일 읽기 모드 | 설명 
 -------------|--------
r | 읽기 전용 모드 - 파일 읽기만 할때
w | 쓰기 모드 - 파일을 읽고 쓸 때
a | 추가 모드 (Append) - 파일 끝에 내용을 덧붙일 때

파일을 쓰기 모드로 열게 되면, **해당 파일이 존재할 경우에는 원래있던 내용이 모두 사라지게 되고**, **해당 파일이 존재하지 않으면 새로운 파일이 생성된다.** 위의 예에서는 없는 파일인 “새파일.txt"를 쓰기 모드로 열었기 때문에 새로운 파일인 "새파일.txt"라는 이름의 파일이 현재디렉토리에 생성되는 것이다.

만약 ”새파일.txt"라는 파일을 C:/Python이란 디렉토리에 생성하고 싶다면 절대 경로로 그냥 적어주면 된다.

또한 위에 보면 f.close()를 호출해주는 걸 볼 수 있는데, 이건 열었던 파일 객체를 닫는 것이다. 사실 파이썬이 알아서 열린 객체를 다 닫아주기 때문에 이 문장은 생략해도 무방하지만, 가급적이면 파일 쓰기 시에는 직접 열린 파일을 닫는게 좋다. 닫히지 않은 파일을 다시 쓰려고 시도하면 에러가 발생하기 때문이다.


#### 파일 쓰기

파일을 쓰려면 파일 객체의 write 함수를 사용하면 된다.

```python
f = open('test.txt', 'w')

for i in range(1, 10):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)

f.close()
```

`test.txt`의 내용 : 

```
1번째 줄입니다.
2번째 줄입니다.
3번째 줄입니다.
4번째 줄입니다.
5번째 줄입니다.
6번째 줄입니다.
7번째 줄입니다.
8번째 줄입니다.
9번째 줄입니다.
10번째 줄입니다.
```

###### 파일 끝에 덧붙이기

아까 말했던 a (Append) 모드를 쓰면 된다. 직접 해보자.

#### 파일 읽기
###### 한줄한줄 읽기
파일을 읽는데는 여러가지 방법이 있다. 일단 가장 먼저 알아볼 건 `readline()`을 이용해 한 줄 단위로 읽는 방법이다.

```python
f = open('test.txt', 'r')

line = f.readline()
print(line)

f.close()
```

이렇게 하면 파일의 첫 한줄이 출력될 것이다. 그러면 만약에 파일의 모든 라인을 읽고 싶으면 어떻게 해야할까?

```python
f = open('test.txt', 'r')

while True:
    line = f.readline()
    if not line: break
    print(line)

f.close()
```

무한 반복문을 통해서 한줄한줄 읽어들이는데, 만약에 line이 없다면 입력을 종료하고 break로 빠져나간다.  
(`readline` 함수는 파일의 끝에 도달해서 더이상 읽을 게 없을 시 `None`을 리턴한다.)  

**실습 #1 : ** 파일의 내용을 `readline()` 함수를 이용해 줄 단위로 읽어, 리스트에 담아보시오!

###### 모든 줄을 한번에 읽기

실습 #1을 해봤으면 알겠지만, 그냥 좀 배열에 담아주면 좋을텐데 심각하게 귀찮다. 하지만 파이썬은 그걸 대비해서 미리 함수를 만들어 놓았다.

```python
f = open('test.txt', 'r')
lines = f.readlines()
print(lines)  # ['1번째 줄입니다.\n', '2번째 줄입니다.\n', '3번째 줄입니다.\n', ...]

f.close()
```

###### 통쨰로 읽기
아예 파일 자체를 통째로 문자열로 읽을 수도 있다.

```python
f = open('test.txt', 'r')
str = f.readlines()
print(str)

f.close()
```

#### close()가 귀찮아요!

프로그래머는 반복되고 의미없는 걸 매우 싫어한다! 일일히 close하는건 정말 고통스러운 작업이다.  
그래서 Python은 그걸 대비해서 문법을 미리 만들어 놓았다.

```python
with open('test.txt', 'w') as f:
    f.write('I am lazy ㅁㄴ이ㅏㄹㄴㅁㅇ ㅁㄴㅇ라ㅣㅁㄴ어라ㅣ')
```

## 모듈 심화

## MD5 해싱 방법
```python
import md5
myString = "hello, i am gonna be md5ed"
hashed = md5.md5(myString).hexdigest()
print(hashed)  # 792f5bdd0b5cf1a4ad66996eded147af
```
