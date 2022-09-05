# 솔직히 .. 이런문제는 안풀어봐도 될듯 ㅎ ㅋㅋ

import sys
input = sys.stdin.readline

def professor(x: int, y : int) :
    if y == 0 :
        str = '____'*x
        print(str + "\"재귀함수가 뭔가요?\"")
        print(str + "\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        print(str + "라고 답변하였지.")
    else :
        str = '____'*(x-y)
        print(str+"\"재귀함수가 뭔가요?\"")
        print(str+"\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
        print(str+"마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        print(str+"그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
        professor(x, y-1)
        print(str+"라고 답변하였지.")

N = int(input().strip())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
professor(N, N)