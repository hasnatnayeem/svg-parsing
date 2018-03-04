from lxml import etree

tree = etree.parse(open("test.svg", 'r'))

indent = 0

def printRecur(root):
    """Recursively prints the tree."""
    global indent

    i = root.tag.find('}')
    if i >= 0:
        root.tag = root.tag[i+1:]

    print ' '*indent + '%s: %s %s' % (root.tag.title(), root.attrib.get('id', ""), root.attrib.get('fill', ""))
    
    indent += 4
    for elem in root.getchildren():
        printRecur(elem)
    indent -= 4

root = tree.getroot()
printRecur(root)
