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
    if len1 >= len2:
        collect = [0] * (len1 + 1)
        for i in range(len1 - len2):
            bin2.insert(0,0)
        bin1.reverse()
        bin2.reverse()
        for i in range(len1-1,0):
            if bin1[i] == 1 and bin2[i] == 1:
                if i != len1 - 1:
                    if collect[i] == 1:
                        pass
                    else:
                        collect[i + 1] = 1
                        collect[i] = 0
                elif bin1[i] == 1 and bin2[i] == 0:
                    if collect[i] == 1:
                        pass
                    else:
                        collect[i] = 1
                elif bin1[i] == 0 and bin2[i] == 1:
                    if collect[i] == 1:
                        pass
                    else:
                        collect[i] = 1
                elif bin1[i] == 0 and bin2[i] == 0:
                    if collect[i] == 1:
                        pass
                    else:
                        collect[i] = 0
                else:
                    if collect[i] == 1:
                        pass
                    else:
                        collect[i] = 0
                        collect[i + 1] = 1
    else:
        for i in range(len2 - len1):
            bin1.insert(0,0)
    print(collect)
def calculate(value1,value2):
    binary1 = binary_divider(value1)
    binary2 = binary_divider(value2)
    binary_adder(binary1,binary2)
calculate(3,2)