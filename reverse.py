n = input()

arr = [str(x) for x in n]

if arr[0] == "-":
    first = arr[0] #to seperate negative sign and merge it again after reversing the rest of the digits
    rest = arr[1:]

    rest.reverse()

    total = [first] + rest

else:
    arr.reverse()
    total = arr



merge = ""

for i in total:
    merge = "".join(total)
        
    int_merge = int(merge)


print(int_merge)
