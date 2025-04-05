
# 1. bytearray

- bytes와 거의 똑같지만, '수정 가능(mutable)'한 버전
    - bytes: 불변 (immutable), 바이너리 데이터 읽기에 사용
    - bytearray: 변경 가능 (mutable), 바이너리 데이터 수정, 네트워크, 버퍼 작업 등에 사용


- bytes 예제

```python
b = bytes([65, 66, 67])
print(b)       # b'ABC'
b[0] = 90      # ❌ TypeError: 'bytes' object does not support item assignment
```

- bytearray 예제
    - 90은 ASCII로 Z에 해당

```python
ba = bytearray([65, 66, 67])
print(ba)      # bytearray(b'ABC')
ba[0] = 90
print(ba)      # bytearray(b'ZBC')
```


# 2. 용례

1. 파일에서 읽은 바이너리 데이터를 수정하고 싶을 때

```python
with open('image.png', 'rb') as f:
    raw = bytearray(f.read())
    raw[0] = 0  # 첫 바이트 수정
```

2. 버퍼 처리, 네트워크 I/O, 영상처리 등 속도 + 메모리 중요한 상황
    - 데이터 복사 없이 바로 바이트 단위 조작
    - 특히 C 확장, NumPy, socket, memoryview와 잘 어울림

3. bytearray 생성 방법

```python
bytearray([65, 66, 67])   # → b'ABC'
bytearray(b'hello')       # → b'hello'
bytearray(5)              # → b'\x00\x00\x00\x00\x00' (0으로 채운 5바이트)
```

4. 추가 특징
    - 슬라이싱 가능: `ba[1:3]`
    - 반복 가능: `for b in ba:`
    - len(ba): `바이트 개수`
    - `.hex()`: 헥사 문자열(아스키 코드를 16진수로 바꾼 문자열) 변환

- 정리
    - bytearray는 바이너리 데이터 처리할 때 쓰는 가변 시퀀스 타입이다.
    - bytes는 읽기 전용, bytearray는 읽기+쓰기 가능!
    - memoryview, struct, pickle, socket 같은 거에 자주 쓰인대
