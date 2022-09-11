import timeit

def main():

def sum1(n):
    
    finalSum = 0
    for x in range(n+1):
        finalSum += x
    
    return finalSum


def sum2(n):
    
    return (n*(n+1)) / 2

print(sum1(10))
sum2(10)

#print(%timeit sum1(100))
#print(%timeit sum2(100))

#timeit.timeit(sum1(100), number=10000)

if __name__ == 