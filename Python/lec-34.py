# Decorators in Python

def greet(fx):
    def mfx():
        print("Good morning !")
        fx()
        print("Thanks for using this function")
    return mfx

# this is hello function
@greet
def hello():
    print("Hello world")

hello()