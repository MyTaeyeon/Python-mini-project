'''
Find missing number:
Finding the missing number in an array means finding the numbers missing 
from the array according to the range of values inside the array. 
Most of the time, the question you get based on this problem is like:
    Given an array containing a range of numbers from 0 to n with a missing number, 
    find the missing number in the input array.
'''

def findMissingNumbers(a):
    numbers = set(a)
    output = []
    for i in range(1, a[-1]):
        if i not in numbers:
            output.append(i)
    return output

listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
print(findMissingNumbers(listOfNumbers))
