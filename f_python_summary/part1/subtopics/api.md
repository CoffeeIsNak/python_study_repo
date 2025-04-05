# 1. API의 사전적 의미

- API = Application Programming Interface = 프로그램과 프로그램이 서로 상호작용할 수 있게 만든 '접점'

- 즉, 나 아닌 다른 코드/시스템을 다룰 수 있게 만든 문법/규약 → '사용자가 써야 할 명령어들의 모음'


# 2. 종류별 예시

- 웹 API (REST API): 다른 서비스에 HTTP로 요청하는 인터페이스 => `requests.get("https://api.github.com")`
- 라이브러리 API: `어떤 라이브러리가 제공하는 함수/클래스` => `pandas.DataFrame()`, `spark.read.csv()`
- 내부 객체 API: `특정 객체가 갖는 인터페이스 (= 메서드들)` => `list.append()`, `str.upper()`
- Python Data Model: 객체가 언어 기능들과 잘 작동하게 만드는 API => `__add__`, `__iter__`, `obj.__len__()`

- API는 '기능'이 아니라, '인터페이스(접점)': 무엇을 할 수 있게 해주는 규칙과 약속을 말함.


# 3. Python Data Model = 언어 내부에서의 객체 API


- `__len__ 구현` → len(obj) 가능

- `__getitem__` 구현 → `obj[i]` 가능

- `__iter__` 구현 → `for obj in ...` 가능

- 이 모든 걸 가능하게 해주는 약속을 Python Data Model이라는 API라고 부름.

- 즉, 파이썬 언어 자체가 요구하는 객체의 인터페이스라고 볼 수 있음.




# 4. Spark의 DataFrame API

- DataFrame 객체의 인터페이스를 말함. => Spark의 DataFrame도 결국 클래스

- `.select()`, `.filter()`, `.groupBy()` 등 → 다 메서드

- 사용자가 DataFrame을 '무엇처럼 쓸 수 있는가'를 정의한 인터페이스를 통틀어서 DataFrame API 라고 부르게 됨.




# 5. 총정리

- API는 기능이 아니라, '규칙과 접점'

- 웹 API: 서버와 상호작용하는 HTTP 약속
- Python Data Model: 파이썬 객체가 언어 문법과 작동하는 인터페이스
- pandas / spark API: 객체가 제공하는 사용 가능한 기능의 집합

- 쉽게말해 사용 설명서 + 버튼들을 말함. => 내부 구현은 몰라도, 이렇게 쓰면 된다는 규약(interface)만 있으면 객체를 사용할 수 있도록 함.

