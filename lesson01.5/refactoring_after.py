from typing import List, Any


def foo1(a: int, b: int) -> List[int]:
    return [i for i in range(a, b)] # [a, b)


def foo2(a: List[int], b: List[int]) -> None:
    for a1, b1 in zip(a, b):
        print(a1, b1)


def foo3(cond: bool, a: int, b: int) -> int:
    return a * 2 if cond else b * 3

def foo4(a: Any, b: Any) -> bool:
    return a is None or b is None or a == b

def foo5(cond: bool, cond1: bool, a: int, b: int) -> int:
    result = b
    if cond:
        result = b * a
    if cond1:
        result = a + b
    return result

def foo6(cond1: bool, cond2: bool, a: int, b: int) -> None:
    if cond1:
        result = a + b
        operation = '+'
    else:
        result = a * b
        operation = '*'

    print(result if cond2 else f'a {operation} b: {result}')

    if not cond2:
        print(f'a {operation} b:', end = '')
    print(result)


def foo7(a: List[int]) -> None:
    for el, i in enumerate(a):
        print(i, el)

def foo8(name: str, a: int):
    "Hi {}. You are {} now".format(name, a)


n, m = 3, 6
matrix = ["#?##..",
          "##..#.",
          "##..#?"]

def is_neighbourghood_empty(x, y, matrix, n, m):
    deltas = [( 0,  0),
              (-1,  0),
              ( 1,  0),
              ( 0, -1),
              ( 0,  1)]
    for dx, dy in deltas:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < n and \
           0 <= new_y < m and \
           matrix[new_x][new_y] != '.':
                return False
    return True

print(is_neighbourghood_empty(0, 5, matrix, n, m))