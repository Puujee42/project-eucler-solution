def is_prime(value):
    if value % 2 == 0:
        return False
    for i in range(3,int((value**0.5))+1):
        if value % i == 0:
            return False
    return True
def sigma(val1):
   value = 5
   repeat = val1 // 6
   remainder = val1 % 6
   print(remainder)
   if remainder > 0:
       for i in range(0,repeat):
           if(is_prime(6*(i+1)+1)):
               value  = value + ((6*(i+1))+1)
           if(is_prime(6*(i+1)-1)):
               value = value + ((6*(i+1))-1)
       if remainder > 5:
           if(is_prime(6*(remainder+1)+1)):
               value  = value + ((6*(remainder+1))+1)
   else:
        for i in range(0,repeat):
             if(is_prime(6*(i+1)+1)):
               value  = value + ((6*(i+1))+1)
             if(is_prime(6*(i+1)-1)):
               value = value + ((6*(i+1))-1)
   return value
def calculate(val1):
    result = sigma(val1)
    return result
print(calculate(2000000))  