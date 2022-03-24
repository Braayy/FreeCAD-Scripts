from xml.etree.ElementTree import register_namespace

namespaces = {
    '': 'http://www.w3.org/2000/svg',
    'inkscape': 'http://www.inkscape.org/namespaces/inkscape',
    'sodipodi': 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd',
    'svg': 'http://www.w3.org/2000/svg',
    'freecad': 'http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace',
    'xml': 'http://www.w3.org/XML/1998/namespace'
}

def namespaced(name, namespace_prefix=''):
    return f'{{{namespaces[namespace_prefix]}}}{name}'

def namespaced_attrib(name, namespace_prefix=''):
    if namespace_prefix == '':
        return name
    
    return namespaced(name, namespace_prefix)

def register_namespaces():
    for prefix, url in namespaces.items():
        register_namespace(prefix, url)