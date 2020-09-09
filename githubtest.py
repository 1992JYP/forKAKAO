def solution(v):
    x = v[2][0] if v[1][0] == v[0][0] else (v[1][0] if v[2][0] == v[0][0] else v[0][0])
    y = v[2][1] if v[1][1] == v[0][1] else (v[1][1] if v[2][1] == v[0][1] else v[0][1])
    answer = [x,y]
	
	answer++

    return answer