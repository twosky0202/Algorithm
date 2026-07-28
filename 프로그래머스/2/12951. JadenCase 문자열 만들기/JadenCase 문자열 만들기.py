def solution(s):
    answer = []
    str = s.split(" ")
    for i in str:
        if i == "":
            answer.append("")
        else:
            answer.append(i.capitalize())
    answer = " ".join(answer)
    return answer