try:
    raise ZeroDivisionError ("demo message")
except ZeroDivisionError as e:
    print("am at ZeroDivisionError block")
    print("e value:",e)
