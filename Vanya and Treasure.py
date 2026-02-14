import sys
input = sys.stdin.readline

n, m, p = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

pos = [[] for _ in range(p+1)]
for i in range(n):
    for j in range(m):
        typ = grid[i][j]
        pos[typ].append((i, j))

dist = [10**9] * len(pos[1])
for idx, (i, j) in enumerate(pos[1]):
    dist[idx] = i + j

for t in range(2, p+1):
    new_dist = [10**9] * len(pos[t])
    for i2, (r2, c2) in enumerate(pos[t]):
        for i1, (r1, c1) in enumerate(pos[t-1]):
            d = dist[i1] + abs(r1 - r2) + abs(c1 - c2)
            if d < new_dist[i2]:
                new_dist[i2] = d
    dist = new_dist

print(min(dist))
