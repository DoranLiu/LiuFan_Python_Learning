'''

'''

'''------------------------简单工厂模式（Simple Factory）------------------------------'''
import random
class BasicCourse(object):
    """ 基础课程 """
    def get_labs(self):
        return "basic_course: labs"
    def __str__(self):
        return "BasciCourse"

class ProjectCourse(object):
    """ 项目课 """
    def get_labs(self):
        return "project_course: labs"
    def __str__(self):
        return "ProjectCourse"

class SimpleCourseFactory(object):
    @staticmethod
    def create_course(type):
        """ 简单工厂，用于创建课程"""
        if type == 'bc':
            return BasicCourse()
        elif type == 'pc':
            return ProjectCourse()

if __name__ == '__main__':
    t = random.choice(['bc', 'pc'])
    course = SimpleCourseFactory.create_course(t)
    print(course.get_labs())

# 在上面的代码中，我们的产品是课程，然后使用 SimpleCourseFactory.create_course 来创建课程.
# 在这个静态方法中，我们根据传递的需要创建的课程类型来创建不同的课程。
# 我们有一些问题：如果需要增加一种产品（比如：私有课程），那我们需要改造整个工厂。那么我们有什么解决办法呢？


'''------------------------工厂方法（Factory Method）------------------------------'''
# 如果对工厂进行抽象化，让每个工厂只负责一种产品的生产，当增加一种产品时，就不需要修改已有的工厂，只需要新增加一个工厂就行了。
import random
import abc
# Python本身不提供抽象类和接口机制，要求实现抽象类，可以借助abc模块.ABC是Abstract Base Class的缩写。
class BasicCourse(object):
    """ 基础课程 """
    def get_labs(self):
        return "basic_course: labs"
    def __str__(self):
        return "BasicCourse"
class ProjectCourse(object):
    """ 项目课 """
    def get_labs(self):
        return "project_course: labs"
    def __str__(self):
        return "ProjectCourse"

class Factory(object):
    """ 抽象工厂类 """
    __metaclass__ = abc.ABCMeta
    # 这是用来生成抽象基本类的元类类。由它生成的类可以直接继承。
    @abc.abstractmethod # 表明抽象方法的生成器
    def create_course(self):
        pass

class BasciCourseFactory(Factory):
    """ 基础课程工厂类 """
    def create_course(self):
        return BasicCourse()
class ProjectCourseFactory(Factory):
    """ 项目课程工厂类 """
    def create_course(self):
        return ProjectCourse()

def get_factory():
    """ 随机获取一个工厂类 """
    return random.choice([BasciCourseFactory, ProjectCourseFactory])()

if __name__ == '__main__':
    factory = get_factory()
    course = factory.create_course()
    print(course.get_labs())

'''------------------------抽象工厂模式(Abstract Factory)------------------------------'''
# 在工厂方法模式中，我们会遇到一个问题，当产品非常多时，继续使用工厂方法模式会产生非常多的工厂类。
# 现在我们有一个产品是课程，但是仅仅依靠课程还没办法提供完美的服务，因为在 实验楼 你可以边学课程边做实验呢。在哪里做实验呢？当然是在虚拟机里了。当然我们也有很多种虚拟机，比如 Linux 虚拟机和 Mac 虚拟机。
# 如果按照工厂方法模式的作法，我们需要创建 Linux 虚拟机工厂类和 Mac 虚拟机工厂类， 这样我们就会有一堆工厂类了。但是在 实验楼 里，真正的情况是只有虚拟机和课程结合在一起才能给用户提供完美的服务。我们就不能创建出一个能同时创建课程和虚拟机的工厂吗？因为我们知道其实用户的需求同时包含了课程和虚拟机，如果有一座工厂能同时生产这两种产品就完美了。
#

import random
import abc
# 两种类型的课程
class BasicCourse(object):
    """ 基础课程 """
    def get_labs(self):
        return "basic_course: labs"
    def __str__(self):
        return "BasicCourse"
class ProjectCourse(object):
    """ 项目课 """
    def get_labs(self):
        return "project_course: labs"
    def __str__(self):
        return "ProjectCourse"
# 两种类型的虚拟机
class LinuxVm(object):
    """ Linux 虚拟机 """
    def start(self):
        return "Linux vm running"
class MacVm(object):
    """ Mac OSX 虚拟机 """
    def start(self):
        return "Mac OSX vm running"
class Factory(object):
    """ 抽象工厂类, 现在工厂类不仅能创建课程，还能创建虚拟机了 """
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def create_course(self):
        pass
    @abc.abstractmethod
    def create_vm(self):
        pass
class BasciCourseLinuxFactory(Factory):
    """ 基础课程工厂类 """
    def create_course(self):
        return BasicCourse()
    def create_vm(self):
        return LinuxVm()
class ProjectCourseMacFactory(Factory):
    """ 项目课程工厂类 """
    def create_course(self):
        return ProjectCourse()
    def create_vm(self):
        return MacVm()
def get_factory():
    """ 随机获取一个工厂类 """
    return random.choice([BasciCourseLinuxFactory, ProjectCourseMacFactory])()
if __name__ == '__main__':
    factory = get_factory()
    course = factory.create_course()
    vm = factory.create_vm()
    print(course.get_labs())
    print(vm.start())

    '''抽象工厂模式顺利的解决了工厂方法模式中遇到的问题，我们通过将产品的创建进行组合放入一个工厂类中，不但减少了工厂类的数量，还增加了生产产品体系的能力（比如课程和虚拟机组成了一个产品体系）。现在，工厂类不仅仅能创建课程，还能创建虚拟机，我们只需要一座工厂就能为 实验楼 用户服务啦 。
从简单工厂模式到抽象工厂模式，我们都是在用后一种模式解决前一种模式的缺陷，都是在最大程度降低代码的耦合性。在使用工厂模式家族时，不管使用哪一种工厂模式，只要能达到最大程度的解耦，都是不错的选择。'''