''' DAY 1 : Hands on- Lab exercises
PROBLEM 1 : Count occurrences of a substring allowing overlaps.'''
#Solution:

a=input("String: ")
b=input("Substring: ")
c=0 #count
for i in range(len(a)-len(b)+1):
    if a[i:i+len(b)]==b:
        c=c+1
print("Number of occurences of substring in the string : ",c)

''' RESULT:
String: banana
Substring: an
Number of occurences of substring in the string :  2 '''

#PROBLEM 2 : Implement division that returns "NaN" if denominator is zero.
#Solution:


a=int(input("enter numerator: ")) 
b=int(input("enter denominator : ")) 
if b==0:
    print("NaN")
else:
    print("Ans: ",a/b)
    
'''Result: 
enter numerator: 12
enter denominator : 0
NaN '''
#PROBLEM 3 : Given income, credit_score, and existing_debt, determine "Eligible", "Review", or "Reject" using sensible thresholds.
# thresholds : income must be >=60k , credit score >=730 and debt <=22k
#Solution:

income=int(input("income: "))
credit=int(input("credit score :"))
debt=int(input("existing debt :"))
if (income>=60000 and credit>=730 and debt<=22000 ):
    print("Eligible")
elif (40000 <= income < 60000 and credit >= 650 and debt <= 45000):
    print("Review")
else:
    print("reject")
    
'''Result :
income: 50000
credit score :740
existing debt :21000
Review '''

#PROBLEM 4 : Receive an amount, apply discount: <1000 → 0%, 1000–4999 → 5%, >=5000 → 10%. Return final payable.
#Solution:

amount=float(input("Enter the amount :"))
if amount<1000:
    discount=0
elif 1000<= amount < 4999:
    discount =0.05
else:
    discount=0.10
discount_price= discount*amount
payable_price = amount- discount_price
print("Final payable amount : ", payable_price )

'''Result:
Enter the amount :6000
Final payable amount :  5400.0'''

#PROBLEM 5 : Convert a sentence to title case but keep known abbreviations (e.g., AI, ML) uppercase.
#solution:

sentence =input("Enter sentence :")
abbreviations ={"AI","ML","API"}
words=sentence.split()
results=[]
for i in words:
    if i.upper() in abbreviations:
        results.append(i.upper())
    else:
        results.append(i.capitalize())
final= " ".join(results)
print(final)

'''Results:
Enter sentence :I love working with  ai and ml 
I Love Working With AI And ML'''

#PROBLEM 6 : Replace all digits in a string with #.
#solution:

sentence=str(input())
result=""
for i in sentence:
    if i.isdigit():
        result=result+"#"
    else:
        result=result+i
print(result)

'''REsult:
he77oo
he##oo '''

#PROBLEM 7 : Return squares of even numbers or cubes when odd numbers
#solution:
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
result = []
for num in numbers:
    if num % 2 == 0:     
        result.append(num ** 2)
    else:                
        result.append(num ** 3)

print("Result:", result)

'''result:
Enter numbers separated by space: 2 3 4 5 6 7 8 9 
Result: [4, 27, 16, 125, 36, 343, 64, 729] '''

#PROBLEM 8 : Password Check with Limited Attempts
#solution:
correct_password = str(input("Enter password: "))
attempts = 3

while attempts > 0:
    password = input("Enter password: ")
    
    if password == correct_password:
        print("Login Successful")
        break
    else:
        attempts -= 1
        print("Wrong password! attempts left:",attempts)

if attempts == 0:
    print("Account Locked")

'''result:
Enter password: abcdefgh
Enter password: abcdef
Wrong password! attempts left: 2
Enter password: vuts
Wrong password! attempts left: 1
Enter password: abcdefgh
Login Successful
'''

#PROBLEM 9 : Multiplication Table (1..N) 
#solution:

n = int(input("Enter number: "))
m = int(input("Enter limit: "))

for i in range(1, m + 1):
    print(n, "x", i, "=", n * i)
    
'''result:
Enter number: 5
Enter limit: 7
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
'''