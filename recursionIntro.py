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


def naturalNum(n):
    print(n) #11-1
    if n==1:
        # naturalNum(n - 1) #11
        return
    naturalNum(n - 1)
    # print(n) #2-11


lastNum=int(input('Enter the last number: '))
naturalNum(lastNum)