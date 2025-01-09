with open ("data.txt") as f:
    lines = f.readlines()
for line in lines:
    print(line)


with open ("data.txt", "a") as f:
    lines = f.write("Eve, 35\n")

with open ("data.txt", "r") as f:
    lines = f.readlines()
for line in lines:
    print(line)