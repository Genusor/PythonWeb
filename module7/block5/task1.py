def file_Parse(file):
    base=[]
    with open(file) as fp:
        for line in fp:
            line=line.split(' :: ')
            if len(line)>1:
                coordinates=line[1].split(',')
                x,y=line[2].split('x')
                x=int(x)
                y=int(y)
                if x>y:
                    elongation=x/y
                else:
                    elongation=y/x
                base.append({
                    "id":line[0],
                    "coordinates": coordinates,
                    "size": [x,y],
                    "area": x*y,
                    "elongation": elongation,
                })
        return base 

f1=file_Parse("m7-map-1.txt")
f2=file_Parse("m7-map-2.txt")
f=f1+f2

val=[]
val1=[]

for s1 in f:
    val.append(s1["area"])
    val1.append(s1['elongation'])
print("average area")
print(round(sum(val)/len(val)))

max_size=max(val)
max_elon=max(val1)
flag1=True
flag2=True
for s2 in f:
    if s2["area"]==max_size and flag1:
        print("id max area %s",max_size)
        print(s2["id"][3:])
        flag1=False
    if s2['elongation']==max_elon and flag2:
        print("id max elongation %s", max_elon)
        print(s2["id"][3:])
        flag2=False

#TODO:
#можно было так, но я дебил
# base={
#                     "id": [],
#                     "coordinates": [],
#                     "size": [],
#                     "area": [],
#                     "elongation": [],
# }
# base1["id"].append(1)
# base1["id"].append(2)
# print(base1["id"])
