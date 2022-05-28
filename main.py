#Various different names can be bound to the same function object.
def myPrint(str):
    print(str)

myPrint("Hi to you")

myOtherNameForPrint = myPrint
myOtherNameForPrint("Goodbye")

#Functions can be passed as arguments to another function.
def plus(x,y):
    return x + y

def minus(x,y):
    return x - y

def calc(x,func,y):
    result = func(x,y)
    return result

print (calc(7,minus,3))

#A function can return another function.

def printResult():
    def returnWhatToPrint():
        print(calc(10, plus, 6))
    return returnWhatToPrint()

printResult()

#Basically, a decorator takes in a function, adds some functionality and returns it.
def addThousand(calculation):
    def withAddition():
        print("Adding 1000:")
        print(calculation+1000)
    return withAddition()

addThousand(calc(10, plus, 6))


#Decorating Functions with Parameters

def betterDivide(foo):
    def inner(a,b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return foo(a,b)
    return inner

@betterDivide
def divide(a, b):
    print(a/b)

divide(10,5)
divide(2,0)

#Chaining Decorators
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("Nastya")

#List comprehension
x=[i for i in range(10)]
print(x)

#Dictionary comprehension
j={i: i+2 for i in range(5)}
print(j)

square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)

old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
dollar_to_pound = 0.76
new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
print(new_price)

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
print({k: v for (k, v) in original_dict.items() if v % 2 == 0})

print({k: ('old' if v > 40 else 'young')
    for (k, v) in original_dict.items()})

print({k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)})
#equivalent to:
dictionary = dict()
for k1 in range(11, 16):
    dictionary[k1] = {k2: k1*k2 for k2 in range(1, 6)}
print(dictionary)

#Slicing
print(x[2:5])

#Dataframes
#import pandas as pd
#df = pd.DataFrame(original_dict)