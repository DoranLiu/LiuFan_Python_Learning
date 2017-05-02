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
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=增加数据=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''#增加数据'''
MySesion = sessionmaker(bind=engine)
session = MySesion()

# # 添加单条数据
# 创建一条数据
users = UserInfo(name='Hello', password='World')
# 把数据添加到表内
session.add(users)
# 提交生效
session.commit()

# 添加多条数据
session.add_all([
    UserInfo(name='A', password='1'),
    UserInfo(name='B', password='2')
])

# 提交
session.commit()


'''# 往表里添加数据'''
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

# 添加父亲的数据
F = Father(name='as')
session.add(F)
session.commit()
# 添加儿子的数据
S1 = Son(name='Son1', father_id=1)
S2 = Son(name='Son2', father_id=1)
session.add_all([S1, S2])
session.commit()
# 另外一种添加数据的方式
F = session.query(Father).filter_by(id=1).first()
S3 = Son(name='Son3')
# 要用追加的方式进行添加，F.son是一个列表，如果不用append将会把之前的数据对应的值进行删除
F.son.append(S3)
session.add(F)
session.commit()