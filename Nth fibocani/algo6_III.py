# O(n) time | O(1) Space

def getNthFib(n):
    lastTwo = [0,1]
    c = 3
    while c <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        c += 1
    return lastTwo[1] if n > 1 else  lastTwo[0]

print(getNthFib(6))