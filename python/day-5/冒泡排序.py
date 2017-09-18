


#将一个不规则的数组按从小到大的顺序进行排序

data = [10,4,33,21,54,8,25,11,5,22,2,1,17,13,6]

count = 0
for j in range(1,len(data)):
    count += 1
    for i in range(len(data)-j):
        count += 1
        if data[i] > data[i+1]:
            count += 1
            tmp = data[i+1]
            data[i+1] = data[i]
            data[i]= tmp




print(count,data)