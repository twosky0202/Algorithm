def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if '0' <= i <= '9':
                answer = True
            else:
                answer = False
                break
    else:
        answer = False

    
    return answer