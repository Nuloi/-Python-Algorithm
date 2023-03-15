for _ in range(int(input())):
    l, v1, v2, t, s = map(int, input().split())
    
    # 최소 확인 횟수 계산
    # t+s 시간동안 l 거리를 달리는 경우
    total_time = (l / v1) + t + (l / v2)
    # 확인을 해야 하는 횟수
    check_count = 0
    for i in range(int(total_time // (2*t))):
        check_count += 1
        # 확인 시간
        check_time = i*2*t + t
        # 유라가 해당 지점에 도착할 수 있는 시간
        arrive_time = (l / v1) + check_time + (l / v2)
        # 확인할 수 있는 범위
        check_range = arrive_time * v1 - (check_time * v1 + s*v1)
        if check_range >= l:
            break
    else:
        check_count = "impossible"
        
    print(check_count)
