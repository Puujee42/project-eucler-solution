def binary_divider(value1):
    binary= []
    while value1 > 0:
        binary.append(value1 % 2)
        value1 = value1 // 2
    binary.reverse()
    return binary
def  binary_adder(bin1,bin2):
    print(bin1)
    print(bin2)
    len1 = len(bin1)
    len2 = len(bin2)
    collect = []
    if len1 > len2:
        for i in range(len1 - len2):
            bin2.insert(0,0)
        for i in range(0,len(bin2)):
            collect.append(0)
        for i in range(len(bin2)-1,-1,-1):
            if bin1[i] == 1 and bin2[i] == 1:
                if collect[i] == 1  and i < len(bin2)-1:
                    collect[i] = 1
                    collect[i-1] = 1
                elif collect[i] ==  1 and i == len(bin2)-1:
                    collect[i] = 0
                    collect.insert(0,1)
                else:
                    collect[i] = 1
            elif bin1[i] == 0 and bin2[i] == 1:
                if collect[i] == 1  and i < len(bin2)-1:
                    collect[i] = 1
                    collect[i-1] = 1
                elif collect[i] ==  1 and i == len(bin2)-1:
                    collect[i] = 0
                    collect.insert(0,1)
                else:
                    collect[i] = 1
            elif bin1[i] == 1 and bin2[i] == 0:
                if collect[i] == 1  and i < len(bin2)-1:
                    collect[i] = 1
                    collect[i-1] = 1
                elif collect[i] ==  1 and i == len(bin2)-1:
                    collect[i] = 0
                    collect.insert(0,1)
                else:
                    collect[i] = 1
            else:
                pass
    elif len2 > len1:
        for i in range(len2 - len1):
            bin1.insert(0,0)
        print(bin1)
        for i in range(0,len(bin1)):
            collect.append(0)
        print(collect)
        for i in range(len(bin1)-1,-1,-1):
            if bin1[i] == 1 and bin2[i] == 1:
                if collect[i] == 1  and i < len(bin1)-1:
                    collect[i] = 1
                    collect[i-1] = 1
                elif collect[i] ==  1 and i == len(bin1)-1:
                    collect[i] = 0
                    collect.insert(0,1)
                else:
                    collect[i] = 1
            elif bin1[i] == 0 and bin2[i] == 1:
                if collect[i] == 1  and i < len(bin1)-1:
                    collect[i] = 1
                    collect[i-1] = 1
                elif collect[i] ==  1 and i == len(bin1)-1:
                    collect[i] = 0
                    collect.insert(0,1)
                else:
                    collect[i] = 1
            elif bin1[i] == 1 and bin2[i] == 0:
                if collect[i] == 1  and i < len(bin1)-1:
                    collect[i] = 1
                    collect[i-1] = 1
                elif collect[i] ==  1 and i == len(bin1)-1:
                    collect[i] = 0
                    collect.insert(0,1)
                else:
                    collect[i] = 1
            else:
                pass
    print(collect)
def calculate(value1,value2):
    binary1 = binary_divider(value1)
    binary2 = binary_divider(value2)
    binary_adder(binary1,binary2)
calculate(100,10000)