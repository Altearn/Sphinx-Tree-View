from enum import Enum
import importlib
import os
from pathlib import Path
from sphinx.util import logging
from sphinx.application import Sphinx
from sphinx_treeview.decorator import DecoratorType, imagesToDecoratorIcons
from sphinx_treeview.icon_renderer import TreeIconRenderer
from sphinx_treeview.treeview import TreeViewDirective
from jinja2 import Environment, FileSystemLoader

logger = logging.getLogger(__name__)

__version__ = importlib.metadata.version('sphinx-treeview')
package_dir = os.path.abspath(os.path.dirname(__file__))

class DecoratorRegistry(Enum):
    DIR = "dir"
    
    
def add_static_path(app):
    static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "_static"))
    app.config.html_static_path.append(static_path)
    
    
def config_inited(app: Sphinx, config: dict):
    
    app.connect("builder-inited", add_static_path)
    
    decorators: list[DecoratorType] = []

    if config.stv_decorators:
        for decorator in config.stv_decorators:
            if isinstance(decorator, DecoratorType):
                decorators.append(decorator)
                logger.verbose(f"Tree view decorator '{decorator.name}' added.")
            else:
                logger.error(f"Invalid decorator type: {type(decorator)}")
                
    if not config.stv_disable_default_decorators:
        for decorator in DecoratorRegistry:
            dir_type = DecoratorType(decorator.value, imagesToDecoratorIcons(Path(__file__).parent / '_static' / 'stv' / 'images' / decorator.value, f"stv/images/{decorator.value}"))
            decorators.append(dir_type)
            logger.verbose(f"Tree decorator '{decorator.value}' added.")
            
    env = Environment(loader = FileSystemLoader({Path(__file__).parent}))
    template = env.get_template("tree.css.jinja")
    css = template.render(decorators=decorators)
    
    for decorator in decorators:
        app.add_role(decorator.name, TreeIconRenderer(decorator.name))
    
    with open(Path(__file__).parent / '_static' / 'tree.css', "w") as f:
        f.write(css)
    app.add_css_file('tree.css')
    logger.verbose("CSS file generated and added.")
    

def setup(app: Sphinx):
    
    app.add_directive('treeview', TreeViewDirective)
    app.add_config_value('stv_decorators', [], 'html')
    app.add_config_value('stv_disable_default_decorators', False, 'html')
    logger.verbose("Tree view added.")
        
    app.connect("config-inited", config_inited)
    
    return {
        "version": __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
    
    
    
