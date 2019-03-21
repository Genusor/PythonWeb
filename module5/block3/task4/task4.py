sum=0
with open ("m5-calibration.dat", encoding="utf-8") as f:
    for line in f:
        line=line.strip()
        if line[0]=="-":
            sum-=int(line[1:])
        else:
            sum+=int(line[1:])
    print(sum)
