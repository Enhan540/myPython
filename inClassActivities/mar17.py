# fibonacci sequence
def fib(n: int):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    arr = []
    a, b, c = 0, 1, 1
    for i in range(n - 1):
        c = a + b
        a, b = b, c
    return c


def fib2(n):
    arr = [0] * n + 1
    arr[1] = 1
    for i in range(2, n):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[-1]


# finding unique chars in a string using dict
sentence = "This is a string"

unique_chars = {}
for char in sentence:
    unique_chars[char] = unique_chars.get(char, 0) + 1
print(len(unique_chars))
