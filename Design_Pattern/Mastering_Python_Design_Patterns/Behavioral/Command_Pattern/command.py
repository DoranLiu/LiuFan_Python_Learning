'''
命令模式(Command pattern)
命令设计模式帮助我们将一个操作(撤销、重做、复制、粘贴等)封装成一个对象。
简而言之，这意味着创建一个类，包含实现该操作所需要的所有逻辑和方法。
这样做的优势如下所述(请 参考[GOF95，第265页]和网页[t.cn/Rqr3tfQ])。
 我们并不需要直接执行一个命令。命令可以按照希望执行。
 调用命令的对象与知道如何执行命令的对象解耦。调用者无需知道命令的任何实现细节。
 如果有意义，可以把多个命令组织起来，这样调用者能够按顺序执行它们。例如，在实现一个多层撤销命令时，这是很有用的。
'''

'''
本节中，我们将使用命令模式实现最基本的文件操作工具。
 创建一个文件，并随意写入一个字符串  读取一个文件的内容
 重命名一个文件
 删除一个文件
我们并不从头实现这些工具程序，因为Python在os模块中已提供了良好的实现。
我们想做的 是在已有实现之上添加一个额外的抽象层，这样可以当作命令来使用。
这样，我们就能获得命令 提供的所有优势。
'''
import os

verbose = True


class RenameFile:
    # 接受源文件路径(path_src)和目标文件路径(path_dest)作为参数。如果文件路径未使用路径分隔符，则 在当前目录下创建文件。
    def __init__(self, path_src, path_dest):
        self.src, self.dest = path_src, path_dest

    def execute(self):
        if verbose:
            print("[renaming '{}' to '{}']".format(self.src, self.dest))
        os.rename(self.src, self.dest)

    def undo(self):
        if verbose:
            print("[renaming '{}' back to '{}']".format(self.dest, self.src))
        os.rename(self.dest, self.src)


class CreateFile:

    def __init__(self, path, txt='hello world\n'):
        self.path, self.txt = path, txt

    def execute(self):
        if verbose:
            print("[creating file '{}']".format(self.path))
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)

    def undo(self):
        delete_file(self.path)


class ReadFile:

    def __init__(self, path):
        self.path = path

    def execute(self):
        if verbose:
            print("[reading file '{}']".format(self.path))
        with open(self.path, mode='r', encoding='utf-8') as in_file:
            print(in_file.read(), end='')


def delete_file(path):
    if verbose:
        print("deleting file '{}'".format(path))
    os.remove(path)


def main():
    orig_name, new_name = 'file1', 'file2'

    commands = []
    for cmd in CreateFile(orig_name), ReadFile(orig_name), RenameFile(orig_name, new_name):
        commands.append(cmd)

    [c.execute() for c in commands]

    answer = input('reverse the executed commands? [y/n] ')

    if answer not in 'yY':
        print("the result is {}".format(new_name))
        exit()

    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            pass

if __name__ == '__main__':
    main()
