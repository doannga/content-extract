from lxml import etree


with open('./Resources/test_careerbuilder.html', encoding='utf8', mode='r') as f:
    root = etree.HTML(f.read())
    f.close()
tree = etree.ElementTree(root)
for node in root.iter():
	attributes = node.attrib
	print(attributes)
	print(tree.getpath(node))

def parse(tree):
    tree = html