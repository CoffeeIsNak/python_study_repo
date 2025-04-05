# 1. Coroutine - 대기 가능한 함수

### 1 - 1. 정의

- 정의: 코루틴은 중간에 멈췄다가 다시 실행될 수 있는 함수

- 일반 함수

```python
def foo():
    return 42
```

- 코루틴

```python
async def foo():
    await asyncio.sleep(1)
    return 42
```

- 중간에 await 만나면 잠시 멈췄다가, 나중에 다시 실행됨

- 상태를 기억하면서 멈췄다 재개 가능 = 일종의 협력형 멀티태스킹


### 1 - 2. 일반 함수 vs 코루틴

- 일반 함수	
    - 정의: def
    - 실행 방식: 즉시 실행
    - 결과: 즉시 반환
    - 예시: result = func()

- 코루틴
    - 정의: async def
    - 실행 방식: 대기 가능, 예약됨
    - 결과: coroutine object 반환 (나중에 실행)
    - 예시: result = await coro()



### 1 - 3. 주의점


```python
async def foo():
    return 1
```

- 위 코드는 실행되지 않음 → foo()는 그냥 coroutine object를 반환할 뿐

- 실제로 실행하기 위해서는 아래와 같이 작성.

```python
# 1. await
await foo()

# aysncio.run() 사용
asyncio.run(foo())
```

# 2. 이벤트 루프 (Event Loop) — 코루틴을 실행시키는 스케줄러

### 2 - 1. 정의

- 코루틴들을 스케줄링하고 실행 순서를 정해주는 파이썬의 작업 관리자

- 비유
    - async def는 작업 지시서
    - await는 잠시 멈춤 요청
    - 이벤트 루프는 일을 언제 할지 결정하고 실행시키는 사장님

- 이벤트 루프의 실제 흐름
    - `asyncio.run()` → 이벤트 루프 시작
    - `hello()` 코루틴 → 루프에 등록됨
    - `await asyncio.sleep(1)` 만나면 다른 작업 먼저 수행 가능
    - 1초 후 다시 돌아와서 실행 재개

```python
import asyncio

async def hello():
    print("1초 기다림 시작")
    await asyncio.sleep(1)
    print("1초 기다림 끝!")

asyncio.run(hello())
```



### 2 - 2. 코루틴 용례

- 코루틴
    - `async def fetch_data()`: 데이터 요청을 비동기로 처리
    - `await fetch_data()`: 다른 작업 하면서 기다릴 수 있음


- 이벤트 루프 사용
    - `asyncio.run()`: 메인 루프
    - `asyncio.gather()`: 여러 작업 병렬 처리
    - `asyncio.create_task()`: 태스크로 예약 → 루프가 관리



