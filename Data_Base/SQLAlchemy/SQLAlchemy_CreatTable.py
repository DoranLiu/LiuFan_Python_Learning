'''
https://blog.ansheng.me/article/python-full-stack-way-sqlalchemy/

SQLAlchemy的目的是满足这两个原则:
SQL数据库的行为不像对象集合的较具规模和业绩开始关系; 对象集合表现得不像越抽象开始关系表和行。

SQLAlchemy认为数据库是关系代数发动机，而不仅仅是一个表的集合，行可以不仅从表中选择，但也加入和其他select语句;
任何这些单元可被组合成一个较大的结构，SQLAlchemy的表达式语言基础上，从它的核心这个概念。

SQLAlchemy是最有名的对象关系映射器（ORM），提供数据映射模式 ，其中类可以在开放式的，
多种方式被映射到数据库中的可选组件-允许对象模型和数据库模式中，以开发干净地分离从开始方式。

SQLAlchemy的对这些问题的总体思路是大多数其它SQL/ORM工具，根植于所谓的complimentarity-导向的方式完全不同;
而不是藏起来了SQL和关系对象的细节自动化墙后面，所有的进程都充分一系列组合的，透明的工具中暴露出来 。

该库发生在自动冗余任务的工作，而开发商仍然在数据库中是如何组织和SQL是如何构造的控制。
'''
'''
数据库的链接：
MySQL-Python
mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>

pymysql
mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]

MySQL-Connector
mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
'''
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=单表创建=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Index, UniqueConstraint, ForeignKey
from sqlalchemy.orm import sessionmaker

                       #'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/Spider_Data?charset=utf8', echo=True)  # echo=True输出生成的SQL语句
Base = declarative_base()  # 生成一个ORM基类
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
'''
# 相当于这条创建语句
CREATE TABLE `UserInfo` (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(32),
    password VARCHAR(16),
    PRIMARY KEY (id),
    CONSTRAINT name_password UNIQUE (name, password)
)
'''

'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=创建一对多表=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
class Favor(Base):
    __tablename__ = 'favor'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    caption = Column(String(50), default='red', unique=True)
class Person(Base):
    __tablename__ = 'person'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    favor_id = Column(Integer, ForeignKey("favor.nid"))


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=创建多对多表=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# 组
class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    port = Column(Integer, default=22)
# 服务器
class Server(Base):
    __tablename__ = 'server'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)
# 服务器组，第三张表
class ServerToGroup(Base):
    __tablename__ = 'servertogroup'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    server_id = Column(Integer, ForeignKey('server.id'))
    group_id = Column(Integer, ForeignKey('group.id'))

'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=删除表=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
Base.metadata.drop_all(engine)  # 把所有集成Base类的类，删除表