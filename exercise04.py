import re

s = """孙新翔:1980
    张三:1998
    李四:2000
"""
result = re.findall(r"\w+$", s, flags=re.M)
print(result)
