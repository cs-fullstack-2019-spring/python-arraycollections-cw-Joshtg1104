def main():
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    problem5()



# ### Problem 1:
# Create a function with the variable below. After you create the variable do the instructions below that.
# ```
# arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
# ```
# a) Print the 3rd element of the numberList.
#
# b) Print the size of the array
#
# c) Delete the second element.
#
# d) Print the 3rd element.

def problem1():
    arrayForProblem1 = ["Kenn", "Kevin", "Erin", "Meka"]

    print(arrayForProblem1[2])
    print(len(arrayForProblem1))
    arrayForProblem1.remove("Kevin")
    print(arrayForProblem1[2])


# ### Problem 2:
# ##### We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.

def problem2():
    saySomething = input("Type Something, Dude. Press Q to Give Up.")

    while True:
        if saySomething == "q" or saySomething == "Q":
            break
        else:
            saySomething = input("Try Again, My Man.")

# ### Problem 3:
# Create a function that contains a collection of information for the following.
# After you create the collection do the instructions below that.
# ```
# Jonathan/John
# Michael/Mike
# William/Bill
# Robert/Rob
# ```
# a) Print the collection
#
# b) Print William's nickname

def problem3():
    nickNames = {
        "Johnathan": "John",
        "Michael": "Mike",
        "William": "Bill",
        "Robert": "Rob"
    }
    print(nickNames)
    print(nickNames["William"])

# ### Problem 4:
# Create an array of 5 numbers. <strong>Using a loop</strong>,
# print the elements in the array reverse order.
# <strong>Do not use a function</strong>

def problem4():
    array = [1, 2, 3, 4, 5]
    for num in range(4, -1, -1):
        # num -= 1
        print(array[num])


# ### Problem 5:
# Create a function that will have a hard coded array then ask the user for a number.
# Use the userInput to state how many numbers in an array are higher, lower, or equal to it.

def problem5():
    array = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 40, 30, 20, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    userInput = int(input("Enter a number"))

    higher = 0
    equal = 0
    lower = 0

    for x in array:
        if(x > userInput):
            higher += 1
        elif(x == userInput):
            equal += 1
        elif(x < userInput):
            lower += 1

    print(f"{higher}, {lower}, {equal}")





if __name__ == '__main__':
    main()