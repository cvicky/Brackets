def solution(S):
    #if given an empty string
    if len(S) == 0:
        return 0
        
    closedCount = 0
    openCount = 0
    
    #first pass, count total closed brackets
    for i in S:
        if i == ')':
            closedCount += 1
     
    #if not empty string and closedCount=0, then it's all open brackets, return 0
    if closedCount == 0 and len(S) != 0:
        return 0
      
    #second pass, count open brackets, stop when # of open brackets = # of closed brackets
    for index in range(0,len(S) ):
        if S[index] == '(':
            openCount += 1
        elif S[index] == ')': #decrement the closed bracket count remaining on the right half
            closedCount -= 1 
        if openCount == closedCount:
            break
    return index + 1  
