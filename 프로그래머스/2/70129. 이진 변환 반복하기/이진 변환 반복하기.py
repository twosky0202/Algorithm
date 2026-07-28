def solution(s):
    answer = []
    count = 0
    zero_count = 0
    while s != "1":
        print(s)
        count += 1
        zero_count += s.count("0")
        value = len(s.replace("0", ""))
        s = str(format(value, 'b'))
    answer.append(count)
    answer.append(zero_count)
    return answer