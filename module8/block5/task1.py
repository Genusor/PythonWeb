from collections import Counter

# data = [2, 4, 2, 2, 4, 6, 2, 4, 6, 7, 15, 2, 8]
# c = Counter(data)
# print(c.most_common())
# print("Two most common entries:")
# for entry, count in c.most_common(2):
# 	print(f" {entry} (met {count} times)")

# data = "aosneuhaoseuahonusaohuno"
# c = Counter(data)
# print(c.most_common())
# print("Two most common entries:")
# for entry, count in c.most_common(2):
# 	print(f" {entry} (met {count} times)")

# c = Counter()
# c.update("aosneuhaoseuahonusaohuno")
# c.update("aaaaaaaaaaaaaa")
# print(c.most_common(3))

c = Counter()
with open("m8-sirotlivo.txt", "r", encoding='utf-8') as fp:
    for line in fp:
        c.update(line.upper().split(" "))
        
print(c["КОУЛМЕН."])