if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    x=list(set(arr))
    x.sort(reverse=True)
    print(x[1])
