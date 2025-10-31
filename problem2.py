container = set()
def calculation(limit):
    even_sum = 0
    sorted_container = sorted(container)
    for i in range(1, limit,3):
        print(sorted_container[i])
        even_sum += sorted_container[i]
    print(even_sum)
def phibanoci(limit):
    a = 1
    b = 2
    limit -= 1
    counter = 2 
    container.add(a)
    container.add(b)
    while b <= limit:
        counter += 1
        a, b = b, a + b
        container.add(b)
    print(counter)
    calculation(counter)
phibanoci(4000000)