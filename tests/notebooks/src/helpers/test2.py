def a_func():
    a = 1
    b = 2 * a
    c = a * foo() + b * 3
    print(b, c)


def foo():
    return 2
