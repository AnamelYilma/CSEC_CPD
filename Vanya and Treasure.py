import sys
input = sys.stdin.readline

n, m, p = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

pos = [[] for _ in range(p+1)]
for i in range(n):
    for j in range(m):
        pos[grid[i][j]].append((i, j))

dp = []
for i, (r, c) in enumerate(pos[1]):
    dp.append(r + c)

for t in range(2, p+1):
    curr = []
    if len(dp) > len(pos[t]):
        for r2, c2 in pos[t]:
            best = 10**9
            for idx, (r1, c1) in enumerate(pos[t-1]):
                d = dp[idx] + abs(r1 - r2) + abs(c1 - c2)
                if d < best:
                    best = d
            curr.append(best)
    else:
        for r2, c2 in pos[t]:
            best = 10**9
            for idx, (r1, c1) in enumerate(pos[t-1]):
                d = dp[idx] + abs(r1 - r2) + abs(c1 - c2)
                if d < best:
                    best = d
            curr.append(best)
    dp = curr

print(min(dp))
