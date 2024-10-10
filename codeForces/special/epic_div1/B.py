
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("Bob" if a == b or a == b[::-1] else "Alice")