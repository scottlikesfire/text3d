import math
import numpy as np
import xml.etree.ElementTree as ET
import pdb

#import fonttools

#1 point of font is 1/72 of an inch


if __name__ == "__main__":
    fontfile = '/Users/sorensen/Documents/pythonProjects/text3d/great-vibes/GreatVibes-Regular.ttx'
    print('loading in text xml')
    tree = ET.parse(fontfile)
    root = tree.getroot()
    pdb.set_trace()
    for child in root:
        print(child.tag) 
        print(child.attrib)
        pdb.set_trace()


