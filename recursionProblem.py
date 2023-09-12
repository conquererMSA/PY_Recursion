#make factorial function more coustomable and so easy by recursion
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# inputNum=int(input('Enter recursion number: '))
# if inputNum<0:
#     print('Factorial of negative number can not be calculated')
# elif inputNum==0:
#     print('Factorial of 0 is 1')
# else:
#     result=fact(inputNum)
#     print(result)

# find power values of a number
def power(n,p):
    if p==0:
        return 1
    return n*power(n,p-1) #2*2 #2*2
print(power(10,10))

# check number prime or not
def primeNumber(n,i):
    if i==1:
        return 1
    if n%i==0:
        return 0
    return primeNumber(n,i-1)
n=int(input('Enter number to check: '))
ind=primeNumber(n,n-1)
if ind==1:
    print('Prime number')
if ind==0:
    print('Not prime number')