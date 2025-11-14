import random
collect = []
def calculate(x0,d,p):
    global collect
    if len(collect) == 0:
        collect.append((x0**d)%p)
    else:
        if collect[-1] > 0:
            collect.append(((collect[-1]*len(collect))**d)%p)
        else:
            collect.append(((int(random.random()*100000)//1*len(collect))**d)%p)
for i in range(0,100):
    calculate(2,3,7)
print(collect)