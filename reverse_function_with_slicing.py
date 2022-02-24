''' Mike Sword -- 02/22/2022 '''
#funtion to reverse a list using slicing instead of the built-in reverse() function.

def reverseList(inputList):

   reversedList = inputList[::-1]

   return reversedList

inputList = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Indigo", "Violet"]

print("The original list is: ", inputList)

print("The list after reversal is: ", reverseList(inputList))