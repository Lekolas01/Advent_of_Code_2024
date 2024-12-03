def split_line(y):
    s = 0
    while not (y[s] == " "):
        s = s + 1
    a = int(y[0:s])
    while y[s] == " ":
        s = s + 1
    b = int(y[s:])
    return a, b


def filllist(file):
    list1 = []
    list2 = []

    row = file.readline()

    while row != "":
        a, b = split_line(row)
        list1.append(a)
        list2.append(b)
        row = file.readline()

    list1 = sorted(list1)
    list2 = sorted(list2)
    return list1, list2


file = open("data_day1.txt", "r")
list1, list2 = filllist(file)

simi = 0
for erst in list1:
    mult = 0
    for zweit in list2:
        if erst == zweit:
            mult = mult + 1
    simi = simi + erst * mult

print(f"similarity score {simi}")


x = 0
i = 0
while i < len(list1):
    x = x + abs(list1[i] - list2[i])
    i = i + 1

print(f"total distance is {x}")
