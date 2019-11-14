from typing import List, Any


def foo1(a: int, b: int) -> List[int]:
    result = []
    for i in range(a, b):
        result.append(i)
    return result


def foo2(a: List[int], b: List[int]) -> None:
    length = len(a)
    for i in range(length):
        print(a[i], b[i])


def foo3(cond: bool, a: int, b: int) -> int:
    if cond:
        result = a * 2
    else:
        result = b * 3
    return result


def foo4(a: Any, b: Any) -> bool:
    if a is None or b is None or a == b:
        return True
    else:
        return False


def foo5(cond: bool, a: int, b: int) -> int:
    if cond:
        return a * b
    else:
        return b


def foo6(cond1: bool, cond2: bool, a: int, b: int) -> None:
    if cond1:
        if cond2:
            print(a + b)
        else:
            print("a + b:", a + b)
    else:
        if cond2:
            print(a * b)
        else:
            print("a * b:", a * b)


def foo7(a: List[int]) -> None:
    for i in range(len(a)):
        print(i, a[i])


n, m = 3, 6
matrix = ["#?##..",
          "##..#.",
          "##..#?"]


def is_neighbourghood_empty(x, y):
    result = True
    if matrix[x][y] == '#' or matrix[x][y] == '?':
        result = False
    if x - 1 > 0 and (matrix[x - 1][y] == '#' or matrix[x - 1][y] == '?'):
        result = False
    if y - 1 > 0 and (matrix[x][y - 1] == '#' or matrix[x][y - 1] == '?'):
        result = False
    if y + 1 < m and (matrix[x][y + 1] == '#' or matrix[x][y + 1] == '?'):
        result = False
    if x + 1 < n and (matrix[x + 1][y] == '#' or matrix[x + 1][y] == '?'):
        result = False
    return result
