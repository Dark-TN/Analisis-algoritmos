n = 10
global rec
rec = 0

def recursion1(n):
    global rec
    if n < 1:
        return 1
    else:
        rec += 1
        return recursion1(n/2) + n

def recursion2(n):
    global rec
    if n < 1:
        return 1
    else:
        for i in range(3):
            rec += 1
            return recursion2(n/2) + n

def recursion3(n):
    global rec
    if n < 2:
        return 1
    else:
        rec += 1
        return recursion3(n-1) + recursion3(n-2)

def recursion4(n):
    global rec
    if n <= 1:
        return 1
    else:
        rec += 1
        return recursion4(n-1) * n

print(recursion4(n))
print(rec)