import json
with open("m5-access-log-100.json") as fp:
    data = json.load(fp)

freq_dict = {}
for record in data:
    ip = record["ip"] 
    if ip in freq_dict:
        freq_dict[ip] = freq_dict[ip] + 1
    else: freq_dict[ip] = 1

count=0
for ip in freq_dict:
    if freq_dict[ip]==1:
        count+=1

print(count)