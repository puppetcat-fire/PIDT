import numpy as np
import random
import copy
import matplotlib.pyplot as plt
length = 4
width = 4
cell = np.zeros((length,width),int)
cell_temp = copy.deepcopy(cell)
for i in range(0,length):
    for j in range(0,width):
        cell_temp[i][j] = random.randint(0,1)
#当所有细胞状态不变时结束
#可能存在棋盘一直周期性变化，此时如果需要结束可手动结束
cc = 0
with open("out.txt","w") as f:
    while not(cell_temp==cell).all() and cc<100:
        cc += 1
        for i in cell:
            for j in i:
                f.write("{}".format(j))
        f.write('''
''')
        #通过读取cell矩阵，不断判断每一个单元格是存活还是死亡，将判断结果保存在cell_temp中，最终再复制给cell矩阵
        cell = copy.deepcopy(cell_temp)
        #显示每一轮的图像
        plt.imshow(cell)
        plt.pause(0.2)
        #两重循环遍历整个矩阵，判断每个细胞下一个状态是生存还是死亡
        for i in range(0,length):
            for j in range(0,width):
                '''
                count保存一个细胞周围8个方格内有几个存活的细胞，注意这两将上下边界和左右边界连接起来进行判断，
                如对于8*8的棋盘,[0,0]与[0,7]和[7,0]在逻辑上相邻
                '''
                count = cell[(i-1)%length][j] + cell[(i+1)%length][j] + cell[i][(j-1)%width] + cell[i][(j+1)%width] + cell[(i+1)%length][(j+1)%width] + cell[(i-1)%length][(j+1)%width] + cell[(i+1)%length][(j-1)%width] + cell[(i-1)%length][(j-1)%width]
                #如果一个单元格是死亡，且周围是三个单元格则存活，否则保持死亡
                if(cell[i][j] == 0 and count != 3):
                    continue
                if(cell[i][j] == 0 and count == 3):
                    cell_temp[i][j] = 1
                    continue
                #如果一个存活的单元格周围有2或3个单元格存活则该单元格继续存活，否则死亡
                if(count == 2 or count ==3):
                    continue
                cell_temp[i][j] = 0