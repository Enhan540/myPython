import random


def write_to_file():
    file = open("numbers.txt", "w")
    random.seed(42)

    for i in range(3):
        rand_int = random.randint(1, 10)
        file.write(str(rand_int) + "\n")
    file.close()

def write_float_to_file():
    random.seed(42)
    with open("sales.txt", "w") as file: 
        for i in range(10):
            rand_int = round(random.uniform(1, 10))
            file.write(str(rand_int) + "\n")

def sales_stats():
    with open("sales.txt", "r") as file:
        sales_list = [float(line) for line in file]
    
    print(f"Total sales: {sum(sales_list)}\n"
          f"Average sales: {sum(sales_list)/len(sales_list)}")


def read_file():

    # file = open("numbers.txt", 'r')
    # print(file.read())

    # for loop iterating
    file = open("numbers.txt", 'r')
    acc = 0
    for line in file:
        acc = acc + int(line)
        print(line.rstrip("\n"))
    print(f"Total = {acc}\n")

    # while loop iterating
    file = open("numbers.txt", 'r')
    acc = 0
    line = file.readline()
    while line != "":
        acc = acc + int(line)
        print(line.rstrip("\n"))
        line = file.readline()
    print(f"Total = {acc}")
    
    # List comprehension totalling
    file = open("numbers.txt", 'r')
    total = sum([int(line) for line in file])
    print(f"\nTotal with list comprehension = {total}\n")
    
    # 

    file.close()

def main():
    write_to_file()
    read_file()
    write_float_to_file()
    sales_stats()


if __name__ == "__main__":
    main()