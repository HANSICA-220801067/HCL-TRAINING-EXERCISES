#1. Given text, return sorted unique words ignoring case.
#Solution:
text = (input().lower().split())
words=sorted(set(text))
print(words)
#Result:
'''good morning  good night good evening
['evening', 'good', 'morning', 'night'] '''

#2. Merge two inventory dicts by summing quantities of same keys.
#Solution:
dict1 =eval(input())
dict2 =eval(input())
for key in dict2:
  if key in dict1:
    dict1[key]=dict1[key]+dict2[key]
  else:
    dict1[key]=dict2[key]
print(dict1)
#Result:
'''{"apple":5,"banana":4,"grapes":3}
{"apple":5,"banana":4,"tea":6}
{'apple': 10, 'banana': 8, 'grapes': 3, 'tea': 6}'''

#3. Given a dict and target value, return all keys with that value
#Solution:
d = eval(input())
target = int(input())
result = []
for key in d:
    if d[key] == target:
        result.append(key)
print(result)
#RESULT:
'''{"fig":3,"table":4}
3
['fig']'''

#4. Remove duplicates (order NOT important)
#Solution:
lst = list(map(int, input().split()))
print(list(set(lst)))
#RESULT:
'''1 2 2 2 3 5 3 6 4 6 
[1, 2, 3, 4, 5, 6]'''
