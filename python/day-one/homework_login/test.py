error_counted = open("sam_passws_error.txt",'r')
f = error_counted.read().count("1")
print(type(f))


if 2<f:
    print("2<f")
else:
    print(12312)