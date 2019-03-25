import pandas
data = pandas.read_json("m5-access-log-100.json")
s = data["ip"].value_counts()
# sum = s[object][0]+s[object][1]+s[object][2]
# print(sum)
print((s[0]+s[1]+s[2]))