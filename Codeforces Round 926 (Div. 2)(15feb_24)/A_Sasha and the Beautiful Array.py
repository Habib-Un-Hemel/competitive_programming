x = int(input())  
for i in range(x):
    n = int(input()) 
    arr = list(map(int, input().split()))  
    maxx = max(arr)
    minn = min(arr)
    max_b = maxx - minn   
    print(max_b)