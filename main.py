from initJvm import initJVM

from te import te
from mi import mi
if __name__ == "__main__":
    datas = None
    with open("out2.txt") as f:
        datas = f.readlines()
    if datas:
        raws1 = []
        raws2 = []
        for data in datas:
            raws1.append(int(data[:16][6]))
            raws2.append(int(data[:16][8]))

        resMi = mi(raws1, raws2)
        print(resMi)    
        resTe = te(raws1, raws2)
        print(resTe)

        

