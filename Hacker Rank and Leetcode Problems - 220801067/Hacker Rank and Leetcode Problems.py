'''Hacker Rank problem Number 1 :https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/count-elements-greater-than-previous-average/problem?isFullScreen=true'''
#Solution:
def countResponseTimeRegressions(responseTimes):
    n = len(responseTimes)
    if n<=1:
        return 0
    c=0
    currentSum=responseTimes[0]
    for i in range(1,n):
        prev_average = currentSum / i
        if responseTimes[i]>prev_average:
            c=c+1
        currentSum =currentSum+responseTimes[i]
    return c

'''Hacker Rank problem Number 2 : https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/find-smallest-missing-positive-integer/problem?isFullScreen=true'''
#Solution

def findSmallestMissingPositive(orderNumbers):
    n=len(orderNumbers)
    for i in range(n):
        while 1<= orderNumbers[i]<=n and orderNumbers[orderNumbers[i]-1] != orderNumbers[i]:
            orderNumbers[orderNumbers[i]-1],orderNumbers[i]=orderNumbers[i],orderNumbers[orderNumbers[i]-1]
    for i in range(n): 
        if orderNumbers[i] !=i+1:
            return i+1
    return n+1
