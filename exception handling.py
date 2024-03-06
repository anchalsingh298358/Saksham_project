# file handling + exception handling
a=int(input())
b=int(input())
try:
    c=a/b
    print(c)
except  ZeroDivisionError as e:
    print(e)
except  ValueError as ve:
    print(ve)
except  Exception as ex:
    print(ex)

print('Hello')
