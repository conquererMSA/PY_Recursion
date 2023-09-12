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
# def power(n,p):
#     if p==0:
#         return 1
#     return n*power(n,p-1) #2*2 #2*2
# print(power(10,10))

# check number prime or not
# def primeNumber(n,i):
#     if i==1:
#         return 1
#     if n%i==0:
#         return 0
#     return primeNumber(n,i-1)
# n=int(input('Enter number to check: '))
# ind=primeNumber(n,n-1)
# if ind==1:
#     print('Prime number')
# if ind==0:
#     print('Not prime number')

#count how many digit contain of a number
#number=1583635 number contain total 7 number
# count=0
def count_digit(n):
    if n<10:
        return 1
    # global count
    # count += 1
    return count_digit(n//10)+1
# return kora count_digit final value dey, zodi given number 346 hoy tobe return
# statement e count-digit(346//10) =34 hobe and return value te 1 add hobe

# result=count_digit(9) #1
# result=count_digit(91) #2
# result=count_digit(9234) #4
# print(result)

# fibonacci series:
# fibonacci series e protom dui term fixed hoy 0 and 1, porer value hobe purbo vorti
# duiti value er addition zemon: 0 +1=> 1=>+ 2=>3+=> 5+=> 8 etc
'''
fibonacci function er given value zodi 3 hoy mane 3 ti term hobe => 0,1,1
zodi term number 4 hoy tobe=> 0, 1, 1, 2 evabe purbo vorti duiti number er addition hobe
'''

def fibonacci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return (fibonacci(n-2)+fibonacci(n-1))

fiboTerm=int(input('Enter fibo term number: '))

# result=fibonacci(fiboTerm) # 10=34 4=2
for i in range(1,fiboTerm+1):
    print(fibonacci(i))
