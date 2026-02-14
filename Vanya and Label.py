s = input().strip()
MOD = 10**9 + 7
ans = 1
for c in s:
    if '0' <= c <= '9':
        d = ord(c) - ord('0')
    elif 'A' <= c <= 'Z':
        d = 10 + ord(c) - ord('A')
    elif 'a' <= c <= 'z':
        d = 36 + ord(c) - ord('a')
    elif c == '-':
        d = 62
    else:
        d = 63
    zeros = 6 - bin(d).count('1')
    ans = (ans * (3 ** zeros)) % MOD
print(ans)
