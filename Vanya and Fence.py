n, h = map(int, input().split())
a = list(map(int, input().split()))
tall = 0
for x in a:
    if x > h:
        tall += 1
print(n + tall)
