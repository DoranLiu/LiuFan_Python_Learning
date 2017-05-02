import sqlalchemy
from sqlalchemy import Column, Integer, String, Index, UniqueConstraint, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationships
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/Spider_Data?charset=utf8', echo=True)  # echo=True输出生成的SQL语句
Base = declarative_base()  # 生成一个ORM基类

# 创建一个UserInfo表
class UserInfo(Base):
    __tablename__ = 'UserInfo'  # 表名
    """
    创建字段
    index=True  普通索引
    unique=T  唯一索引
    """
    id = Column(Integer, primary_key=True, autoincrement=True)  # primary_key=主键,autoincrement=自增
    name = Column(String(32))
    password = Column(String(16))
    __table_args__ = (
        Index('id', 'name'),  # 联合索引
        UniqueConstraint('name', 'password', name='name_password')  # 联合唯一索引,name索引的名字
    )
    # 让查询出来的数据显示中文
    def __repr__(self):
        return self.name
Base.metadata.create_all(engine)  # 把所有集成Base类的类，创建表结构

'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=查询数据=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''#查询数据'''
MySesion = sessionmaker(bind=engine)
session = MySesion()

# 获取某个表中的所有内容
result = session.query(UserInfo).all()
print(result)


# 获取指定字段
result = session.query(UserInfo.name, UserInfo.password).all()

# 获取指定的
result = session.query(UserInfo).filter_by(name='b').all() # 返回的是一个列表

# 获取第一条
result = session.query(UserInfo).filter_by(name='b').first()

# 获取值中的某个属性
result.name

# 获取数据出现的个数
result = session.query(UserInfo).filter_by(name='b').count()

'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=and_和or_查询数据=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''

# 使用and_和or_进行查询
# 导入and_, or_模块
from sqlalchemy import and_, or_

'''and_'''
for row in session.query(UserInfo).filter(and_(UserInfo.name == 'A', UserInfo.password == 1)):
    print(row)

'''or_'''
for row in session.query(UserInfo).filter(or_(UserInfo.name == 'Hello', UserInfo.password == 1)):
    print(row)

'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=关联查询=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''

# 关联查询

# 创建以下数据库
class Son(Base):
    __tablename__ = 'son'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    father = relationship('Father')
    # 创建外键
    father_id = Column(Integer, ForeignKey('father.id'))
class Father(Base):
    __tablename__ = 'father'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    son = relationship('Son')
    # son = relationship('Son', backref='Father') 相当于上面两个relationship
# 生成表
Base.metadata.create_all(engine)