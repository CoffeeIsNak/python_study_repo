
# 아래 코드는 Card라는 간단한 불변 객체(immutable object)를 만듬.
# namedtuple을 쓰면 클래스처럼 필드 접근 가능하면서도, 튜플처럼 가볍고 빠른 객체 생성 가능

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)

print(p.x)  # 3
print(p[1])  # 4 (튜플처럼도 작동)

# Point는 자동으로 __init__, __repr__, __eq__, __getitem__을 제공함.
# 메모리도 적고 불변이기 때문에 안전하고 빠름 => 데이터만 담는 간단한 객체 만들 때 좋음
