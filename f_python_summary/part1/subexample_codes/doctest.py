# 아래 코드를 python -m doctest your_file.py과 같이 실행하여 검사 가능.
def add(a, b):
    """
    >>> add(2, 3)
    6
    """
    return a + b

# 성공하면 아무 출력도 없으나, 실패 시 아래와 같은 출력이 나옴
# C:.../python_study_repo>python -m doctest f_python_summary/part1/subexample_codes/doctest.py
# **********************************************************************
# File "C:\.../python_study_repo\f_python_summary/part1/subexample_codes\doctest.py", line 4, in doctest.add
# Failed example:
#     add(2, 3)
# Expected:
#     6
# Got:
#     5
# **********************************************************************
# 1 items had failures:
#    1 of   1 in doctest.add
# ***Test Failed*** 1 failures.

# pytest, unittest와 비슷하나 docstring 안의 형식을 통해 실행하는 간단한 테스트.
# pip로도 관리 안되는 표준 라이브러리
