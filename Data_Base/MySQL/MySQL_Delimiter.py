'''
创建触发器基本语法

插入前

CREATE TRIGGER tri_before_insert_tb1 BEFORE INSERT ON tb1 FOR EACH ROW
BEGIN
    ...
END
插入后

CREATE TRIGGER tri_after_insert_tb1 AFTER INSERT ON tb1 FOR EACH ROW
BEGIN
    ...
END
删除前

CREATE TRIGGER tri_before_delete_tb1 BEFORE DELETE ON tb1 FOR EACH ROW
BEGIN
    ...
END
删除后

CREATE TRIGGER tri_after_delete_tb1 AFTER DELETE ON tb1 FOR EACH ROW
BEGIN
    ...
END
更新前

CREATE TRIGGER tri_before_update_tb1 BEFORE UPDATE ON tb1 FOR EACH ROW
BEGIN
    ...
END
更新后

CREATE TRIGGER tri_after_update_tb1 AFTER UPDATE ON tb1 FOR EACH ROW
BEGIN
    ...
END
触发器实例

创建一个user_info表和user_info_back表，里面有UID,Name,Password,E-mil列；

CREATE TABLE `user_info` (
  `UID` int(5) NOT NULL AUTO_INCREMENT,
  `Name` char(15) NOT NULL,
  `Password` varchar(32) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`UID`,`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `user_info_back` (
  `UID` int(5) NOT NULL AUTO_INCREMENT,
  `Name` char(15) NOT NULL,
  `Password` varchar(32) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`UID`,`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
创建一个插入前的触发器

触发器的作用就是在往user_info表中插入数据之前进入tri_before_insert_tb1触发器，执行里面的操作

delimiter %
CREATE TRIGGER tri_before_insert_tb1 BEFORE INSERT ON user_info FOR EACH ROW
BEGIN
-- 如果插入时的Name="as"
IF NEW.Name = "ansheng" THEN
    -- 那么就把这条数据先插入user_info_back表中，数据相同
    INSERT INTO user_info_back(Name,Password,Email) VALUES(NEW.Name,NEW.Password,NEW.Email);
END IF;
END%
delimiter ;
使用触发器

触发器无法由用户直接调用，而知由于对表的增/删/改操作被动引发的。

往user_info表中插入两条数据

INSERT INTO user_info(Name,Password,Email) VALUES("ansheng","ansheng","ansheng@ansheng.me"),("root","r","root@ansheng.me");
查看表中的数据

mysql> select * from user_info;
+-----+---------+----------+--------------------+
| UID | Name    | Password | Email              |
+-----+---------+----------+--------------------+
|   1 | ansheng | ansheng  | ansheng@ansheng.me |
|   2 | root    | r        | root@ansheng.me    |
+-----+---------+----------+--------------------+
2 rows in set (0.00 sec)
mysql> select * from user_info_back;
+-----+---------+----------+--------------------+
| UID | Name    | Password | Email              |
+-----+---------+----------+--------------------+
|   1 | ansheng | ansheng  | ansheng@ansheng.me |
+-----+---------+----------+--------------------+
1 row in set (0.00 sec)
删除触发器

DROP TRIGGER tri_after_insert_tb1;
NEW表示即将插入的数据行，OLD表示即将删除的数据行，对于INSERT语句,只有NEW是合法的，对于DELETE语句，只有OLD才合法，而UPDATE语句可以在和NEW以及OLD同时使用
'''