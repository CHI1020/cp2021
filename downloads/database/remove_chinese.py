import hanzidentifier

with open("wed.txt", "r", encoding="utf-8") as f:
    data = f.readlines()

all = ""
for line in data:
    if not hanzidentifier.has_chinese(line):
        all += line
    
print(all)

