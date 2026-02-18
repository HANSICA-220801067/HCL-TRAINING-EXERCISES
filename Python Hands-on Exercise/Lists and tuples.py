''' DAY 12 : Hands on- Lab exercises
PROBLEM 1 : From a list, remove duplicates while keeping the last occurrence of each element.'''
#Solution:

l=list(map(int, input().split()))
result=[]
for i in l:
    if i in result:
        result.remove(i)
    result.append(i)
print(result)

''' Output:
1 2 3 5 3 6 9 4 9 7 8
[1, 2, 5, 3, 6, 4, 9, 7, 8] '''

#PROBLEM 2 : Convert [a,b,c,d,e] to [(a,b),(c,d)] and ignore the last if odd length. Use Tuple List.
#Solution:

l=list(map(str, input().split()))
if len(l)%2 !=0:
    l.pop()
result=[]
for i in range(0,len(l),2):
    result.append((l[i],l[i+1]))
print(result)

'''Output:
1 2 3 4 5 6 7 8 9
[(1, 2), (3, 4), (5, 6), (7, 8)] ''' 


#PROBLEM 3 : Return the index of the second largest distinct element; if not exists, return -1.
#Solution:
l = list(map(int, input().split()))
u = list(set(l))
if len(unique) < 2:
    print(-1)
else:
    u.remove(max(u))
    second = max(unique)
    print(l.index(second))

'''Output:
1 2 58 6 4 3 88 
2'''

#PROBLEM 4 : Rotate List Right by K (No Slicing)
#Solution:

l= list(map(int, input().split()))
k=int(input())
n=len(l)
k=k%n
for i in range(k):
    last=l.pop()
    l.insert(0,last)
print(l)

'''output:
12 13 14 15 16 17
3
[15, 16, 17, 12, 13, 14]'''

#PROBLEM 5 : Interleave two lists element-wise, stopping when one ends.
#Solution:
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
result = []
for i in range(min(len(l1), len(l2))):
    result.append(l1[i])
    result.append(l2[i])
print(result)

'''output:
4 5 
1 2 3 8 9 
[4, 1, 5, 2]'''

#PROBLEM 6 : Compute cumulative sum; stop when a negative number is encountered.
#Solution:
l = list(map(int, input().split()))
total = 0
for i in l:
    if i < 0:
        break
    total += i
print(total)

'''output:
1 2 3 -1 4 5 -2
6'''

#PROBLEM 7 : Return squares of even numbers from a list.
#solution:
l = list(map(int, input().split()))
result = []
for i in l:
    if i % 2 == 0:
        result.append(i * i)
print(result)

'''output:
1 3 4 6 2 8 
[16, 36, 4, 64]'''

#PROBLEM 8 : Password Check- Allow up to 3 attempts; on success return "Unlocked" else "Locked".
#solution:
pw = input()
count = 0
while count < 3:
    attempt = input()
    if attempt == pw:
        print("Unlocked")
        break
    count += 1
if count == 3:
    print("Locked")
    
'''output:
ghjk
asa
dwa
asdw
Locked'''

#PROBLEM 8 : rack running maximum; reset to 0 when value ≤ 0. Output list of running max values.
#solution: 
l = list(map(int,input().split()))
result = []
high = 0
for i in l:
    if i <= 0:
        high = 0
    else:
        high = max(high, i)
    result.append(high)
print(result)
'''output:
1 2 5 5 0 3 -2 7
[1, 2, 5, 5, 0, 3, 0, 7]'''
