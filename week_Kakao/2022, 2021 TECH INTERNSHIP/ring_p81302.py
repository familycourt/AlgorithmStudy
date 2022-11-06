def solution(places):
    answer = []
    
    for place in places :
        answer.append(checkPlace(place))
    
    return answer

def checkPlace(place) :
    plist = []
    for str in place :
        plist.append(list(str))
        
    for i in range(5) :
        for j in range(5) :
            if plist[i][j] == 'P' :
                if (checkPeople(plist, i, j) == -1) :
                    return 0
    return 1

def checkPeople(plist, i, j) :
    if i-1 >= 0 :
        if plist[i-1][j] == 'P' :
            return -1
        if j-1 >= 0 :
            if plist[i-1][j-1] == 'P' :
                if plist[i-1][j] != 'X' or plist[i][j-1] != 'X' :
                    return -1
        if j+1 <= 4 :
            if plist[i-1][j+1] == 'P' :
                if plist[i-1][j] != 'X' or plist[i][j+1] != 'X' :
                    return -1
    if j-1 >= 0 :
        if plist[i][j-1] == 'P' :
            return -1
    if i+1 <= 4 :
        if plist[i+1][j] == 'P' :
            return -1
        if j-1 >= 0 :
            if plist[i+1][j-1] == 'P' :
                if plist[i+1][j] != 'X' or plist[i][j-1] != 'X' :
                    return -1
        if j+1 <= 4 :
            if plist[i+1][j+1] == 'P' :
                if plist[i+1][j] != 'X' or plist[i][j+1] != 'X' :
                    return -1
    if j+1 <= 4 :
        if plist[i][j+1] == 'P' :
            return -1

    if i-2 >= 0 :
        if plist[i-2][j] == 'P' and plist[i-1][j] != 'X' :
            return -1
    if j-2 >= 0 :
        if plist[i][j-2] == 'P' and plist[i][j-1] != 'X' :
            return -1
    if i+2 <= 4 :
        if plist[i+2][j] == 'P' and plist[i+1][j] != 'X' :
            return -1
    if j+2 <= 4 :
        if plist[i][j+2] == 'P' and plist[i][j+1] != 'X' :
            return -1
    
    return 1
        
    