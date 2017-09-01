#!/usr/bin/evn python3



user_account = open("user_passwd1.txt",'r')

passwd= user_account.readlines()
print(passwd)
print(type(passwd))