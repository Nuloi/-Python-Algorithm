N=int(input())
budget=list(map(int,input().split()))
budget.sort()
total_budget = int(input())

low=0
high=budget[-1]
while low <= higt:
    mid = (low + higt) // 2

    requests = [min(request, mid) for request in budget]
    total = sum(requests)

    if total <= total_budget:
            low = mid + 1
    else:
        higt = mid - 1

print(higt)