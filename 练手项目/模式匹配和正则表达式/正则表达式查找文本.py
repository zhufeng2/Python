import re
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('my phone number is 233-233-4545')
# search 对象返回一个match对象，match返回一个group（）方法，返回被查找的对象的具体文本还可以讲
# group()对象进行分组
print('Phone number found:' + mo.group())

