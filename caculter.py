import random
print('made by God_spud')
print('report bugs or suggestions')
print('GitHub page(https://github.com/Godspud/cactuler-Python)')
while True:
    print("select an operation to perform:")
    print('E.evaluate equation')
    print("^.RAISE TO EXPONENT")
    print('root.ROOT TO EXPONENT')
    print('P.permuation')
    print('C.combination')
    print('!.factorial')
    print("r.RANDOM")
    operation = input()
    if operation == 'r':
        r=random.randint(1,7)
        r3=input('input start and end for random seperated by a space')
        r1,r2=r3.split( )
        r2=int(r2)
        r1=int(r1)
        r4=random.randint(r1,r2)
        r5=random.randint(r1,r2)
        if r == 1:
            print('+')
            result=(r4+r5)
            result=str(result)
            print("The sum is "+result)
        elif r == 2:
            print('-')
            result=(r4-r5)
            result=str(result)
            print("The difference is "+result)
        elif r == 3:
            print('*')
            result=(r4*r5)
            result=str(result)
            print("The product is "+result)
        elif r == 4:
            print('/')
            result=(r4/r5)
            result=str(result)
            print("The quotient is "+result)
        elif r == 5:
            print('^')
            result=(r4**r5)
            result=str(result)
            print("The result is "+result)
        elif r == 6:
            print('root to exponent')
            result=(r4**(1/r5))
            result=round(result,10)
            result=str(result)
            print('the result is '+result)
        elif r == 7:
            print('!')
            num2=1
            for fact in range(1,(r4+1)):
                num2=num2*fact
            print(num2)
        else:
            print('Done')
    if operation == 'E':
        print('E(need to have * between brackets')
        function=input('input your equation')
        result=eval(function)
        print(result)
    elif operation == "^":
        print('^')
        num1=float(input("enter first number"))
        num2=float(input("enter exponent number"))
        result=(num1**num2)
        result=str(result)
        print("The result is "+result)
    elif operation == 'root':
        print('root to exponent')
        num1=float(input("enter first number(will get rooted)"))
        num2=float(input("enter exponent number"))
        result=(num1**(1/num2))
        result=round(result,10)
        result=str(result)
        print('the result is '+result)
    elif operation == '!':
        num1=int(input('enter number'))
        num2=1
        for fact in range(1,(num1+1)):
            num2=num2*fact
        print(num2)
    elif operation == 'P':
        num1=int(input('enter first number'))
        num2=int(input('enter second number'))
        num3=1
        num4=num1-num2
        num5=1
        for Perm in range(1,(num1+1)):
            num3=num3*Perm
        for Perm in range(1,(num4+1)):
            num5=num5*Perm
        result=num3/num5
        print(result)
    elif operation == 'C':
        r=int(input('enter first number'))
        n=int(input('enter second number'))
        n1=1
        num4=n-r
        num5=1
        for Perm in range(1,(n+1)):
            n1=n1*Perm
        for Perm in range(1,(num4+1)):
            num4=num4*Perm
        num6=n1*num5
        result=n1/num6
        print(result)
    else:
        print('Done')
