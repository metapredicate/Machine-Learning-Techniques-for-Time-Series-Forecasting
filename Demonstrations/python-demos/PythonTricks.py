# Title
# This is a collection of various more sophisticated python code you might consider using for your coding.
# Most python tutorial will likely be beginner level, so I wanted to share some stuff you're well capable of 


# OVERVIEW OF OBJECT ORIENTED PROGRAMMING 
class Person(object):
    # construct is done with __init__(self, arg1, arg2)
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age
        # I can set default instance variables
        self.haircolor = "brown"
        self.school = None
    # instance methods are likewise easy. You just need to include the 'self' keyword.
    def introduce(self):
        # You'll be likely use print() a lot, so this is how you can print contents of variables into your string
        print("Hello, my name is {}. I am {} years old, my haircolor is {}.".format(self.name, self.age, self.haircolor))

# Inheritence in Python is done like this
class Trinner(Person):
    def __init__(self, name, age, course):
        # we can still use the parent class' constructor via
        Person.__init__(self, name, age)
        self.course = course
        self.college = "Trinity"
    def smugTrinnerBrag(self):
        print("I am a {} student, I got to {} college. How about that >:-)".format(self.course, self.college))
    def introduce(self):
        #likewise
        Person.introduce(self)
        self.smugTrinnerBrag()


# PROGRAMMING PARADIGMS COMPATIBLE WITH PYTHON

# We discussed different ways you could approach various problems using Python.
# Let's say we want to take a list of integers e.g. [1,2,3,4,5] and return that list but with each element incremented by one [2,3,4,5,6]
# We could just use Iteration
def imperativeInteration(listOfIntegers):
    # for loops in python are always of this format: for <index> in <iterable>:
    # you can not do say a java syntax for loop which would look like for(i = 0 ; i < limit ; i++)
    newListOfIntegers = []
    for i in range(len(listOfIntegers)):
        newListOfIntegers.append(listOfIntegers[i] + 1) 
    return newListOfIntegers

# Another approach would be to use recursion. This particular solution is not so straightforward, but I wanted to give an example
def tailRecursive(listOfIntegers):
    newListOfIntegers = []
    # you can do multiple assignments in one line like this
    try:
        firstElement = listOfIntegers[0]
        restOfTheList = listOfIntegers[1:] # 1: specifies the second element up to and including the last element
    except IndexError:
        return []
    # We recursively concatenate a list together whilist incrementing the first element.
    # The first element is different on each recursive function call because are calling tailRecursive on an continously shriking list 
    newListOfIntegers.append(firstElement+1)
    return newListOfIntegers + tailRecursive(restOfTheList)

# This approach is super cool, and would be in keeping with the Functional Programming paradigm. You would usually expect to write
# code similiar to this in a declarative functional programming language, however in Python functions are also first class citizens
# so we can do this here too. We use what are known as Higher-Order functions to write some super expressive code.
def incrementUsingHigherOrderFunctions(listOfIntegers):
    # This is a super tidy way to do this work.
    result = map( lambda x : x + 1 , listOfIntegers)
    return list(result)
    # this solution is going to need some explaination:
    #   1.  Higher-Order functions are defined as being functions which either take a function as an input,
    #       or a function which returns a function in its output.
    #   2.  map() is a Higher-Order Function, and its the most straightforward example of one really.
    #       What it does essentially is it takes a function of some sort in its first parameter,
    #       and it takes a list of some kind in its second parameter, and it applies this function
    #       to each element in the list. I actually expected map to return a list outright, but it instead returned
    #       a "map" object, so I needed to cast result to a list.
    #   3.  This lambda keyword is a function. Its a special type of function which is more similiar to a function
    #       from your Leaving Certificate Project Maths; for each input there is only ever one corresponding output.
    #       This is as you will remember called an injective function. In programming speak, we say that this function
    #       has no "Side Effects", and we can consider such functions to be known as Lambda Functions (from Alonzo
    #       Church's Lambda Calculus). Lambda calculus is a big deal in the programming world as Lambda Calculus was one
    #       of the two original theories which explain Turing Completeness - the other being Turing Machines which is a
    #       state based representation of computation. 
    #   4.  So our lambda function is analogous to increment(x): return x+1 .
    #   5.  So what our code does is it takes this lambda function and returns a list consisting of each element in
    #       listOfElements applied to this lambda. I hope this explaination makes sense. 

# MAIN METHOD

print("hello there from outside main :-) - I am above it.")

# How to do a Main method
if(__name__=='__main__'):
    eoin = Trinner("Eoin Dowling", "23", "Computer Science")
    eoin.introduce()
    print("Let's demo our functions with the list [1, 2, 3, 4]")
    demoList = [1,2,3,4]
    print("imperativeIteration yields:                {}".format(imperativeInteration(demoList)))
    print("tailRecursive yields:                      {}".format(tailRecursive(demoList)))
    print("incrementUsingHigherOrderFunctions yields: {}".format(incrementUsingHigherOrderFunctions(demoList)))
# such a main method is not strictly required, but it is cool in so far it will only ever be called if you run this whole file.
print("hello there from outside main :-) - I am below it.")