"""
第 012 题：敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights

北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
"""
import codecs
def read_txt():
    l=[]
    with codecs.open(r'c:\python27\oneday_one\1.txt') as fp:
        for line in fp.readlines():
           l.append(line.strip())
    return l

def check(l):
    word=input('word:')
    for each_word in l:
        if word==each_word:
            print ('Freedom')
            return None
    print ('Human rights')
    return None

def main():
    l=read_txt()
    check(l)
    print (l)

if __name__=='__main__':
    main()