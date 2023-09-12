#make factorial function more coustomable and so easy by recursion
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
inputNum=int(input('Enter recursion number: '))
if inputNum<0:
    print('Factorial of negative number can not be calculated')
elif inputNum==0:
    print('Factorial of 0 is 1')
else:
    result=fact(inputNum)
    print(result)