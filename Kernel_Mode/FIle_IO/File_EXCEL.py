'使用第三方库xlrd和xlwt，这两个库分别用于excel读和写'

# 导入xlrd和xlwt
import xlrd
import xlwt
# 打开excel文件
rbook = xlrd.open_workbook('x.xlsx')
# 表
rsheet = rbook.sheet_by_index(0)
# 添加一个总分的列
# 列
nc = rsheet.ncols
# 第0行，列，文本类型，文字，内容
rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, '总分', None)
# 迭代表中的所有数据，计算总分
for row in range(1, rsheet.nrows):
    # 计算每行的总分，跳过第0行,0==姓名,sum对列表进行求和，t等于最后加上拿出来的分数
    t = sum(rsheet.row_values(row, 1))
    # 写入数据
    rsheet.put_cell(row, nc, xlrd.XL_CELL_NUMBER, t, None)
# 写入到文件中
wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)
# 对其方式，垂直和水平都是剧中
style = xlwt.easyxf('align: vertical center, horizontal center')
# rsheet的每个单元格写入到wsheet中
for r in range(rsheet.nrows):  # 行
    for c in range(rsheet.ncols):  # 列
        wsheet.write(r, c, rsheet.cell_value(r, c), style)
wbook.save('output.xlsx')
