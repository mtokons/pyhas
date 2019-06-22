from lxml import etree

tree = etree.parse("fundamentals/src/web_page.html")

title_element = tree.xpath("//title/text()")[0]
print(title_element)

paragraph_element = tree.xpath("//p/text()")[0]
print(paragraph_element)

list_item = tree.xpath("//li")
# print(list_item)

for lis in list_item:
    text = ''.join(map(str.strip, lis.xpath(".//text()")))
    print(text)