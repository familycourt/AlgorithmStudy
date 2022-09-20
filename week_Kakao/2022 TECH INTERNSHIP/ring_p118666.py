def solution(survey, choices):
    answer = ''
    dict= {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for i, ans in enumerate(survey) :
        if choices[i] > 4 :
            dict[ans[1]] += choices[i]-4
        elif choices[i] < 4 :
            dict[ans[0]] += 4-choices[i]
    
    if dict['R'] >= dict['T'] : answer+= 'R'
    else : answer+= 'T'
    if dict['C'] >= dict['F'] : answer+= 'C'
    else : answer+= 'F'
    if dict['J'] >= dict['M'] : answer+= 'J'
    else : answer+= 'M'
    if dict['A'] >= dict['N'] : answer+= 'A'
    else : answer+= 'N'
        
    return answer