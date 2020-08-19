import re

s = """孙新翔:1980
    张三:1998
    李四:2000
"""
# result = re.finditer(r"(\w+):(\d+)", s)
result = re.search(r"(\w+):(?P<age>\d+)", s)
# result = re.match(r"(\w+):(\d+)", s)
# for item in result:
#     print(item.group())
print(result.group(1))
print(result.group("age"))
print(result.span())
print(result.groupdict())
