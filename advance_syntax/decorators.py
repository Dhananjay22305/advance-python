def wrapper(func):
    def wrap():
        print("Hello")
        func()   # function is actually called here
        print("Bye")
    return wrap

@wrapper
def say():
    print("This is how the decorators work")

say()   # ✅ correct way to call
