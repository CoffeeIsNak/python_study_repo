# 0. 궁금했던 점들

- Python은 어떤 방식으로 "얘는 리스트처럼 행동하네"라고 판단하는가?

- 그걸 위해 `__getitem__`, `__len__` 같은 특정 매직 메서드 조합을 체크하는 건가?

- 그럴 바엔 그냥 list를 상속받으면 더 낫지 않나?

- 이에 관한 파이썬의 객체 철학이 있음.


# 1. 파이썬은 인터페이스를 타입이 아니라 행동(행동 기반 프로토콜)으로 판단함.

- 이걸 덕 타이핑(Duck Typing) 이라고 함. => '오리처럼 걷고, 꽥꽥거리고, 오리처럼 생겼다면 오리다.'
- 즉, 타입을 명시적으로 검사하지 않고, 그냥 그렇게 행동하는지만 본다.

- Python에서 리스트처럼 보이는 객체의 기준
    - 즉, 어떤 객체가 `__getitem__()`과 `__len__()`만 갖고 있으면,
    - for x in obj 가능, len(obj) 가능, `obj[i]` 가능
    - 그래서 Python은 얘는 시퀀스처럼 동작한다고 판단 => 이걸 "시퀀스 인터페이스를 따른다"고 표현


```python
# 리스트처럼 반복할 수 있는가? → iterable?
# 리스트처럼 슬라이싱 가능한가? → __getitem__
# 리스트처럼 길이 구할 수 있는가? → __len__
```





- 예제: 리스트처럼 동작하는 내 객체 만들기

```python
class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

ml = MyList([1, 2, 3])
print(len(ml))     # 3
print(ml[1])       # 2
for x in ml:
    print(x)       # 1 2 3
```

- for x in ml가 되는 이유:  → `__getitem__`이 존재하면 iter() 없이도 자동 반복 가능
    - 내부적으로 i = 0; while True: obj[i] 시도함.


# 2. 파이썬은 인터페이스 검사를 명시적으로 하지 않음

- 다른 언어 예시 (Java)

```java
if (obj instanceof List) ...
```

- Python 동작
    - 여기서 seq가 list인지 tuple인지 MyList인지 몰라도 상관 없음
    - 그냥 for가 가능하기만 하면 됨 => 행동 기반 인터페이스 = Protocol

```python
def do_something(seq):
    for x in seq:
        ...
```



# 3. 왜 상속받지 않고 직접 매직 메서드 구현할까?

1. 유연성 (Duck Typing 철학)

```python
class MyCustomStream:
    def __iter__(self): ...
    def __next__(self): ...
```

- 이걸 list 상속 안 받고도 for문 돌릴 수 있음 → 상속 필요 없음

2. list 상속은 동작을 고정시킴

```python
class MyList(list):
    ...
```

- 이건 진짜 list 그 자체의 동작을 물려받음
- 원하지 않는 기능까지 포함될 수 있음 (sort, insert, etc.)

3. Mixin이 더 낫다

- Python은 상속보다 조합(composition)을 선호
    - 필요한 메서드만 골라서 인터페이스만 맞추면 된다는 유연함을 좋아함
    - 이걸 non-inheritance polymorphism 이라고도 함.



4. `collections.abc`의 시퀀스 인터페이스 체크 방법

```python
from collections.abc import Sequence

class MyList:
    def __getitem__(self, i): ...
    def __len__(self): ...

isinstance(MyList(), Sequence)  # False (상속 안 했으니까)
```

- 하지만 for, len, [] 전부 동작함 → 행동은 완전히 Sequence와 일치

