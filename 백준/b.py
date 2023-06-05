N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
A.sort()

for i in B: #i는 B배열의 첫번째 값부터 하나씩 빼옴
    low = 0 #시작값
    high = len(A) - 1 #끝값
    found = False  # 원소를 찾았는지 여부
    while low <= high: #시작값이 끝값을 넘기면 종료
        mid = (low + high) // 2 #중간값
        if A[mid] == i: #배열에서 같은수를 찾았을 때
            found = True #찾았으므로 참
            break #종료
        if A[mid] < i: #찾은값이 현재값보다 낮을때
            low = mid + 1 #시작값을 중앙 값으로
        else: #찾은값이 현재값보다 높을때
            high = mid - 1 #끝값을 중앙 값으로
    if found: #찾았는지 여부
        print("1")
    else:
        print("0")
