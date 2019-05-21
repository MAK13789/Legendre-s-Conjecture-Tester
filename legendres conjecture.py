result = []
xval = []
def isPrime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False

    return True
for i in range(1, 500):
    count = 0
    a = i ** 2
    b = (i + 1) ** 2
    for j in range(a, b):
        if (isPrime(j) == True):
            count = count + 1
    result.append(count)
print (result)
'''
for k in range(1, 500):
    xval.append(k)
print (xval)
'''
