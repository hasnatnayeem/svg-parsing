from lxml import etree
import json

tree = etree.parse(open("test.svg", 'r'))

indent = 0
data = {}

def recursive_dict(element):
    if element.text == None and len(element.attrib):
        return element.tag, element.attrib
    return element.tag, \
            dict(map(recursive_dict, element)) or element.text

def printRecur(root):
    """Recursively prints the tree."""
    global indent

    i = root.tag.find('}')
    if i >= 0:
        root.tag = root.tag[i+1:]

    print ' '*indent + '%s: %s %s' % (root.tag.title(), root.attrib.get('id', ""), root.attrib.get('fill', ""))
    data["xml"] = element;
    
    indent += 4
    for elem in root.getchildren():
        printRecur(elem)
    indent -= 4

def xml_to_json(xml_input, json_output):
    '''Converts an xml file to json.'''
    dict_to_json(etree_to_dict(xml_to_etree(xml_input), True), json_output)

def xml_to_etree(xml_input):
    '''Converts xml to a lxml etree.'''
    f = open(xml_input, 'r')
    xml = f.read()
    f.close()
    return etree.HTML(xml)

def etree_to_dict(tree, only_child):
    tree.attrib.pop("d", None)
    i = tree.tag.find('}')
    if i >= 0:
        tree.tag = tree.tag[i+1:]
    '''Converts an lxml etree into a dictionary.'''
    mydict = dict([(item[0], item[1]) for item in tree.items()])
    children = tree.getchildren()
    if children:
        if len(children) > 1:
            mydict['children'] = [etree_to_dict(child, False) for child in children]
        else:
            child = children[0]
            mydict[child.tag] = etree_to_dict(child, True)
    if only_child:
        return mydict
    else:        
        return {tree.tag: mydict}

def dict_to_json(dictionary, json_output):
    print json.dumps(dictionary, sort_keys=True, indent=4)
    '''Coverts a dictionary into a json file.'''
    f = open(json_output, 'w')
    f.write(json.dumps(dictionary, sort_keys=True, indent=4))
    f.close()


root = tree.getroot()
root.attrib.pop("viewBox", None)
dict_to_json(etree_to_dict(root, True), "json.json")
#printRecur(root)

