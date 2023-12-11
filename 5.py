'''
Mean, Median and Mode are the fundamentals of statistics used in almost 
every domain where we deal with numbers.
'''

list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

#mean
mean = sum(list1) / len(list1)

#median
list1.sort()
median = list1[len(list1)//2] if len(list1) % 2 == 1 \
            else (list1[len(list1)//2-1] + list1[len(list1)//2]) / 2

#Mode
import collections
c = collections.Counter(list1)
frequent = max(c.values())
for key, val in c.items():
    if val == frequent:
        mode = key

print('mean = ', mean)
print('median = ', median)
print('mode = ', mode)
