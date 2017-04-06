#在这门课程中，我们将介绍其中一种基于Hebb学习规则的方法——自联想存储器。自联想存储器是当一个已存储序列的片段，或者加上噪音的版本再次出现时，能够回忆起该序列原貌的存储器。它能够有效地降低输入的噪音，或移除输入中的其他干扰。
'''
Hebb 学习规则
神经网络的学习即是神经元间的连接权值调整过程 w_i^{old}→w_i^{new}， 基于 Hebb 理论：“当一个神经元 A 的轴突与神经元B很近足以刺激 B ，且持续或者重复地参与了对 B 的兴奋时，这两个神经元或其中一个就会发生某些生长过程或代谢变化”，换句话说即是，当突触 w_{ij}​ 两侧连接的神经元 x_i,x_j​​ 同时兴奋，它们之间的连接权值就会增大。
基于 hebb 规则，该网络中的权值 wijw_{ij}w​ij​​ 的调整会根据以下规则进行调整：
w_{ij}^{new}=w_{ij}^{old}+α⋅x​_i​​⋅y_​j​​

在训练阶段，自联想存储器的任务是学习模式对{0,0},{1,1},{2,2},{3,3} 的匹配。

学习规则：
wij=wij+α⋅xi(1)⋅yi(1)

wij=wij+α⋅xi(2)⋅yi(2)

wij=wij+α⋅xi(3)⋅yi(3)

wij=wij+α⋅xi(4)⋅yi(4)

在测试阶段，我们会对这些数字加了遮挡或是噪声之后作为输入。
testData

使用训练阶段学习到的 w 权值矩阵，并且由于为控制输出结果向量值为 0 或 1 ，我们采用硬限幅输函数作为激发函数：

hardlim(n)={1,n≥0
           {0,n<0 

hardlim 硬限幅激活函数： 在给定网络的输入矢量或矩阵S时，返回该矢量或矩阵S的输出。当S中的元素值大于等于0时返回值为1，小于0时返回值为0. 即模拟突触中，当网络的输入达到阈值时，则硬限幅激活函数的输出为1，否则为0.

因此测试阶段的输出为：
yj=hardlim(∑i=1nwij⋅xi)
'''

# sudo pip install pillow
# sudo pip install numpy
# sudo pip install matplotlib
# sudo apt-get install python-tk


import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 主函数处理从文件中读入数据，调用训练函数及测试函数测试训练结果并展示
def main():
    #学习步长设置为0.5，可设置成不同值查看训练效果
    alpha = 0.5 
    #分别存放训练集与测试集的文件目录相对路径
    trainDir = "train/"
    testDir = "test/"
    trainImg = os.listdir(trainDir)
    trainImg.sort()
    
    trnLen = len(trainImg)
    W = None;
    # training
    for i in range(trnLen):
             img = np.array(Image.open(trainDir+trainImg[i]))
                #调用训练函数进行自联想存储器的训练
             W = training(W, img, alpha)
     #展示训练集中的数字图片
    count = 1
    for i in range(trnLen):
            img = Image.open(trainDir+trainImg[i])
            plt.subplot(1,trnLen,i+1)
            plt.title(str(i))
            count = count + 1
            plt.imshow(img,cmap=plt.cm.gray)
            
    # testing
    dirsAll = os.listdir(testDir)
    dirsAll.sort()
    dirLen = len(dirsAll) 
    # 设置输出测试结果面板的大小
    count = 1

    plt.figure(figsize=(10,10))
    # 则测试集中，每个数字的图片都放置在一个文件夹中，因此先对每个子目录进行遍历
    for i in range(dirLen):
            files = os.listdir(testDir+dirsAll[i])
            files.sort()
            filesLen = len(files)
            # 进入每个数字图片对应的文件目录中
            # 取出对应于每个数字图片的遮挡或加噪音图片进行自联想存储器的测试
            for j in range(filesLen):
    
                 fullPath = testDir + dirsAll[i] + '/' + files[j]
                 img = np.array(Image.open(fullPath))
                      #利用训练得到的权值矩阵进行测试
                 imageResult = testing(W, img)
                 
                 DisSource = hardlim(transform(img).reshape(img.shape))
                  # 将对测试集的联想结果从列向量的形式转换为与输入图片一样的矩阵形式
                 DisResult = imageResult.reshape(img.shape)
                 
                 plt.subplot(dirLen, 2 * filesLen , count)                 
                 plt.title('source')
                 count = count + 1
                 plt.imshow(DisSource,cmap=plt.cm.gray)
                 
                 plt.subplot(dirLen, 2 * filesLen, count)
                 plt.title('result')
                 count = count + 1                 
                 plt.imshow(DisResult,cmap=plt.cm.gray)
    fig = plt.get_current_fig_manager()
    fig.window.wm_geometry("+100+0")             
    plt.show() 

# 实现hardlim硬限传输激发函数
def hardlim(a):   
    a[ a >= 0 ] = 1
    a[a < 0 ] = 0
    return a

# 对输入图片作处理
def transform(img):
# 将图片转换为列向量的形式，一般在机器学习的训练中都用一个列向量表示某个样本
     result = np.int_(img.reshape((-1,1)))
     length = len(result)
     # 由于输入的二值图片像素值为0(黑色)或非0(白色)
     # 为便于分类训练色像素点对应的分量值置为-1，其他置为1 
     for i in range(length):
        if result[i] == 0:
            result[i] = -1            
        else:
            result[i] = 1;          
     return result   

# 训练函数
def training(W,img,al): 
    p = transform(img)
    pLen = len(p)
        # 初始化权值矩阵W全0矩阵
    if W is None:
        W = np.zeros((pLen,pLen))
    t = p
    # 实现训练阶段基于hebb规则的学习过程
    # 使用np.dot()函数实现向量的内积运算
    result = W + al * np.dot(p,t.T);
    return result

# 使用训练阶段得到的W矩阵，实现神经元中的输出'$$ y = f(W \cdot X) $$', 这里的fff函数即是hardlim硬限传输激发函数， WWW为训练阶段得到的权值举证。
def testing(W, img):
        #  调用激发函数hardlim控制输出结果为0或1    
        result = hardlim(np.dot(transform(img).T,W))      
            
        return result  
    
if __name__ == '__main__':
    main()
    
'''
通过本次实验我们可以看出自联想存储器具有降噪或从众多输入中去除干扰的功能，这也是自联想存储器能够在解决鸡尾酒问题中发挥初步作用的原因。从实验中可看出在输入的数字有噪音或是遮挡的情况下，自联想存储器的联想结果也不是特别一致，与其训练效果有关的有学习步长或是整个网络层次结构的设置。目前许多机器学习里的训练算法都是基于 Hebb 规则进行改进，使得整个神经网络的学习性能更佳，不管是在物体，图像或是语音识别上都取得了不错的效果。因此通过此门课程学习到的 Hebb 规则，及通过设置自联想存储器帮助理解其工作原理后，有助于后续机器学习神经网络中训练算法的学习。
'''
