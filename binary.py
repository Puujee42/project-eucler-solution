def binary_divider(value1,n):
    binary= []
    while value1 > 0:
        binary.append(value1 % n)
        value1 = value1 // n
    binary.reverse()
    return binary
def binary_minus(bin1,bin2):
    bin11 = bin1
    bin22 = bin2
    while len(bin11) > len(bin22):
        bin22.insert(0,0)
    while len(bin22) > len(bin11):
        bin11.insert(0,0)
    collect  = []
    carry = 0
    i = len(bin11)-1
    while i > -1:
        bit1 = bin11[i]
        bit2 =  bin22[i]
        if (bit1 == 1 and bit2 == 1 and carry==0)or(bit1 == 0 and bit2 == 0 and carry == 0):
            collect.insert(0,0)
        elif (bit1 == 1 and bit2 == 0 and carry == 1):
            carry = 0
            collect.insert(0,0)
        elif (bit1 == 0 and bit2 == 1 and carry == 0):
            carry = 1
            collect.insert(0,1)
        elif (bit1 == 0 and bit2 == 1 and carry == 1):
            carry = 1
            collect.insert(0,0)
        elif (bit1 == 0 and bit2 == 0 and carry == 1):
            carry = 1
            collect.insert(0,1)
        elif (bit1 == 1 and bit2 == 0 and carry == 1):
            carry = 0
            collect.insert(0,0)
        elif(bit1 == 1 and bit2 == 1 and carry == 1):
            carry = 1
            collect.insert(0,1)
        elif bit1 == 1 and bit2 == 0 and carry == 0:
            collect.insert(0,1)
        i = i -1
    if(carry == 1):
        collect.insert(1,0)
    return collect
def  binary_adder(bin1,bin2):
    len1 = len(bin1)
    len2 = len(bin2)
    bin11 = bin1
    bin22 = bin2
    while len(bin11) < len2:
        bin11.insert(0,0)
    while len(bin22) < len1:
        bin22.insert(0,0)
    carry = 0
    i = len(bin11) - 1
    result = []
    while i > -1:
        bit1 = bin11[i]
        bit2 = bin22[i]
        if bit1 == 0 and bit2 == 0 and carry == 0:
            result.insert(0,0)
            carry = 0
        elif (bit1 == 1 and bit2 == 0 and carry == 0) or (bit1 == 0 and bit2 == 1 and carry == 0) or (bit1 == 0 and bit2 == 0 and carry == 1):
            result.insert(0,1)
            carry = 0
        elif (bit1 == 1 and bit2 == 1 and carry == 0) or(bit1 == 1 and bit2 == 0 and carry == 1) or(bit1 == 0 and bit2 == 1 and carry == 1):
            result.insert(0,0)
            carry = 1
        elif(bit1 == 1 and bit2 == 1 and carry == 1):
            result.insert(0,1)
            carry = 1
        i = i-1
    if(carry == 1):
        result.insert(0,1)
    return result
def binary_multiplier(bin1,bin2):
    len1 = len(bin1)
    len2 = len(bin2)
    bin11 = bin1
    bin22 = bin2
    while len(bin11) < len2:
        bin11.insert(0,0)
    while len(bin22) < len1:
        bin22.insert(0,0)
    collect = []
    repeat = 0
    for i in range ((len(bin22)-1),-1,-1):
        repeat = repeat + (bin22[i]*(2**(len(bin22)-i-1)))
    for i in range(0,repeat):
        collect = binary_adder(collect,bin1)
    return  collect
def binary_div(bin1,bin2,n):
    bin11 = bin1 
    bin22 = bin2
    while len(bin11) < len(bin22):
        bin11.insert(0,0)
    while len(bin22) < len(bin11):
        bin22.insert(0,0)
    collect  = bin11
    count = 0
    while collect >= bin22:
        collect = binary_minus(collect,bin22)
        count = count + 1
    return binary_divider(count,n)
def binary_mod(bin1,bin2,n):
    bit1 = bin1
    bit2 = bin2
    times = binary_div(bit1,bit2,n)
    value = binary_multiplier(bin2,times)
    result = binary_minus(bin1,value)
    return result
def calculate(value1,value2):
    n = int(input("Enter:"))
    binary1 = binary_divider(value1,n)
    binary2 = binary_divider(value2,n)
    print(binary_div(binary1,binary2,n))
def calculating(value1):
    n = int(input("Enter:"))
    print(binary_divider(value1,n))
calculate(36,6)