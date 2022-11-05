def solution(survey, choices):
    choices = [x - 4 for x in choices]
    result = {
        ('R', 'T'): 0,
        ('C', 'F'): 0,
        ('J', 'M'): 0,
        ('A', 'N'): 0,
    }
    for s, c in zip(survey, choices):
        for k in result.keys():
            if s[0] in k:
                rev = 1 if s[1] > s[0] else -1
                result[k] += c * rev
    answer = ''.join([k[0] if v <= 0 else k[1] for k, v in result.items()])
    return answer
