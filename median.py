l1 = input()
l2 = input()

total = l1 + l2

arr = [int(x) for x in total]

n = len(arr)

if n % 2 == 0:
    n1 = arr[n // 2 - 1]
    n2 = arr[n // 2]
    
    result = (n1 / n2)
    
    print(result)
else:
    result = arr[n // 2] #floor division (//) - to get the middle index
    print(result)
