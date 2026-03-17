if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    num = arr[-1]              # largest number
    rep = arr.count(num)      # how many times it appears
    
    result = arr[-(rep + 1)]  # second largest
    
    print(result)
