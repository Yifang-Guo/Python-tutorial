class justNotCoolError(Exception):
    pass

x = 2
try:
    #print(x / 1)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed")
    raise justNotCoolError("This isn't cool")
except NameError:
    print("Name error is something undefined")
except ZeroDivisionError:
    print("Can't divided by 0")
except Exception as error:
    print(error)
else:
    print("no errors")
finally:
    print("I'm going to print with or without an error")