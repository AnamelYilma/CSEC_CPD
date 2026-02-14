n = int(input())
g = [input().strip() for _ in range(n)]
MOD = 10**9+7
ans = 0
for i in range(n):
    for j in range(n):
        v = int(g[i][j])
        if v == 0:
            candidate = 0
        else:
            candidate = v
            d = 1
            prod = v
            while True:
                coords = [(i-d, j-d), (i-d, j+d), (i+d, j-d), (i+d, j+d)]
                if any(r < 0 or r >= n or c < 0 or c >= n for r, c in coords):
                    break
                vals = [int(g[r][c]) for r, c in coords]
                if 0 in vals:
                    break
                prod *= vals[0] * vals[1] * vals[2] * vals[3]
                if prod > candidate:
                    candidate = prod
                d += 1
            prod = v
            d = 1
            while True:
                coords = [(i-d, j), (i+d, j), (i, j-d), (i, j+d)]
                if any(r < 0 or r >= n or c < 0 or c >= n for r, c in coords):
                    break
                vals = [int(g[r][c]) for r, c in coords]
                if 0 in vals:
                    break
                prod *= vals[0] * vals[1] * vals[2] * vals[3]
                if prod > candidate:
                    candidate = prod
                d += 1
        if candidate > ans:
            ans = candidate
print(ans % MOD)
