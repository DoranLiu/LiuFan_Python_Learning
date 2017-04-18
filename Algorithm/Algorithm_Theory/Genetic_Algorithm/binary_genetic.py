from numpy import random
import numpy as np
import matplotlib.pyplot as plt
from math import pi,sin
import copy

class Gas():
    def __init__(self,popsize,chrosize,xrangemin,xrangemax):
        self.popsize =popsize  # 每代的个体数
        self.chrosize =chrosize  #变量编码长度
        self.xrangemin =xrangemin  # [xrangemin,xrangxmax] ：变量取值范围
        self.xrangemax =xrangemax
        self.crossrate =0.8  # 交叉率
        self.mutationrate =0.01  # 变异率
    # 初始化种群
    def initialpop(self):
        pop = random.randint(0,2,size =(self.popsize,self.chrosize))
        return pop

    # 对传入的每个变量，计算函数值
    def fun(self,x1):
        return x1*sin(10*pi*x1)+2.0

    # 由于我们所求的是最大值，所有可以用函数值代替适应度
    def get_fitness(self,x):       
        fitness = []
        for x1 in x:
           fitness.append(self.fun(x1))
        return fitness

    # 输入参数为上一代的种群，和上一代种群的适应度列表
    def selection(self,popsel,fitvalue):
        new_fitvalue = []
        totalfit = sum(fitvalue)
        accumulator = 0.0
        for val in fitvalue:
            # 对每一个适应度除以总适应度，然后累加，这样可以使适应度大对个体获得更大的比例空间
            new_val =(val*1.0/totalfit)            
            accumulator += new_val
            new_fitvalue.append(accumulator)            
        ms = []
        for i in range(self.popsize):
            # 随机生成0，1之间的随机数
            ms.append(random.random()) 
        ms.sort() # 对随机数进行排序
        fitin = 0
        newin = 0
        newpop = popsel
        while newin < self.popsize:
            # 随机投掷，选择落入个体所占轮盘空间的个体
            if(ms[newin] < new_fitvalue[fitin]):
                newpop[newin] = popsel[fitin]
                newin = newin + 1
            else:
                fitin = fitin + 1
        pop = newpop
        # 适应度大的个体会被选择的概率较大
        # 使得新种群中，会有重复的较优个体
        return pop
    
    def crossover(self,pop):
        for i in range(self.popsize-1):
            # 近邻个体交叉，若随机数小于交叉率
            if(random.random()<self.crossrate):
                # 随机选择交叉点
                singpoint =random.randint(0,self.chrosize)
                temp1 = []
                temp2 = []
                # 对个体进行切片，重组
                temp1.extend(pop[i][0:singpoint])
                temp1.extend(pop[i+1][singpoint:self.chrosize])
                temp2.extend(pop[i+1][0:singpoint])
                temp2.extend(pop[i][singpoint:self.chrosize])
                pop[i]=temp1
                pop[i+1]=temp2

        return pop
    
    def mutation(self,pop):
        for i in range(self.popsize):
            # 反转变异，随机数小于变异率，进行变异
            if (random.random()< self.mutationrate):
                mpoint = random.randint(0,self.chrosize-1)
                # 将随机点上的基因进行反转
                if(pop[i][mpoint]==1):
                    pop[i][mpoint] = 0
                else:
                    pop[mpoint] =1
        return pop

    def elitism(self,pop,popbest,nextbestfit,fitbest):
        # 输入参数为上一代最优个体，变异之后的种群，上一代的最优适应度，本代最优适应度。这些变量是在主函数中生成的。
        if nextbestfit-fitbest <0:
            # 满足精英策略后，找到最差个体的索引，进行替换
            pop_worst =nextfitvalue.index(min(nextfitvalue))
            pop[pop_worst] = popbest
        return pop          
    # 对十进制进行转换到求解空间中的数值
    def get_declist(self,chroms):
        step =(self.xrangemax - self.xrangemin)/float(2**self.chrosize-1)
        self.chroms_declist =[]
        for i in range(self.popsize):
            chrom_dec =self.xrangemin+step*self.chromtodec(chroms[i])  
            self.chroms_declist.append(chrom_dec)      
        return self.chroms_declist
    # 将二进制数转化为十进制
    def chromtodec(self,chrom):
        m = 1
        r = 0
        for i in range(self.chrosize):
            r = r + m * chrom[i]
            m = m * 2
        return r

if __name__ == '__main__':
    generation = 100   # 遗传代数
    mainGas =Gas(100,10,-1,2)
    pop =mainGas.initialpop()  # 种群初始化
    pop_best = [] # 每代最优个体
    #average = []
    for i in range(generation):
        # 在遗传代数内进行迭代
        declist =mainGas.get_declist(pop) # 解码
        fitvalue =mainGas.get_fitness(declist) # 适应度函数
        popbest = pop[fitvalue.index(max(fitvalue))] # 选择适应度函数最高个体
        popbest =copy.deepcopy(popbest) # 对popbest进行深复制，以为后面精英选择做准备。
        fitbest = max(fitvalue) # 最高适应度
        pop_best.append(fitbest) # 保存每代最高适应度值
        #average.append(sum(fitvalue)/len(fitvalue))       
        ################################
        mainGas.selection(pop,fitvalue)  # 进行算子操作，并不断更新pop
        mainGas.crossover(pop) # 交叉
        mainGas.mutation(pop)  # 变异
        ################################ 精英策略前的准备
        nextdeclist = mainGas.get_declist(pop)  # 对变异后的pop，求解最大适应度
        nextfitvalue =mainGas.get_fitness(nextdeclist)        
        nextbestfit = max(nextfitvalue) 
        ################################ 精英策略
        mainGas.elitism(pop,popbest,nextbestfit,fitbest)    # 比较深复制的个体适应度和变异之后的适应度
    print(max(pop_best))
    t = [x for x in range(generation)]
    s = pop_best
    plt.plot(t,s)
    plt.show()
    plt.close()