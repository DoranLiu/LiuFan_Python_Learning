import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Index, UniqueConstraint, ForeignKey
from sqlalchemy.orm import sessionmaker

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
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=修改数据=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''#修改数据'''
MySesion = sessionmaker(bind=engine)
session = MySesion()

session.query(UserInfo).filter(UserInfo.id == 8).update({"name": "ffff"})
session.commit()
