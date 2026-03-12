# create a new list that contains the squares
# of only the numbers that are divisible by 10
numbers = [10, 25, 39, 45, 60, 75, 90]

mod_10 = filter(lambda x: x % 10 == 0, numbers)
new_num = [x**2 for x in mod_10]  # Method 1
new_num = list(map(lambda x: x**2, mod_10))  # Method 2
print(new_num)

# reduce()

# reduce(function, iterable, [initializer])
from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda acc, x: acc + [x * 2], numbers, [])

print(result)

# find largest number given reduce
numbers = [15, 3, 27, 9, 42, 8]
result = reduce(lambda x, y: x if x > y else y, numbers)
print(result)

# calculate the total numbers of characters in all words combined
words = ["Python", "is", "powerful", "and", "simple"]  # 25
total_chars = reduce(lambda total, word: total + len(word), words, 0)
print(total_chars)

# iterators
my_list = [10, 20, 30]
iter = iter(my_list)

print(next(iter))
print(next(iter))
print(next(iter))

arr = [0, 1, 2, 3, 4]
iter = map(lambda x: x * 3, arr)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

# generators
def simple_gen():
    print(1)
    yield 1
    print(2)
    yield 2 
    print(3)
    yield 3

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

# tuple