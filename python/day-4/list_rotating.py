data = list([i for i in range(4)] for r in range(4))



for row in data:
    print(row)
print("---------------")


for r_index,row in enumerate(data):
    print(row)
    for c_index in range(r_index,len(row)):
        tmp = data[c_index][r_index]
        data[c_index][r_index] = row[c_index]
        data[r_index][c_index] = tmp
    print("-----------------")
    for r in data : print(r)