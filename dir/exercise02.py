"""
正则表达式　示例
"""
import re

s = """
    孙新翔:1980
    张三:1998
"""
# result = re.findall(r"\w+:\d+", s)
# print(result)

# result = re.split(r"\W+", s, 3)
# print(result)

new = re.sub(r"\d+", "××××", s)
print(new)
