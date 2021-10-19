with open("cp2021_1b_w1.txt", "r", encoding="utf-8") as f:
    data = f.readlines()

stu = {}

for i in data[1:]:
    data = i.split("\t")
    stu_num = data[0]
    if data[1] == "":
        stu_account = stu_num
    else:
        stu_account = data[1]
        
    stu[stu_num] = stu_account
    #print(stu_num, stu_account)

print(stu["41023237"])
