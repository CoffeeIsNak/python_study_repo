
# 1. memoryview란

- memoryview는 파이썬 내장 클래스 중 하나
    - 바이트 기반 객체(bytes, bytearray 등)의 데이터를 복사하지 않고 직접 참조해서 사용할 수 있게 해주는 객체임.
    - 즉, memoryview는 큰 데이터를 복사하지 않고, 그 데이터의 윈도우를 만들어서 슬라이싱하거나 읽는 도구

```python
data = bytearray(b"hello world")
view = memoryview(data)

print(view[0])       # 104 (ASCII for 'h')
print(view[0:5])     # <memory at 0x...>

# 수정도 가능
view[0] = ord('H')
print(data)          # bytearray(b'Hello world')
```

- `view[0]` = `ord('H')` 는 원본 data 자체를 수정한 것임
    - 이 때 복사가 일어나지 않고 메모리를 직접 참조함.

- 주로 아래와 같은 데이터에 사용함
    - bytes, bytearray
    - array.array
    - numpy.ndarray (넘파이 배열도 메모리 버퍼 인터페이스 제공)
    - 이미지 데이터, 바이너리 파일 등

- 장점 정리
    - 메모리 절약: 큰 데이터를 복사하지 않음
    - 빠른 성능: 슬라이싱/처리 시 메모리 효율적
    - 부분 접근 가능: 특정 위치, 슬라이스만 다룰 수 있음
    - 바이너리 처리: C/C++과 연동하거나, 저수준 작업에 유용


# 2. 실제 사용 예시: numpy 없이 이차원 배열 흉내내기

```python
import array

a = array.array('h', [1, 2, 3, 4, 5, 6])  # 2바이트 정수 배열
mv = memoryview(a)
mv2 = mv.cast('B')  # 1바이트로 변환해서 더 세밀한 제어

print(mv2.tolist())  # [1, 0, 2, 0, 3, 0, ...] (리틀 엔디언)
```

- 예제 코드 설명

1. `array.array('h', [1, 2, 3, 4, 5, 6])`
    - 'h'는 short 정수형(2바이트)를 의미
    - 이 배열은 내부적으로 2바이트씩 6개 = 총 12바이트 메모리를 사용


2. `memoryview(a)`
    - 배열 a의 메모리에 직접 접근할 수 있는 객체를 생성
    - 데이터를 복사하지 않고 참조만 한다는 것에 유의

3. `mv.cast('B')`
    - 원래 2바이트 단위였던 메모리를 1바이트 단위로 잘라서 재해석
    - 'B'는 unsigned char = 1바이트 부호 없는 정수를 의미
    - 즉, 원래 [1, 2, 3, 4, 5, 6]이라는 2바이트 단위 숫자들을, 1바이트 단위로 "바이너리 시점에서 쪼개서 보는 것

4. 출력 결과: `print(mv2.tolist())`

```python
[1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0]
```

- 파이썬(CPython)이 내부적으로 리틀 엔디언(Little Endian) 방식으로 숫자를 저장하기 때문에 위와 같은 출력이 나옴.
    - 리틀 엔디언: 낮은 바이트(LSB)가 먼저 저장되는 방식
        - 예: `1 → 0x01 0x00`, `2 → 0x02 0x00 …`
    - 따라서, `1 → [1, 0]`, `2 → [2, 0]`, ... 식으로 저장되어있음.


- 만약 빅 엔디언 시스템이라면, 아래와 같은 출력 결과가 나왔을 것
    - 하지만 대부분의 현대 시스템(특히 인텔 기반)은 리틀 엔디언을 사용


```python
[0, 1, 0, 2, 0, 3, ...]
```



- 주의할 점
    - memoryview는 가변 객체여야 수정이 가능 (bytearray, array.array 등)
    - bytes는 불변이므로, memoryview를 통해 읽기만 가능

