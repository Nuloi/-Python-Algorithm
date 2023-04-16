def bt(idx, n, ops, nums, res):
    if idx == n - 1:
        expr = ''
        for i in range(n - 1):
            expr += str(nums[i]) + ops[i]
        expr += str(nums[-1])

        if eval(expr.replace(' ', '')) == 0:
            res.append(expr)
        return

    for op in ['+', '-', ' ']:
        ops[idx] = op
        bt(idx + 1, n, ops, nums, res)

t = int(input())
cases = [int(input()) for _ in range(t)]
for c in range(t):
        n = cases[c]
        nums = list(range(1, n + 1))
        ops = [None] * (n - 1)
        res = []
        
        bt(0, n, ops, nums, res)
        res.sort()
        for expr in res:
            print(expr)
        
        if c != t - 1:
            print()
