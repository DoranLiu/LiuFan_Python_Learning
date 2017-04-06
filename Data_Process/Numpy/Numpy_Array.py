'''
1。创建数组
2。保存数组
3。操作数组


'''
# Numpy 的数组操作

from numpy import *
'''
# 创建数组
'''
# v 与 M 对象都是 numpy 模块提供的 ndarray 类型
v = array([1,2,3,4])
m = array([[1,2],[3,4]])

# v 与 M 数组的不同之处在于它们的维度。 我们可以通过 ndarray.shape 获得它的维度属性：
# print(v.shape) # (4,)
# print(m.shape) # (2, 2)

# ndarray.size 数组的元素数量：
# print(m.size) # 4

# dtype 属性我们能获得数组元素的类型：
# print(m.dtype)

# 可以显示地定义元素类型通过在创建数组时使用 dtype 关键字参数：
M = array([[1, 2], [3, 4]], dtype=complex)
# array([[ 1.+0.j,  2.+0.j],
#        [ 3.+0.j,  4.+0.j]])


# 同样的，我们可以使用 numpy.shape 与 numpy.size 函数获取对应属性值：
shape(m)
size(m)

'''
ndarray 与 list差不多，但不用list但原因如下：
Python 的 list 是动态类型，可以包含不同类型的元素，所以没有支持诸如点乘等数学函数，因为要为 list 实现这些操作会牺牲性能。
Numpy 数组是 静态类型 并且 齐次。 元素类型在数组创建的时候就已经确定了。
Numpy 数组节约内存。
由于是静态类型，对其数学操作函数（如矩阵乘法，矩阵加法）的实现可以使用 C 或者 Fortran 完成。
'''

# create a range
'''
使用数组生成函数：
当需要生产大数组时，手动创建显然是不明智的，我们可以使用函数来生成数组，最常用的有如下几个函数：
'''
# arange
x_arange = arange(-1, 10, 1) # arguments: start, stop, step
print(x_arange)
# [-1  0  1  2  3  4  5  6  7  8  9]

# linspace
x_linspace = linspace(0,10,25)
print(x_linspace)
# [  0.           0.41666667   0.83333333   1.25         1.66666667
#    2.08333333   2.5          2.91666667   3.33333333   3.75         4.16666667
#    4.58333333   5.           5.41666667   5.83333333   6.25         6.66666667
#    7.08333333   7.5          7.91666667   8.33333333   8.75         9.16666667
#    9.58333333  10.        ]

# logspace
x_logspace = logspace(0,10,10,base=e)
print(x_logspace)
# [  1.00000000e+00   3.03773178e+00   9.22781435e+00   2.80316249e+01
#    8.51525577e+01   2.58670631e+02   7.85771994e+02   2.38696456e+03
   # 7.25095809e+03   2.20264658e+04]

x,y = mgrid[0:5,0:5]
print(x)
# [[0 0 0 0 0]
#  [1 1 1 1 1]
#  [2 2 2 2 2]
#  [3 3 3 3 3]
#  [4 4 4 4 4]]
print(y)
# [[0 1 2 3 4]
#  [0 1 2 3 4]
#  [0 1 2 3 4]
#  [0 1 2 3 4]
#  [0 1 2 3 4]]

x_rand = random.rand(5,5)
x_randn = random.randn(5,5)

x_diag = diag([1,2,3])
print(x_diag)
# [[1 0 0]
#  [0 2 0]
#  [0 0 3]]

x_diag_k = diag([1,2,3],k=2)
print(x_diag_k)
# [[0 0 1 0 0]
#  [0 0 0 2 0]
#  [0 0 0 0 3]
#  [0 0 0 0 0]
#  [0 0 0 0 0]]

x_zeros = zeros((3,4))
print(x_zeros)
# [[ 0.  0.  0.  0.]
#  [ 0.  0.  0.  0.]
#  [ 0.  0.  0.  0.]]

x_ones = ones((3,4))
print(x_ones)
# [[ 1.  1.  1.  1.]
#  [ 1.  1.  1.  1.]
#  [ 1.  1.  1.  1.]]

'''
保存数组：
'''
# savetxt
savetxt("random-matrix.csv", m, fmt='%.5f')

# 使用 numpy.save 与 numpy.load 保存和读取原生文件类型：
x_save = save("random-matrix.npy", m)
x_load = load("random-matrix.npy")

# nnumpy数组的常用属性
x_itemsize = M.itemsize # bytes per element
x_nbytes = M.nbytes # number of bytes
x_ndim = M.ndim # number of dimensions


'''
操作数组：
'''
# 索引

# 最基本的，我们用方括号进行检索：
# v is a vector, and has only one dimension, taking one index
'''
# v[0]
'''
# M is a matrix, or a 2 dimensional array, taking two indices
'''
# M[1,1]
'''
# 如果是N(N > 1)维数列，而我们在检索时省略了一个索引值则会返回一整行((N-1)维数列)：
# M
# => array([[ 0.70506801,  0.54618952,  0.31039856],
#           [ 0.26640475,  0.10358152,  0.73231132],
#           [ 0.07987128,  0.34462854,  0.91114433]])
'''
# M[1]
'''
# => array([ 0.26640475,  0.10358152,  0.73231132])


"使用':'能达到同样的效果:"
# M[1,:] # row 1
# => array([ 0.26640475,  0.10358152,  0.73231132])

# M[:,1] # column 1
# => array([ 0.54618952,  0.10358152,  0.34462854])

"可以利用索引进行赋值："
# M[0,0] = 1

# => array([[ 1.        ,  0.54618952,  0.31039856],
#           [ 0.26640475,  0.10358152,  0.73231132],
#           [ 0.07987128,  0.34462854,  0.91114433]])


# also works for rows and columns
# M[1,:] = 0
# M[:,2] = -1

# => array([[ 1.        ,  0.54618952, -1.        ],
#           [ 0.        ,  0.        , -1.        ],
#           [ 0.07987128,  0.34462854, -1.        ]])



'''切片索引'''

# 切片索引语法：M[lower:upper:step]

# A = array([1,2,3,4,5])

# => array([1, 2, 3, 4, 5])

# A[1:3]

# => array([2, 3])


# 进行切片赋值时，原数组会被修改：

# A[1:3] = [-2,-3]

# => array([ 1, -2, -3,  4,  5])


# 我们可以省略 M[lower:upper:step] 中的任意参数:

# A[::] # lower, upper, step all take the default values

# => array([ 1, -2, -3,  4,  5])

# A[::2] # step is 2, lower and upper defaults to the beginning and end of the array

# => array([ 1, -3,  5])

# A[:3] # first three elements

# => array([ 1, -2, -3])

# A[3:] # elements from index 3

# => array([4, 5])


'''负值索引从数组尾开始计算：'''

# A = array([1,2,3,4,5])
# A[-1] # the last element in the array

# => 5

# A[-3:] # the last three elements

# => array([3, 4, 5])


'''索引切片在多维数组的应用也是一样的:'''

A = array([[n+m*10 for n in range(5)] for m in range(5)])

# => array([[ 0,  1,  2,  3,  4],
#           [10, 11, 12, 13, 14],
#           [20, 21, 22, 23, 24],
#           [30, 31, 32, 33, 34],
#           [40, 41, 42, 43, 44]])


# a block from the original array
# A[1:4, 1:4]

# => array([[11, 12, 13],
#           [21, 22, 23],
#           [31, 32, 33]])

# strides
# A[::2, ::2]

# => array([[ 0,  2,  4],
#           [20, 22, 24],
#           [40, 42, 44]])


'''
高级索引（Fancy indexing）
'''

# 指使用列表或者数组进行索引:

# row_indices = [1, 2, 3]
# A[row_indices]

# => array([[10, 11, 12, 13, 14],
#           [20, 21, 22, 23, 24],
#           [30, 31, 32, 33, 34]])

# col_indices = [1, 2, -1] # remember, index -1 means the last element
# A[row_indices, col_indices]

# => array([11, 22, 34])

'''
我们也可以使用索引掩码:
'''
# B = array([n for n in range(5)])

# => array([0, 1, 2, 3, 4])

# row_mask = array([True, False, True, False, False])
# B[row_mask]

# => array([0, 2])

# same thing
# row_mask = array([1,0,1,0,0], dtype=bool)
# B[row_mask]

# => array([0, 2])

'''
使用比较操作符生成掩码:
'''
x = arange(0, 10, 0.5)

# => array([ 0. ,  0.5,  1. ,  1.5,  2. ,  2.5,  3. ,  3.5,  4. ,  4.5,  5. ,
#            5.5,  6. ,  6.5,  7. ,  7.5,  8. ,  8.5,  9. ,  9.5])

# mask = (5 < x) * (x < 7.5)

# => array([False, False, False, False, False, False, False, False, False,
#           False, False,  True,  True,  True,  True, False, False, False,
#           False, False], dtype=bool)

# x[mask]

# => array([ 5.5,  6. ,  6.5,  7. ])


