test_cases = int(input())

for _ in range(test_cases):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))

    queue = [(i, p) for i, p in enumerate(priorities)]
    count = 0

    while True:
        current_doc = queue.pop(0)

        if any(current_doc[1] < q[1] for q in queue):
            queue.append(current_doc)
        else:
            count += 1
            if current_doc[0] == m:
                print(count)
                break