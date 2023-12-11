'''
Anagrams are words formed by rearranging the letters of another word.
For example, car and arc, cat and act, etc.
'''
from collections import defaultdict

def group_anagrams(a):
    dfdict = defaultdict(list)
    for i in a:
        anagram = ''.join(sorted(i))
        dfdict[anagram].append(i)
    return dfdict.values()

words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))