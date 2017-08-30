#!/usr/bin/evn python3

# f = open("test.log","a")
#
# f.write("6\n")
# f.write("7\n")
#



f = open("test.log","w+")
f.write("new line\n")
print("data:",f.read())




#print (f.read())


# for line in f:
# #    print("line")
#
#     if "3" in line:
#         print("this is the third line")
#     else:
#         print(line)
# # f.write("第一行\n")
# f.write("第2行\n")
# f.write("第3行\n")

f.close()