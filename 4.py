'''
Grouping elements of the same indices means grouping elements of two 
or more data structures according to their indices.

To group elements of the same index, you will initially have two or 
more lists inside a list like [[a, b], [c, d]]. To group the elements 
of these lists, you need to create two new lists where you will store 
the elements of both the lists at index 0 [a, c] and index 1 [b, d]. 
That is the meaning of grouping the elements of the same indices.
'''

inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
outputList = []

for i in range(len(inputLists[0])):
    outputList.append([inputLists[j][i] for j in range(len(inputLists))])

print(outputList)