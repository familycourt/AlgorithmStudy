def solution(s):
    answer = 0
    num_list = ["zero", "one", "two", "three", "four", 
                "five", "six", "seven", "eight", "nine"]
    
    while len(s) != 0 :
        if (s[0]>= '0' and s[0] <= '9') :
            answer *= 10
            answer += int(s[0])
            s = s[1:]
        else :
            for i, num in enumerate(num_list) :
                if (s.startswith(num)) :
                    answer *= 10
                    answer += i
                    s = s[len(num):]
                    break
            
    return answer