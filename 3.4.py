###1 вариант
def my_funs(x, y):
    return x ** y
try:
    n1 = int(input("x = "))
    n2 = int(input("y = "))
    print({my_funs(n1, n2)})
except ValueError as e:
    print(f"{e}")







