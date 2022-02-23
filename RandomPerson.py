import random
import csv


class RandomPerson:
    def __init__(self):
        self.fnames_m = self._openAndStrip("fname_m.txt")
        self.fanams_f = self._openAndStrip("fname_f.txt")
        self.lnames = self._openAndStrip("lname.txt")
        self.domains = self._openAndStrip("email.txt")

    def _openAndStrip(self,in_file):
        with open(in_file,"r") as f:
            tmp_list = f.readlines()
            tmp_list = [line.rstrip('\n') for line in tmp_list]
            return tmp_list

    def getRandomPhone(self,min=1111111111,max=9999999999):
        number = random.randint(min,max)
        str_num = str(number)
        str_num = str_num[0:3] + "-" + str_num[3:6] + "-" + str_num[7:]
        return str_num

    def getFirstName(self):
        return random.choice(self.fnames_m)

    def getLastName(self):
        return random.choice(self.lnames)

    def getEmail(self,fname="",lname="",seperator="."):
        fname = self.getFirstName() if fname == "" else fname
        lname = self.getLastName() if lname == "" else lname
        return fname + seperator + lname + "@" + random.choice(self.domains)

    def getFullUserObj(self):
            user_fname = self.getFirstName()
            user_lname = self.getLastName()
            user_email = self.getEmail(user_fname,user_lname)
            user_phone = self.getRandomPhone()
            rtn_obj = {
                "first_name" : user_fname,
                "last_name" : user_lname,
                "email" : user_email,
                "phone" : user_phone
            }
            return rtn_obj

    def getFullUserList(self):
            user_fname = self.getFirstName()
            user_lname = self.getLastName()
            user_email = self.getEmail(user_fname,user_lname)
            user_phone = self.getRandomPhone()
            return [user_fname,user_lname,user_email,user_phone]

    def makeRandomUserCSV(self,rows=10):
        row_data = [["first_name","last_name","email","phone"]]
        for index in range(rows):
            row_data.append(self.getFullUserList())
        
        with open('random_data.csv','w',encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerows(row_data)

        return row_data