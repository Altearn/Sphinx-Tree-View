import os

class DecoratorIcon:
    def __init__(self, path: str, name: str, width: float = 1.3, height: float = 1.3, css_properties: dict[str, str] = {}):
        self.path = path
        self.name = name
        self.width = width
        self.height = height
        self.css_properties = css_properties

class DecoratorType:
    def __init__(self, name: str, icons: list[DecoratorIcon]):
        self.name = name
        self.icons = icons
        
def imagesToDecoratorIcons(path: str, sphinx_static_path: str, width: float = 1.3, height: float = 1.3, css_properties: dict[str, str] = {}) -> list[DecoratorIcon]:
    assets = []
    for file in os.listdir(path):
        separator = '' if sphinx_static_path.endswith('/') else '/'
        assets.append(DecoratorIcon(f'{sphinx_static_path}{separator}{file}', file.split('.')[0], width, height, css_properties))
    return assets
    