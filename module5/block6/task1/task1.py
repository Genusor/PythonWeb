
import pandas
data = pandas.read_csv("m5-access-log-all.csv")

# ip самого часто встречаемого
ip = data["ip"].value_counts().keys()[0]

# количество в таблице
count = data["ip"].value_counts()[0]

# процент вклада ip
fraction = count/len(data)*100

# номер последней записи
last = data[data["ip"]==ip][["timestamp","user-agent"]][-1:]

suspicious_agent = {}

suspicious_agent["ip"] = ip
suspicious_agent["fraction"] = fraction
suspicious_agent["count"] = count
suspicious_agent["last"] = {"agent": last.values[0][1], "timestamp": last.values[0][0]}

print(suspicious_agent)
