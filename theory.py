def calculating(limit):
    collector = set()
    for i in range(1, limit):
        first  =  i
        count = 0
        while i != 1:
            if i % 2 == 0:
                i = i // 2
            else:
                i = 3 * i + 1
            count += 1
        if(count > 100):
            collector.add(first)
    collector  = sorted(collector)
    for key in collector:
        print(key)
calculating(1000)