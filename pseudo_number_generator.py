import random
collecting = []

def calculate(x0,m):
    global collecting
    collect = []
    for i in range(1, 100):
        value = int(random.random() * 100000) + int(random.random() * 1000000)
        collect.append(value)
    if len(collecting) > 0:
        idx = random.randint(0,100)
        if idx == 100:
            idx = 99
        world = random.randint(0,100)
        collecting.append(((collecting[-1]**collect[idx]) )%m)
    else:
        collecting.append(x0)
    return collecting[-1]
for i in range(0,100):
    calculate(5,17)
print(collecting)