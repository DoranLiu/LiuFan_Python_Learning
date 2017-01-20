功能需求：
1.需要构建命令行解析器从命令中解析出文件路径参数
2.加载图像与滤镜文件
3.处理图像
4.保存处理后的图像

运行方式：
python3 filter.py <curves> <image>

滤镜：nashville、country

main函数涉及的类说明：
Filter	实体类	滤镜类，用于加载 ACV 件并且从文件中解析出 numpy.poly1d 类型的多项式
FilterManager	实体类	滤镜管理类，并将制定滤镜作用于图像
get_name	函数	分割文件路径名，获得文件名，例如处理 str = '/usr/home/123.jpg' 将返回文件名 123


_read_curves 函数解析:
_read_curves 函数负责从 ACV 文件中解析出曲线点的坐标集，但是据我所知 Python 并没有提供可以格式化解析 ACV 文件的内建函数。不过所幸 adobe 官方给出了 ACV 文件的数据格式，因此我们就可以利用 Python 的 struct 模块来解析特定二进制串所代表的实际数据。

首先我们来看一下 ACV 文件的数据格式:
字节长度	 说明
2	标志，值为 1 或 4 。
2	如果标志为 1 ，该字段表示文件中曲线的位映像；如果标志为 4 ，该字段表示文件中曲线的条数。
接下来的这些字段表示了单条曲线的具体信息，因此每一条曲线都对应着这样的一个字段。
2	用于描述当前曲线的点的个数（值介于 2~19 之间，类型为 short integer）。
点的个数 * 4	这个数据段表示一系列的点，每个点存储于包含两个 short integer 类型的元组中，注意！元组中第二个值表示输入值，而第一个值表示对应的输出值，也就是第一个数对应直角坐标系的 Y 坐标，而第二个数对应 X 坐标。
看完上边的一堆说明之后想必大家都觉得一脸懵逼，不知何从下手。想要理解如何使用这些数据还需要明白一个事实，那就是滤镜的本质就是函数（滤波函数），它作用于图像的时候就是通过将图像中每个颜色通道（通常是 RGB，每个通道的可能对应着不同的滤波函数）中的每一个像素点的值都带入滤波函数（或者多项式）进行计算从而获得新的值，而这些新的像素值所组成的图像就呈现出与原图不同的效果。

所以 ACV 文件中存储的曲线就是指的这些滤镜所对应的多项式，但是 ACV 也并不是直接将计算公式存储于文件中，而是将这些公式对应的直角坐标系中的曲线用几个特殊的坐标点进行近似表示。

所以为了从 ACV 中获取滤波的多项式，我们首先要从中解析出多项式的点集，再从点集逆推出多项式各项系数。

备注：我们实验中用到的 ACV 文件都是标志为 4 类型的。
那么在理解了 ACV 文件的数据格式之后，我们就开始尝试解析 ACV 文件了，我们使用 struct 模块来帮助解析。

struct 模块为 Python 变量与 C 结构之间提供了转换操作，该模块可以用来处理二进制数据，比如文件或者是网络字节流等。

struct 模块最主要的三个函数是：

unpack(fmt, buff) 按照 fmt 指定格式解析字节流，并返回元组
pack(fmt, v1, v2, ...) 与 unpack 相反，按照 fmt 指定的格式将数据封装成字节对象并返回
calcsize(fmt) 计算 fmt 格式占用的内存量（字节）
这里我们只需要用到 unpack 函数。

要解析一个二进制流，通常在 fmt 的第一位我们需要指定解析的字节顺序（大小端对齐）、大小等信息。

Character	Byte order	Size	Alignment
!	network (= big-endian)	standard	none
@	native	native	native
然后部分解析格式对应如下：

Format	C Type	Python Type	Standard Size
h	short	integer	2
H	unsigned short	integer	2
这里只简单列出一小部分，想更深入了解的同学可以参考以下链接。

更多参考：

https://docs.python.org/3/library/struct.html?highlight=struct#module-struct
为了获得更直观的操作体验，我这里在 Python 的命令行交互界面对 luma.acv 文件进行解析。


_find_coefficients 函数:

_find_coefficients 函数负责根据上一步提取的点使用 lagrange 插值法获得近似的多项式，返回的类型是 numpy.poly1d 。

下图展示了 numpy.poly1d 的一种使用方式。

此处输入图片的描述

并且每条曲线都对应一个多项式，分别用于处理不同的通道，为了方便调用而定义了各个多项式的调用接口 get_r(), get_g(), get_b(), get_c() 。

更多参考：
https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.interpolate.lagrange.html#scipy.interpolate.lagrange
https://docs.scipy.org/doc/numpy/reference/generated/numpy.poly1d.html
