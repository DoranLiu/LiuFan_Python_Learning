# 图片隐写术 Steganography
from PIL import Image
# https://pillow.readthedocs.io/en/3.3.x/reference/Image.html#PIL.Image.Image.putdata
# https://pillow.readthedocs.io/en/3.3.x/reference/Image.html#PIL.Image.new
# https://pillow.readthedocs.io/en/3.3.x/reference/Image.html#PIL.Image.Image.getdata

def makeImageEven(image):
    pixels = list(image.getdata())  # 得到一个这样的列表： [(r,g,b,t),(r,g,b,t)...]
    evenPixels = [(r>>1<<1,g>>1<<1,b>>1<<1,t>>1<<1) for [r,g,b,t] in pixels]  # 更改所有值为偶数（魔法般的移位）
    evenImage = Image.new(image.mode, image.size)  # 创建一个相同大小的图片副本
    evenImage.putdata(evenPixels)  # 把上面的像素放入到图片副本
    return evenImage

def encodeDataInImage(image, data):
    evenImage = makeImageEven(image)  # 获得最低有效位为 0 的图片副本
    binary = ''.join(map(constLenBin,bytearray(data, 'utf-8'))) # 将需要被隐藏的字符串转换成二进制字符串
    if len(binary) > len(image.getdata()) * 4:  # 如果不可能编码全部数据， 抛出异常
        raise Exception("Error: Can't encode more than " + len(evenImage.getdata()) * 4 + " bits in this image. ")
    encodedPixels = [(r+int(binary[index*4+0]),g+int(binary[index*4+1]),b+int(binary[index*4+2]),t+int(binary[index*4+3])) if index*4 < len(binary) else (r,g,b,t) for index,(r,g,b,t) in enumerate(list(evenImage.getdata()))] # 将 binary 中的二进制字符串信息编码进像素里
    encodedImage = Image.new(evenImage.mode, evenImage.size)  # 创建新图片以存放编码后的像素
    encodedImage.putdata(encodedPixels)  # 添加编码后的数据
    return encodedImage
# encodeDataInImage() 中，bytearray() 将字符串转换为整数值序列（数字范围是 0 到 2^8-1），数值序列由字符串的字节数据转换而来，如下图：

# utf-8 编码的中文字符一个就占了3个字节，那么四个字符共占 3×4=12 个字节，于是共有12个数字。（可以在右下角切换到中文输入法，这样就能输入中文了）
# 然后 map(constLenBin,bytearray(data, 'utf-8')) 对数值序列中的每一个值应用 constLenBin() 函数，将十进制数值序列转换为二进制字符串序列。
def constLenBin(int):
    binary = "0"*(8-(len(bin(int))-2))+bin(int).replace('0b','')  # 去掉 bin() 返回的二进制字符串中的 '0b'，并在左边补足 '0' 直到字符串长度为 8
    return binary
# 在这里 bin() 的作用是将一个 int 值转换为二进制字符串，详见： https://docs.python.org/3/library/functions.html#bin

# decodeImage() 返回图片解码后的隐藏文字，其接受一个图片对象参数。
def decodeImage(image):
    pixels = list(image.getdata())  # 获得像素列表
    binary = ''.join([str(int(r>>1<<1!=r))+str(int(g>>1<<1!=g))+str(int(b>>1<<1!=b))+str(int(t>>1<<1!=t)) for (r,g,b,t) in pixels])  # 提取图片中所有最低有效位中的数据
    # 找到数据截止处的索引
    locationDoubleNull = binary.find('0000000000000000')
    endIndex = locationDoubleNull+(8-(locationDoubleNull % 8)) if locationDoubleNull%8 != 0 else locationDoubleNull
    data = binaryToString(binary[0:endIndex])
    return data

# 找到数据截止处所用的字符串 '0000000000000000' 很有意思，他的长度为16，而不是直觉上的 8，因为两个包含数据的字节的接触部分可能有 8 个 0。
# binaryToString() 函数将提取出来的二进制字符串转换为隐藏的文本：
def binaryToString(binary):
    index = 0
    string = []
    # 在上图中，只有 x 所在的位置（也即是字节中第一个 0 之后的数据）存储的是真正的字符数据，因此我们使用下面两个匿名函数来提取出这些数据：
    rec = lambda x, i: x[2:8] + (rec(x[8:], i-1) if i > 1 else '') if x else ''
    # rec = lambda x, i: x and (x[2:8] + (i > 1 and rec(x[8:], i-1) or '')) or ''
    fun = lambda x, i: x[i+1:8] + rec(x[8:], i-1)
    # fun() 接受 2 个参数，第一个参数为表示一个字符的二进制字符串，这个二进制字符串可能有不同的长度（8、16、24...48）；第二个参数为这个字符占多少个字节。
# lambda x, i: x[i+1:8] + rec(x[8:], i-1) 中 x[i+1:8] 获得第一个字节的数据，然后调用 rec()，以递归的方提取后面字节中的数据。
# 这里要提一句，rec = lambda x, i: x[2:8] + (rec(x[8:], i-1) if i > 1 else '') if x else ''，你可能对在表达式里面引用了 rec 感到不可理解，的确，严格意义上这样是不能实现递归的，但在 python 里这样是可以的，这就是 python 的语法糖了。
    while index + 1 < len(binary):
        chartype = binary[index:].index('0') # 我们注意到，字符的字节数据中，第一个字节开头 1 的数目便是字符所占的字节数 存放字符所占字节数，一个字节的字符会存为 0
        length = chartype*8 if chartype else 8
        # int(): 接受两个参数，第一个参数为数字字符串，第二个参数为这个数字字符串代表的数字的进制。详见： https://docs.python.org/3/library/functions.html#int
        # chr()：接受一个参数，参数为 int 值，返回 Unicode 码点为这个 int 值的字符。
        string.append(chr(int(fun(binary[index:index+length],chartype),2)))
        index += length
    return ''.join(string)