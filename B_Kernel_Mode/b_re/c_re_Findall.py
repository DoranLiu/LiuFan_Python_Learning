









# findall 返回列表 (或空列表)，finditer 和 match、search  样返回 MatchObject 对象。
import re
s = "12abc345ab"
ms = re.findall(r"\d+", s)
print(ms)
# ['12', '345']
ms = re.findall(r"\d{5}", s)
print(ms)
# []
for m in re.finditer(r"\d+", s): print(m.group(), m.span())
# 12 (0, 2)
# 345 (5, 8)

for m in re.finditer(r"\d{5}", s): print(m.group(), m.span())  # 返回空列表
