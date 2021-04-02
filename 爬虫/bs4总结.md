the first key point is  using `Beautifulsoup` to analysis the html, Then we can use some way and attributes such as `Beautifulsoup.tagname`, it will return the label appearedd for the first name.

Beautifulsoup.find('tagname') = Beautifulsoup.tagname

for example:

`Beautifulsoup.find('div', class_ = 'chapter_content')`

findall: all the label that you need

select:

select('(id, class, 标签)')返回一个列表

层级选择器:

返回一个层级

`>表示一个层级，空格表示多个层级`

获取标签的文本数据：

1. soup.a.text返回标签中所有的文本内容。
2. string只返回一个直系的文本内容
   
获取标签中的属性值：
for example :

`Beautifulsoup.a['href']`