#!/usr/bin/env python3
from xml.etree.ElementTree import parse as XMLParse
import sys
import fixer
from namespaces import namespaced, register_namespaces

def fix_template(broken_root):
    for group_element in broken_root.findall(namespaced('g', 'svg')):
        if group_element.attrib.get(namespaced('groupmode', 'inkscape')) == 'layer':
            fixer.fix_layer(group_element)

def main():
    if len(sys.argv) < 3:
        print(f'[!] Usage: {sys.argv[0]} <broken_file> <output_file>')
        return

    broken_filepath = sys.argv[1]
    output_filepath = sys.argv[2]

    if broken_filepath[-4:] != '.svg':
        print('[!!] Broken file should be a svg file')
        return

    if output_filepath[-4:] != '.svg':
        print('[!!] Output file should be a svg file')
        return

    register_namespaces()

    broken_tree = XMLParse(broken_filepath)
    broken_root = broken_tree.getroot()

    fix_template(broken_root)

    broken_tree.write(output_filepath)
    print('[$] Fixed')

if __name__ == '__main__':
    main()