def solution(s):
    answer = True
    pCount = 0
    yCount = 0
    for i in range(len(s)):
        if(s[i]=='p' or s[i]=='P'):
            pCount += 1
        elif(s[i]=='y' or s[i]=='Y'):
            yCount += 1
    
    if(pCount == yCount):
        answer = True
    elif(pCount != yCount):
        answer = False
    elif(pCount == 0 and yCount == 0):
        answer = True

    return answer