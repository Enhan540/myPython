import random

def write_to_file():
    file = open("numbers.txt", 'w')
    random.seed(42)

    for i in range(3):
        rand_int = random.randint(1,10)
        file.write(str(rand_int))
    file.close()