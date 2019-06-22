from lxml import etree

tree = etree.parse("web.html")

print(etree.tostring(tree))
