def solution(participant, completion):
    hash_map = {}

    # 참가자 카운트
    for p in participant:
        if p in hash_map:
            hash_map[p] += 1
        else:
            hash_map[p] = 1

    # 완주자 카운트 감소
    for c in completion:
        hash_map[c] -= 1

    # 값이 1 남은 사람이 완주 못한 사람
    for key in hash_map:
        if hash_map[key] > 0:
            return key