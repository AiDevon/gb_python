def print_decorator(func):
    def wrapper(*args,**kwargs):
        print("start")
        func(*args, **kwargs)
        print("end")

    return wrapper

@print_decorator
def show_message(content):
    print(content)

show_message("Hello, decorator")