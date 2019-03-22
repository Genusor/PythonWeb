import pandas
data = pandas.read_csv("m5-buckwheat.csv")
s = data["Крупа манная, кг"]
print(s.mean() )