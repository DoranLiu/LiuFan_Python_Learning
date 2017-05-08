'''
普通的连表查询，一个把select的查询查询结果当作另外一个select的参数

SELECT * FROM personnel.person_info where personnel.person_info.part_nid in (SELECT nid from personnel.part WHERE personnel.part.caption="XO股份有限公司公司-技术部-Python开发");
显示结果

+-----+---------+------------------+-------------+----------+----------+---------+
| nid | name    | email            | phone       | part_nid | position | caption |
+-----+---------+------------------+-------------+----------+----------+---------+
|   1 | as      | as@anshengme.com | 13800138000 |        5 | Python   | NULL    |
|   2 | ansheng | as@anshengme.com | 13800138000 |        5 | Python   | NULL    |
|   3 | a       | as@anshengme.com | 13800138000 |        5 | Python   | NULL    |
|   4 | v       | as@anshengme.com | 13800138000 |        5 | Python   | NULL    |
|   5 | b       | as@anshengme.com | 13800138000 |        5 | Python   | NULL    |
|   6 | w       | as@anshengme.com | 13800138000 |        5 | Python   | NULL    |
+-----+---------+------------------+-------------+----------+----------+---------+
6 rows in set (0.00 sec)
加入进行连表查询

SQL指令

select * from personnel.person_info left join personnel.part on personnel.person_info.part_nid = personnel.part.nid where personnel.part.caption = 'XO股份有限公司公司-技术部-Python开发';
显示结果

+-----+---------+------------------+-------------+----------+----------+---------+------+---------------------------------------------------+
| nid | name    | email            | phone       | part_nid | position | caption | nid  | caption                                           |
+-----+---------+------------------+-------------+----------+----------+---------+------+---------------------------------------------------+
|   1 | as      | as@anshengme.com | 13800138000 |        5 | Python   | NULL    |    5 | XO股份有限公司公司-技术部-Python开发              |
|   2 | ansheng | as@anshengme.com | 13800138000 |        5 | Python   | NULL    |    5 | XO股份有限公司公司-技术部-Python开发              |
|   3 | a       | as@anshengme.com | 13800138000 |        5 | Python   | NULL    |    5 | XO股份有限公司公司-技术部-Python开发              |
|   4 | v       | as@anshengme.com | 13800138000 |        5 | Python   | NULL    |    5 | XO股份有限公司公司-技术部-Python开发              |
|   5 | b       | as@anshengme.com | 13800138000 |        5 | Python   | NULL    |    5 | XO股份有限公司公司-技术部-Python开发              |
|   6 | w       | as@anshengme.com | 13800138000 |        5 | Python   | NULL    |    5 | XO股份有限公司公司-技术部-Python开发              |
+-----+---------+------------------+-------------+----------+----------+---------+------+---------------------------------------------------+
6 rows in set (0.00 sec)
的上面意思的英文查询personnel.person_info.part_nid列的字段状语从句：personnel.part.nid一样的数据，并且personnel.part.caption = 'XO股份有限公司公司-技术部-Python开发'

参数	实例	描述
left join	tb1 left join tb2	左外链接
right join	tb1 right join tb2	右外链接
inner join	tb1 inner join tb2	内链接
Full Join	-	全外连接
CROSS	-	交叉链接，又称笛卡尔链接或叉乘
左连接

TB1为主，TB2为辅，将一中所有的数据罗列出来
TB2则只显示与TB1对应的数据
以下执行语句在person_info表中插入一条数据

INSERT INTO personnel.person_info (NAME,email,phone,part_nid,position) VALUES("aa","a@ansheng.me",13800138000,3,"DBA");
通过left jion进行查询

mysql> use personnel
Database changed
mysql> select * from person_info LEFT JOIN part on person_info.part_nid = part.nid WHERE part.nid = 3;
+-----+------+--------------+-------------+----------+----------+---------+------+------------------------------------------+
| nid | name | email        | phone       | part_nid | position | caption | nid  | caption                                  |
+-----+------+--------------+-------------+----------+----------+---------+------+------------------------------------------+
|   9 | aa   | a@ansheng.me | 13800138000 |        3 | DBA      | NULL    |    3 | XO股份有限公司公司-技术部-DBA            |
+-----+------+--------------+-------------+----------+----------+---------+------+------------------------------------------+
1 row in set (0.00 sec)
这样他就只把我们刚刚插入的那条数据查询了除了，即查询person_info表中的内容，part表中的列作为person_info表的查询条件，如果person_info表中的part_nid列如果等于part表中nid列，那么就显示数据。

内部联接

自动忽略两张表没有建立关联数据
只返回两个表中链接字段相等的数据
select * from person_info inner JOIN part on person_info.part_nid = part.nid;
显示结果

+-----+---------+------------------+-------------+----------+----------+---------+-----+---------------------------------------------------+
| nid | name    | email            | phone       | part_nid | position | caption | nid | caption                                           |
+-----+---------+------------------+-------------+----------+----------+---------+-----+---------------------------------------------------+
|   1 | as      | as@anshengme.com | 13800138000 |        5 | Python   | NULL    |   5 | XO股份有限公司公司-技术部-Python开发              |
|   2 | ansheng | as@anshengme.com | 13800138000 |        5 | Python   | NULL    |   5 | XO股份有限公司公司-技术部-Python开发              |
|   3 | a       | as@anshengme.com | 13800138000 |        5 | Python   | NULL    |   5 | XO股份有限公司公司-技术部-Python开发              |
|   4 | v       | as@anshengme.com | 13800138000 |        5 | Python   | NULL    |   5 | XO股份有限公司公司-技术部-Python开发              |
|   5 | b       | as@anshengme.com | 13800138000 |        5 | Python   | NULL    |   5 | XO股份有限公司公司-技术部-Python开发              |
|   6 | w       | as@anshengme.com | 13800138000 |        5 | Python   | NULL    |   5 | XO股份有限公司公司-技术部-Python开发              |
|   9 | aa      | a@ansheng.me     | 13800138000 |        3 | DBA      | NULL    |   3 | XO股份有限公司公司-技术部-DBA                     |
+-----+---------+------------------+-------------+----------+----------+---------+-----+---------------------------------------------------+
7 rows in set (0.00 sec)
MySQL Full Join的实现

把左右两个表的数据都取出来，不管是否匹配
MySQL Full Join的实现因为MySQL不支持FULL JOIN，下面是替代方法

语法

select * from A left join B on A.id = B.id (where 条件）
union --all可选
select * from A right join B on A.id = B.id （where条件);
交叉

如果甲和乙是两个集合，他们的交叉连接就记为：AXB

mysql> use personnel
Database changed
mysql> SELECT * from course;
+-----+--------+
| Cno | Cname  |
+-----+--------+
|   1 | 足球   |
|   2 | 篮球   |
|   3 | 排球   |
+-----+--------+
3 rows in set (0.00 sec)
mysql> SELECT * from student;
+-----+--------+
| Sno | Name   |
+-----+--------+
|   1 | 张三   |
|   2 | 李四   |
|   3 | 王五   |
+-----+--------+
3 rows in set (0.00 sec)
mysql> SELECT * FROM course CROSS JOIN student;
+-----+--------+-----+--------+
| Cno | Cname  | Sno | Name   |
+-----+--------+-----+--------+
|   1 | 足球   |   1 | 张三   |
|   2 | 篮球   |   1 | 张三   |
|   3 | 排球   |   1 | 张三   |
|   1 | 足球   |   2 | 李四   |
|   2 | 篮球   |   2 | 李四   |
|   3 | 排球   |   2 | 李四   |
|   1 | 足球   |   3 | 王五   |
|   2 | 篮球   |   3 | 王五   |
|   3 | 排球   |   3 | 王五   |
+-----+--------+-----+--------+
9 rows in set (0.00 sec)
一对多，多表查询

创建³³ color表

CREATE TABLE `color` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`nid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
往color表中添加两条数据

insert into color(title) values('red'),('yellow');
person_info添加表color_nid列，类型是int

alter table person_info add color_nid int;
把person_info表中的color_nid列状语从句：color表中的nid列做一个外键关联

alter table person_info add constraint person_ibfk_2 foreign key person_info(`color_nid`) REFERENCES color(`nid`);
往person_info表中插入一条数据

INSERT INTO personnel.person_info (NAME,email,phone,part_nid,position,color_nid) VALUES("b", "b.ansheng.me",13800138000,3,"DBA",1)
查询职位是XO股份有限公司公司-技术部-DBA，的英文颜色yellow的的人员

SELECT * FROM person_info LEFT JOIN part ON person_info.part_nid = part.nid LEFT JOIN color ON person_info.color_nid = color.nid WHERE color.title = "yellow";
多对多关系及查询

先创建三张表

学生（学生表）

CREATE TABLE `student` (
  `Sno` int(11) NOT NULL AUTO_INCREMENT,
  `Name` char(20) NOT NULL,
  PRIMARY KEY (`Sno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
场（课程表）

CREATE TABLE `course` (
  `Cno` int(11) NOT NULL AUTO_INCREMENT,
  `Cname` char(10) NOT NULL,
  PRIMARY KEY (`Cno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
student_course（关系表）

CREATE TABLE `student_course` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Sno` int(11) NOT NULL,
  `Cno` int(11) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
设置外键关联

ALTER TABLE student_course ADD CONSTRAINT student_course_to_student_ibfk_2 FOREIGN KEY student_course (`Sno`) REFERENCES student (`Sno`);
ALTER TABLE student_course ADD CONSTRAINT student_course_to_course_ibfk_1 FOREIGN KEY student_course (`Cno`) REFERENCES course (`Cno`);
往course(课程表)中插入数据

INSERT INTO course(Cname) VALUES("足球"),("篮球"),("排球");
往student(学生表)中插入数据

INSERT INTO student(Name) VALUES("张三"),("李四"),("王五");
student_course(关系表)插入数据

INSERT INTO student_course(Sno,Cno) VALUES(2,1),(2,3),(3,3),(3,1),(1,2),(3,2);
显示学生所选的课程SQL指令

SELECT s.Name,C.Cname FROM student_course AS sc LEFT JOIN student AS s ON s.Sno=sc.Sno LEFT JOIN course AS c ON c.Cno=sc.Cno;
结果如下：

+--------+--------+
| Name   | Cname  |
+--------+--------+
| 张三   | 篮球   |
| 李四   | 足球   |
| 李四   | 排球   |
| 王五   | 排球   |
| 王五   | 足球   |
| 王五   | 篮球   |
+--------+--------+
6 rows in set (0.00 sec)
'''