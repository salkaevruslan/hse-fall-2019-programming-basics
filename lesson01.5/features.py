def decorator(func):
    def helper(a, b, c):
        return print(func(a, b, c))
    return helper

new_f = decorator(lambda x, y, z: z + y + x * 2)
new_f(1, 2, 3)

@decorator
def foo(x, y, z):
    return x + y + z

foo("1", "2", "3")