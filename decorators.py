# modifying functions -> function that takes a function as input and returns a modified version of it
def announce(f):
    def wrapper(): # wrapper function
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper


@announce # add decorator
def hello():
    print("Hello World.")

hello()