def solution(participant, completion):
    dicts = {}
    for i in participant:
        if i in dicts:
            dicts[i] += 1
        else:
            dicts[i] = 1
    for j in completion:
        dicts[j] -= 1

    drop_out = {v:k for k,v in dicts.items()}
    result = drop_out.get(1)
    return result