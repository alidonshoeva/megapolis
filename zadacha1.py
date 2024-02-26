import csv
with open("space.txt","r",encoding="utf8") as f:
    reader=list(csv.DictReader(f,delimitor="*", quotechar='"' ))
    for row in reader:

    if coord_place[0]==0 and coord_place[1]==0:
        n=ShipName[0]
        m=ShipName[1]
        xd=direction[0]
        yd=direction[1]
        t=len(planet)
        if n    >5:
            x=n+xd
            if m>3:
                y=m+t+yd
            else: y=-(n+yd)*m
        elif n<=5:
            x=-(n+xd)*4+t
            if m > 3:
                y = m + t + yd
            else:
                y = -(n + yd) * m
    print(xd,yd)

