n, h, k = map(int, input().split())
a = list(map(int, input().split()))
cur = 0
ans = 0
i = 0
while i < n:
    while i < n and cur + a[i] <= h:
        cur += a[i]
        i += 1
    ans += 1
    cur = max(0, cur - k)
ans += (cur + k - 1) // k
print(ans)
