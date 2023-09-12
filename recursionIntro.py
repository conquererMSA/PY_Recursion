import sys
'''
Recursion in python: When a function call itself then call it's a recursion.

**Recursion e clean code hoy, and complex problem solving e recursion use hoy.
**Recursion complex howyay eta debug korte kosto hoy. Recursion infinity time call
howyay eta memory efficient hoy na.

Sadaronoto recursion infinity time call hoy, tobe python e recursion_limit 1000.
sys.setcursionlimit(number) function call kore recursion limit set kora zay.
sys.getrecursionlimit() call kore python e recursion er excedeed number pawya zay.
recursionlimit 6 er niche set kora zay na.

'''
# i=0
# recurLimit=sys.getrecursionlimit()
# sys.setrecursionlimit(7)
# print(recurLimit)

# def recursionFunc():
#     global i
#     print(i)
#     i=i+1
#     recursionFunc()
# recursionFunc()

# direct recursion: zokhon ekti function defination e function call hoy and stoping
# condition onuzayee seta return hoy tokhon sei recursion ke direct recursion bole.


# def naturalNum(n):
#     print(n) #11-1
#     if n==1:
#         # naturalNum(n - 1) #11
#         return
#     naturalNum(n - 1)
#     # print(n) #2-11
#
#
# lastNum=int(input('Enter the last number: '))
# naturalNum(lastNum)

# indirect recursion: pasa-pasi duiti function za ekti opertike call korbe and ditio
# function theke recursion start hobe. indirect recursion e o infinite looping call
# create hote pare. eta memmory efficient na.
# def recursive1(n):
#     if n<0:
#         return
#     print(n)
#     recursive2(n-1)
# def recursive2(n):
#     print(n)
#     recursive1(n-1)
#
# recursive1(10) #10-(-1)
# # recursive2(10) #10-1

'''
find factorial value of a number by recursion
5! =5*4*3*2*1
5! =5*4!
   =5*4*3! =20*31!
   =20*3! =20*3*2!
   =60*2! =60*2*1!
   =120*1! =120*1
   =120, za 5 er factorial
   **sob somoy previous number er value gulur factorial er sathe current number er 
   factorial er value multiply korte hobe... zemon first number 5 er factorialValue 
   hobe, 5*factorial(5-1) //5-1=4 za 0 theke boro
         5*4*factorial(4-1) //4-1=3 za 0 theke boro
         20*3*factorial(3-1) //3-1=2 za 0 theke boro
         60*2*factorial(2-1) //2-1=1 za 0 theke boro
         120*1*factorial(1-1) //1-1=0 za 0 er soman
         120*factorial(0), factorial number 0 holei 1 return korbe ortath recursion 
         bondho hoye zabe and factorial function output return korbe 1*120=120
         
   
def factorial(n):      
     if n==0:
        return 1
     return n*factorial(n-1)
     
factorialValue=factorial(5)
print(factorialValue) #120
'''
def factorial(n):
    # 5
    # 4
    # 3
    # 2
    # 1
    # 0 holei stoping condition 1 return korbe
    if n==1:
        return 1
    return n*factorial(n-1)  #return value
#          5*factorial(5-1)
#          20*factorial(4-1)
#          60*factorial(3-1)
#          120*factorial(2-1)
#          return 120 factorial value

factInput=int(input('Enter your number: '))
factorialValue=factorial(factInput)
# print(factorialValue)

#print your name given times by recursion
count=1
def namePrinter(name):
    global count
    if count<=10:
        print(f"{name,count}")
        count+=1
        namePrinter(name)
namePrinter('MSA')