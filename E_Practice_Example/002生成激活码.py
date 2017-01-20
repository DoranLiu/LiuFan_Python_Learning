# 第002题：你要搞限时促销，为你的应用生成激活码（或者优惠券），使用Python如何生成200个激活码（或者优惠券）

import random, string

def rand_str(num, length = 7):
    with open('Activation_code.txt','wt') as f:
        for i in range(num):
            chars = string.ascii_letters + string.digits
            s = [random.choice(chars) for i in range(length)]
            f.write(''.join(s)+'\n')
        f.close()

if __name__ == '__main__':
    rand_str(200)

# Python3x的string类型与Python2x的类型不相同，在Python3x中需要将str编码
# with open("test.out", 'wb') as fp:
#     fp.write(bytes(line, 'utf-8'))
# 如果你不想用b(binary)模式写入，那么用t(text, 此为写入的默认模式)模式写入也可以
# with open("test.out", 'wt') as fp:
#     fp.write(line)

