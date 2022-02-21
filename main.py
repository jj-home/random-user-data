#read neccessary files into arrays

import random
import csv

def openAndStrip(in_file):
    with open(in_file,"r") as f:
        tmp_list = f.readlines()
        tmp_list = [line.rstrip('\n') for line in tmp_list]
        return tmp_list

def randomPhone():
    number = random.randint(1111111111,9999999999)
    str_num = str(number)
    str_num = str_num[0:3] + "-" + str_num[3:6] + "-" + str_num[7:]
    return str_num

def getFirstName():
    return random.choice(fnames_m)

def getLastName():
    return random.choice(lnames)

def getEmail(fname,lname,seperator="."):
    return fname + seperator + lname + "@" + random.choice(domains)


fnames_m = openAndStrip("fname_m.txt")
fanams_f = openAndStrip("fname_f.txt")
lnames = openAndStrip("lname.txt")
domains = openAndStrip("email.txt")

headers = ["first_name","last_name","email","phone"]
data = []

rows = int(input("How many random users to generate? "))


for index in range(rows):
    user_fname = getFirstName() #random.choice(fnames_m)
    user_lname = getLastName() #random.choice(lnames)
    user_email = getEmail(user_fname,user_lname) #user_fname + "." + user_lname + "@" + random.choice(domains)
    user_phone = randomPhone()
    data.append([user_fname,user_lname,user_email,user_phone])
    
"""
usr_obj = {
    "first_name" : user_fname,
    "last_name" : user_lname,
    "email" : user_email,
    "phone" : user_phone
}

print(usr_obj)
"""

#print(data)

with open('random_data.csv','w',encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)




