def calculate():
    n1=(0,3,3,5,4,4,3,5,5,4)
    n10s =(0,3,6,6,5,5,5,7,6,6)
    n11s = (0,6,6,8,8,7,7,9,8,8)
    n = (7,10,11)
    n1to99 = (sum(n1)*9+n10s[1]+sum(n11s)+sum(n10s[2:])*10)*10
    n100to999 = (n[0]*9+n[1]*9*99)+sum(n1)*100
    answer = n1to99 + n100to999 + n[2]
    return answer
print(calculate())