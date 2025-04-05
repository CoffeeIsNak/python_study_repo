# 1. 오버로딩(Overloading) vs 오버라이딩(Overriding)

### 1 - 1. 오버라이딩 (Overriding)

- 부모 클래스에서 정의된 메서드를 자식 클래스에서 덮어쓰기 하는 것

- 예시

```python
class Animal:
    def sound(self):
        return "..."

class Dog(Animal):
    def sound(self):  # ← 오버라이딩
        return "멍멍!"

print(Dog().sound())  # "멍멍!"
```

- 부모의 sound()을 자식이 같은 이름으로 다시 정의함
- 메서드 이름, 인자 수는 그대로, 내부 동작만 바꿈


### 1 - 2. 오버로딩 (Overloading)

- 의미 1: (전통적 의미, C++/Java 스타일) 같은 함수 이름에 서로 다른 인자 개수/타입을 넣는 것

- 파이썬에서는, 전통적 오버로딩을 지원하지 않음. → 대신 *args, **kwargs로 유연하게 처리를 지원.

```python
def greet(*args):
    if len(args) == 0:
        print("Hello!")
    elif len(args) == 1:
        print(f"Hello, {args[0]}!")
```

- 의미 2: 파이썬에서 말하는 오버로딩은 주로 '연산자 오버로딩'을 의미
    - `+`, `==`, `*` 같은 연산자를 내 객체에 맞게 커스터마이징하는 것을 의미.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # ← 오버로딩: + 연산자 재정의
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # 내부적으로 v1.__add__(v2) 호출됨
```

### 1 - 3. 요약 비교

- 구분: 오버라이딩 (Overriding)
    - 정의: 상속 관계에서 부모 메서드 덮어쓰기
    - 예시: 자식 클래스에서 sound() 재정의
    - 목적: 상속받은 동작을 바꾸기
    - 인자 수 변경: 불가 (같은 시그니처)

- 구분: 오버로딩 (Overloading)
    - 정의 연산자나 함수 동작 재정의
    - 예시 `__add__`, `__eq__`, `__getitem__`
    - 목적: 연산자나 함수 호출을 바꿈.
    - 인자 수 변경: 가능 (오버로드처럼 보이지만 args로 처리)


- 파이썬에서 지원하는 오버로딩 종류

- 연산 / 매직 메서드
    - `+`: `__add__`
    - `-`: `__sub__`
    - `*`: `__mul__`
    - `==`: `__eq__`
    - `[]`: `__getitem__`
    - `()`: `__call__`

### 1 - 4. 부록? args, kwargs 참고

- 예제 1: `*args`

```python
def add_all(*args):
    print(args)
    return sum(args)

add_all(1, 2, 3, 4)  # (1, 2, 3, 4)
```

- args는 (1, 2, 3, 4)라는 튜플로 들어옴
- 위치 기반 인자를 모두 묶어서 하나로 처리

- 예제 2: `**kwargs`

```python
def print_info(**kwargs):
    print(kwargs)

print_info(name="헌성", job="Data Engineer")
# {'name': '헌성', 'job': 'Data Engineer'}
```

- kwargs는 딕셔너리: `{key: value}`
- 키워드 인자를 모두 묶어서 하나로 처리


- 예제 3: 통합 예시

```python
def greet(name, job):
    print(f"Hello, {name} the {job}!")

info = ("헌성", "Data Engineer")
greet(*info)  # Hello, 헌성 the Data Engineer!

info_dict = {"name": "헌성", "job": "Data Engineer"}
greet(**info_dict)  # 동일 결과
```
