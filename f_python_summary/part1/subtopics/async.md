1. 비동기 프로그래밍

- 기존 프로그램 동작 방식
    - 순차적으로 처리됨 → 하나 끝나야 다음으로 넘어감

```python
response = requests.get("https://example.com")
# 여기서 서버 응답 올 때까지 프로그램이 '멈춰 있음'
```


- 비동기 동작 방식
    - 기다릴 동안 다른 일도 하는 방식
    - 주로 IO (네트워크, 파일, DB) 작업에서 유리함

```python
response = await fetch("https://example.com")
# 기다리는 동안 다른 작업도 동시에 처리할 수 있음!
```


2. 핵심 문법 요약

- async def: 비동기 함수 정의
- await: 비동기 함수 호출 시, 결과 기다림
- async for: 비동기 반복자 순회
- async with: 비동기 컨텍스트 매니저 사용

3. async def & await 사용 예제

```python
import asyncio

async def say_hello():
    print("Hello...")
    await asyncio.sleep(1)  # 1초 대기 (비동기적으로!)
    print("...world!")

async def main():
    await say_hello()

asyncio.run(main())
```

- async def로 만든 함수는 비동기 함수 (coroutine)

- await로 다른 비동기 함수를 호출할 수 있음

- asyncio.run()은 비동기 함수 실행을 위한 이벤트 루프 실행 함수

4. 여러 작업을 동시에 처리하기

```python
async def task(name, delay):
    print(f"⏳ {name} 시작")
    await asyncio.sleep(delay)
    print(f"✅ {name} 끝!")

async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 1)
    )

asyncio.run(main())
```
```css
⏳ A 시작
⏳ B 시작
✅ B 끝!
✅ A 끝!
```

- 위와 같은 문법이라면 비동기적으로 병렬 처리됨.


5. async for

- 예제: 비동기적으로 숫자를 생성하는 반복자

```python
class AsyncCounter:
    def __init__(self, limit):
        self.count = 0
        self.limit = limit

    async def __aiter__(self):
        return self

    async def __anext__(self):
        if self.count < self.limit:
            await asyncio.sleep(1)  # 1초 대기 후 다음 값
            self.count += 1
            return self.count
        else:
            raise StopAsyncIteration

async def main():
    async for num in AsyncCounter(3):
        print(f"📦 값: {num}")

asyncio.run(main())
```

- 쓰는 이유: await가 필요한 반복 작업에서 for 대신 async for 써야 함
    - 매번 await해야 하는 데이터 수신 (웹소켓, API 등)에 적합


6. 정리 요약
    - async def: 비동기 함수 정의 => `async def fetch_data()`
    - await: 비동기 함수 실행 시 대기 => `await asyncio.sleep(1)`
    - async for: 반복하면서 매번 await => `async for msg in stream`
    - async with: 파일/DB 등 비동기 자원 다룰 때 => `async with aiofiles.open()`


- async/await는 기다리는 작업도 효율적으로 처리하기 위한 구조고, async for는 그걸 하나씩 반복하며 기다릴 수 있는 for문으로 확장한 개념









