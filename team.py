n = int(input("problems: "))

tasks = 0

for i in range(n):
    Sets = input(f"problem set {[i]}:")

    a, b, c = Sets.split()

    if [a, b, c].count("1") >= 2:
        tasks += 1
    

print(tasks)
    