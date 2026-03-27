def add_border(func):
    def wrapper():
        print("=" * 30)
        func()
        print("=" * 30)
    return wrapper


@add_border
def say_hi():
	print("hi!")
	
say_hi()