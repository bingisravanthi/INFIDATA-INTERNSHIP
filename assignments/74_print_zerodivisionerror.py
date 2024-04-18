A,B=5,0
try:
    A/B
except ZeroDivisionError:
    print("Hello")
except SyntaxError:
    print("hii")
except ValueError:
    print("okay")
else:
    print("bye")
