months = [
    ("January", 31), ("February", 28), ("March", 31), ("April", 30), ("May", 31), 
    ("June", 30), ("July", 31), ("August", 31), ("September", 30), ("October", 31), 
    ("November", 30), ("December", 31)
]
with open("steps.txt", 'r') as file:
    all = [int(line for line in file)]
    for month, days in months:
        start = 0
        record = all[start:days]
        start += days
        print(record)
        print(len(record))
        break