'''
视图是一个虚拟表（非真实存在），其本质是根据SQL语句获取动态的数据集，并为其命名，用户使用时只需使用名称即可获取结果集，并可以将其当作表来使用。

创建视图

创建一个名称为v1的视图，其功能就是查询color表中的所有数据

CREATE VIEW v1 AS SELECT * FROM color;
查看视图

使用视图时，将其当作表进行操作即可，由于视图是虚拟表，所以无法使用其对真实表进行创建、更新和删除操作，仅能做查询用。

select * from v1; -- 等于执行SELECT * FROM color
输出结果

+-----+--------+
| nid | title  |
+-----+--------+
|   1 | red    |
|   2 | yellow |
+-----+--------+
2 rows in set (0.00 sec)
修改视图

ALTER VIEW v1 AS SELECT * FROM color WHERE nid = 1;
删除视图

DROP VIEW v1;
'''