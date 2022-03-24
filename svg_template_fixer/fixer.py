import re
from namespaces import namespaced, namespaced_attrib, namespaces

def parse_translate_function(string):
    match = re.search(r'^translate\((\-?\d+(?:\.\d+)?),(\-?\d+(?:\.\d+)?)\)$', string)
    return float(match.group(1)), float(match.group(2))

def is_double_tspan_text(text):
    doubles = text.findall('svg:tspan/svg:tspan', namespaces)

    return len(doubles) == 1

def fix_transformed_element(element):
    x = float(element.get('x'))
    y = float(element.get('y'))
    transform = element.get('transform')
    
    translate_x, translate_y = parse_translate_function(transform)

    new_x = x + translate_x
    new_y = y + translate_y

    element.set('x', str(new_x))
    element.set('y', str(new_y))
    del element.attrib['transform']

def fix_double_tspan_text(text):
    outer_tspan = text.find('svg:tspan', namespaces)
    inner_tspan = outer_tspan.find('svg:tspan', namespaces)

    outer_tspan.text = inner_tspan.text
    outer_tspan.remove(inner_tspan)

def fix_layer(layer_element):
    # Fix texts with transform as FreeCAD doesn't like it
    for text in layer_element.findall(namespaced('text')):
        if text.get('transform') != None:
            fix_transformed_element(text)

    # Fix double tspan elements as FreeCAD doesn't recognize it's text
    for text in layer_element.findall(namespaced('text')):
        if is_double_tspan_text(text):
            fix_double_tspan_text(text)

    # Remove xml:xml as FreeCAD has problems with it
    for element in layer_element.findall('*'):
        element.attrib.pop(namespaced_attrib('space', 'xml'), None)