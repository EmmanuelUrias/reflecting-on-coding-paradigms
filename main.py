import random


def low_to_high(arr):
    new_array = []
    for i in arr:
        new_array.append(i)
    new_array.sort()

    return new_array


# print(low_to_high([1, 2, 7, 4]))

# How does this solution ensure data immutability?
#   The array that is passed into the function is not altered, it is copied and then sorted.
# Is this solution a pure function? Why or why not?
#   Yes the function is pure because the input is separate from the output.
# Is this solution a higher order function? Why or why not?
#   This is not a higher order function because it does not take in another function as a argument.
# Would it have been easier to solve this problem using a different programming style?
#   I think in this case no. Encapsulating this within a function keeps the code readable and clean and using OOP for this solution would be unnecessary unless you want to sort out an array multiple times across a wide range of classes.
# Why in particular is functional programming a helpful paradigm when solving this problem?
#   Functional programming is simple and safe in this case, no input is altered and everything is clean and simple.


class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        if self.condition == 'trashed':
            self.condition = 'repaired'
            print("All fixed up")
        else:
            print("No need for repair")


p_racer = Podracer(200, 'trashed', 2000)
p_racer.repair()


class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2
        print(f"{self.max_speed}")


p_racer_boost = AnakinsPod(p_racer.max_speed, p_racer.condition, p_racer.price)
p_racer_boost.boost()


class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self, other):
        other.condition = "trashed"
        print(f'other racer: {other.condition}')


p_racer_flame = SebulbasPod(
    p_racer.max_speed, p_racer.condition, p_racer.price)
another_racer = SebulbasPod(
    p_racer.max_speed, p_racer.condition, p_racer.price)

p_racer_flame.flame_jet(another_racer)


# Is one of these coding paradigms "better" than the other? Why or why not?
#   In this case OOP is better because it is a lot better and simpler to make classes and methods to alter our data.
# Given the opportunity to work predominantly using either of these coding paradigms, which seems more appealing? Why?
#   It depends. If im making software that stores and modifies employees data I'd much rather make classes and methods than make functions. If im making some mathematical based software that solves complex formulas for aerospace engineers I might rather use functional programming.
# Now being more familiar with these coding paradigms, what tasks/features/pieces of logic would be best handled using functional programming? Object Oriented Programming?
#   When it comes to math or for some reason I want my code to be procedural like I'd use functional programming. Anything else OOP.
# Personally, which of these styles takes more work to understand? What should be done in order to deepen understanding related to this paradigm?
#   I think depending on the complexity of the classes you might be dealing with the overhead of 7 layers of inheritence so that could be difficult because you'd need a deep understanding of the code. But the same goes for functional if you have 5 functions passing down a chain of data you'd have to read and understand the code top to bottom. But I think the difference lies in the planning phase, in OOP you have to plan out the classes, subclasses, and have a generalized idea for whats going to go inside of those classes and subclasses. In functional programming you have to plan out what each function is going to do and how you want to the data to flow downwards.
