def solution(d, budget):
    answer = 0
    d.sort()
    
    sum = 0
    for i in d:
        if sum + i <= budget:
            sum += i
            answer += 1
        else:
            break
            
    return answer
