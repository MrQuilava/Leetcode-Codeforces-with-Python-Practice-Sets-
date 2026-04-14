
results = []

size = int(input())

for i in range(size):
    nums = input().split()

    a, b, c = nums

    results.append((a, b, c))

    
for item in results:   
    if (a == b and a != c) or (b == a and b != c):
        print(c)
    elif (c == a and c != b) or (a == c and a != b):
        print(b)
    elif (c == b and c != a) or (b == c and b != a):
        print(a)
    else:
        print()
