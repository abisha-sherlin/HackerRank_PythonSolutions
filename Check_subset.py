n = int(input())
for i in range(n):
    m = int(input())
    A = set(map(int, input().split()))
    k = int(input())
    B = set(map(int, input().split()))
    print(A.issubset(B))
