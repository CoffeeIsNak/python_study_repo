# 1. 컨텍스트(Context)

- 특정한 실행 환경 또는 범위를 뜻함.

- 예제

```python
with open("file.txt") as f:
    data = f.read()
```

- 여기서 with 블록 안이 바로 파일 열기라는 컨텍스트임.
- 이 범위가 끝나면 자동으로 닫히는 행동이 일어남.

# 2. 컨텍스트 매니저

- 컨텍스트 시작과 끝에서 무언가를 자동으로 처리해주는 객체를 말함.

- 예:
    - 파일 열고 닫기
    - DB 연결하고 끊기
    - 락(lock) 걸고 풀기
    - 타이머 시작하고 종료

- 대표적 문법

```python
with some_context_manager as obj:
    # 여기가 컨텍스트
    do_something()
```

- 위 구조에서 내부적으로는 아래와 같이 동작하게 됨.

```python
obj = some_context_manager.__enter__()
try:
    do_something()
finally:
    some_context_manager.__exit__()
```

# 3. 직접 구현하기

```python
class MyContext:
    def __enter__(self):
        print("👉 컨텍스트 진입")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("👈 컨텍스트 종료")

with MyContext():
    print("🧪 무언가 실행 중")
```

- 출력 결과는 아래와 같음.

```md
👉 컨텍스트 진입
🧪 무언가 실행 중
👈 컨텍스트 종료
```

- `__enter__()` → 진입할 때 실행됨
- `__exit__()` → 정상 종료든, 예외든 상관없이 무조건 실행됨
- 즉, 리소스를 안전하게 정리하는 코드 자리임.

# 4. 용례

- 파일 다루기

```python
with open("data.csv", "r") as f:
    data = f.read()
# 여기서 자동으로 f.close() 실행됨
```

- 락 걸기

```python
lock = threading.Lock()

with lock:
    do_thread_safe_thing()
```

- 시간 측정

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        elapsed = time.time() - self.start
        print(f"⏱️ 경과 시간: {elapsed:.2f}초")

with Timer():
    time.sleep(2)
```

# 5. 비동기 컨텍스트 매니저: async with

```python
async with aiofiles.open("data.txt", "r") as f:
    data = await f.read()
```

- 이 때는 `__aenter__()` / `__aexit__()` 메서드를 구현해줘야 함.
- async for, async with은 모두 await와 함께 쓸 수 있는 컨텍스트/반복의 확장판에 해당함.

- 정리 요약
    - Context: 어떤 동작이 이뤄지는 환경/범위
    - Context Manager: 진입/종료 시 자동 처리할 코드 포함한 객체
        - `__enter__()`: with 블록 들어갈 때 실행됨.
        - `__exit__()`: with 블록 나올 때 실행 (예외 여부 무관)
    - async with: 비동기 컨텍스트, await 가능한 자원 다룰 때

- 마무리 요약
    - 컨텍스트 = '열고 닫는 구조의 실행 범위'
    - 컨텍스트 매니저 = 그 범위에 진입/종료할 때 자동 행동하게 해주는 객체






