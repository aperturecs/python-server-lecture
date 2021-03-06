초보자도 할수있는 서버개발 #2
==================

##### 지난 시간 복습
- 서버란 무엇인가 (서버 컴퓨터, 서버 프로그램)
- HTTP란 무엇인가?
  - Request, Response
  - Header, Body
  - Cookie
- Python 입문



## 자료형 : Dictionary
살면서 이러한 형태의 데이터를 많이 본 적이 있을 것이다.

> "철수의 전화번호" = "010-1234-5678"  
> "준성이의 이름" = "김준성"  
> "준성이의 여자친구" = "영희"

이 데이터를 자세히 살펴보면, 어떠한 이름과 그에 대응하는 값이 있는 형태로 되어 있다. 파이썬은 이런 이름과 값이 있는 형태의 대응관계를 자료형으로 만들었는데, 이것이 바로 Dictionary이다.

Dictionary는 사전이라는 뜻인데, 마치 사전에서 apple이란 단어에 사과라는 뜻, chair라는 단어에 의자라는 뜻이 들어가 있듯이, Key에 상응하는 Value가 있는 *키-밸류 쌍 (Key-Value Pair)*을 여러개 갖는 자료형이다. 위 예시에서는 "철수의 전화번호"라는 Key에 해당하는 "010-1234-5678"이란 값이 있다.

Dictionary는 다음과 같이 생겼다.

```
{
    Key1: Value1,
    Key2: Value2,
    ...
}
```
여러개의 *Key / Value Pair*가 {과 } 안에 둘러쌓여져 나열되어 있고, 쉼표 (,)로 구분되어져 있다.

```python
dict = { name: 'Hyojun Kim', age: 18, friends: ['김준성', '철수']}
```

데이터에 접근할땐 어떻게 할까? Key를 가지고 접근할 수 있다.

```
>>> dict['name']
'Hyojun Kim'
>>> dict['friends']
['김준성', '철수']
```

Key를 가지고 접근해야 하기 때문에 Key는 고유한 값이고, **동일한 Key가 있을 시 뒤의 값은 무시된다.**

## 자료형 : Tuple
튜플은 여러 개의 변수의 묶음이다. 리스트와 거의 동일하고, 리스트와 유사한 성질을 가지지만, 튜플 내의 값은 **바꿀 수 없다.**

```python
>>> a = (3,4,5) 
```

튜플과 리스트의 사용 용도는 다른데, 튜플은 **변수의 묶음, 즉 여러 개의 변수를 묶을 때** 쓰이고 리스트는 **데이터를 나열할 때** 쓰인다.

### 고급 : 디스트럭쳐링 (Destructuring)
변수를 묶는것만 가지고는 일반 리스트와 너무 차이가 없을 것 아닌가? 튜플은 변수를 묶은 다음에 **풀 수 있는**, *Destructing*이라는 기능을 제공한다.

```python
>>> tuple = (3, 4, "Hello?")
>>> a, b, c = tuple
>>> # 좀더 복잡하게 해봅시다
>>> (a, b, (c, d)) = (3, 4, (5, 6))
```

## 함수
파이썬에서의 함수는 다음과 같이 정의한다.

```python
def 함수이름(파라미터들):
    # 내용 1
    # 내용 2
    return 값
```

함수를 만들고 호출하는 예를 보자.

```python
def sum(a, b):
    result = a + b
    return a + b

a = input("a의 값 입력 : ")
b = input("b의 값 입력 : ")
hap = sum(a, b)
print("%d + %d = %d" % (a, b, hap))
```

다음과 같이 사용할 수 있다. 함수는 **오직 하나**의 리턴값을 가지며, 파라미터 (매개변수)를 넣어서 호출하면 결과가 나온다.  

#### 리턴값 없는 함수
`return` 문을 넣지 않거나, 뒤에 값을 적지 않으면 값을 리턴하지 않을 수 있다. (마치 C언어의 `void`처럼!)

```python
>>> def noAnswer(a, b):
...    result = a + b
...
>>> dap = noAnswer(a, b)
>>> dap
None
```

#### 여러 개의 리턴값

```python
def multiAnswer(a, b):
    sum = a + b
    avg = sum / 2
    return sum, avg
```
위와 같이 여러 개의 리턴값을 줄 수도 있다.  

잠깐, 그런데 하나의 값만 리턴할 수 있다고 하지 않았나? 정답이다. 파이썬에서 여러개의 값을 리턴하면 실제론 하나의 값으로 돌아온다. 바로 여러개의 값이 튜플 (Tuple)로 묶여서 돌아오는 것이다.

```python
>>> a = multiAnswer(3, 4)
>>> a
(7, 3.5)
```
그러면 튜플 형태가 아니라, 그냥 여러개의 리턴값을 여러 개의 변수를 통해 바로 받을 순 없을까? **가능하다.**  
위에서 배웠던 튜플의 디스트럭쳐링 (Destructuring)을 이용하면 된다.

```python
>>> a, sum = calc(3, 4)
```

#### 파라미터에 기본값 지정하기
파라미터에 기본값을 지정해줄 경우, 해당하는 값을 넣지 않아도 자동으로 기본값이 들어간다.

```python
>>> def avg(a, b=10):
...    avg = (a + b) / 2
...    return avg
...
>>> avg(3, 4)
3.5
>>> avg(2)
6
```

#### 함수 안에서 선언된 변수의 효력 범위 (Scope)
함수 안에서도 당연히 변수를 선언할 수 있고, 이는 독립적인 효력 범위 (Scope) 를 지닌다.

```python
def foo():
    bar = 3

bar # NameError: name 'bar' is not defined
```

그러면 만약에, 함수 안에서의 변수 이름과 바깥에서의 이름 (전역 변수) 이 겹치면 어떻게 될까?

```python
bar = 3
def foo(bar):
    bar += 3
    return bar

foo(10) # 결과는 과연? 13 or 6?
```

이를 막기 위해선, `global 변수명`이라고 함수 초반부에 명시해주면 전역 변수를 사용할 수 있다.

```python
bar = 3
def foo(bar):
    global bar
    bar += 3
    return bar

foo(10) # 13
```
