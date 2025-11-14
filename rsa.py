def gcd(val1,val2):
    if val1 > val2:
        collect = []
        container = []
        for i in range(2,val1):
            if is_prime(i):
                collect.append(i)
        for prime in collect:
            if val1 % prime == 0 and val2 % prime == 0:
                val1 = val1 // prime
                val2 = val2 // prime
                container.append(prime)
        if len(container) == 0:
            return 1
        else:
            ans = 1
            for container_val in container:
                ans *= container_val
            return ans
    else:
        collect = []
        container = []
        for i in range(2,val2):
            if is_prime(i):
                collect.append(i)
        for prime in collect:
            if val1 % prime == 0 and val2 % prime == 0:
                container.append(prime)
        if len(container) == 0:
            return 1
        else:
            ans = 1
            for prime in container:
                ans *= prime
            return ans
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def d_finder(e,n):
    i = 1
    r = e
    while e % n != 1:
        e = r * i
        i += 1
    d = e // r
    return d
def rsa_encryption(p,q,e,text):
    phi_n = int((p-1)*(q-1))
    n = p * q
    d = 0
    ans = []
    answers = []
    if(gcd(phi_n,e)==1):
        d = d_finder(e,phi_n)
        print(d)
        print(n)
        for i in range(0,len(text)):
            a = ord(text[i])
            answer = pow(a,e,n)
            ans.append((answer))
    print(f"Using the e:{e}")
    print(f"Calculated n: {n}")
    print(f"Calculated phi_n: {phi_n}")
    print(f"Calculated private key d: {d}")
    return ans
def decrypt(d,n,ans):
    answers = []
    for i in range(0,len(ans)):
        answer = (ans[i]**d)%n
        answers.append(((chr(answer))))
    return answers
print(rsa_encryption(53,61,17,"mongolia"))
print(decrypt(2753,3233,[2271,2185,2235,2923,2185,745,3179,1632]))
