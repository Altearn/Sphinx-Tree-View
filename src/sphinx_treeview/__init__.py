from enum import Enum
from importlib import metadata
from pathlib import Path
from shutil import copy
from typing import Any, List

from jinja2 import Environment, FileSystemLoader
from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util import logging

from .decorator import DecoratorType, images_to_decorator_icons
from .directives import TreeViewDirective
from .roles import DecoratorIconRole


BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"
STATIC_DIR = BASE_DIR / "static"

logger = logging.getLogger(__name__)
template_engine = Environment(loader=FileSystemLoader([ASSETS_DIR]))
css_template = template_engine.get_template("treeview.css.jinja")


class DefaultDecoratorRegistry(Enum):
    DIR = "dir"


def config_inited(app: Sphinx, config: Config) -> None:
    decorators = config.stv_decorators or []
    if not config.stv_disable_default_decorators:
        decorators.extend(load_default_decorators())
    decorators = validate_decorators(decorators)

    for decorator in decorators:
        app.add_role(decorator.name, DecoratorIconRole(decorator.name))

    css = css_template.render(decorators=decorators)
    (STATIC_DIR / "treeview.css").write_text(css, encoding="utf-8")
    copy(ASSETS_DIR / "treeview.js", STATIC_DIR / "treeview.js")
    app.add_css_file("treeview.css")
    app.add_js_file("treeview.js")
    logger.verbose("CSS and JS files generated and added.")


def load_default_decorators() -> List[DecoratorType]:
    decorators = []
    for decorator in DefaultDecoratorRegistry:
        icons = images_to_decorator_icons(ASSETS_DIR / decorator.value)
        decorators.append(DecoratorType(decorator.value, icons))
    return decorators


def validate_decorators(decorators: List[Any]) -> List[DecoratorType]:
    valid = []
    for decorator in decorators:
        if isinstance(decorator, DecoratorType):
            logger.verbose(f"Tree view decorator '{decorator.name}' added.")
            valid.append(decorator)
        else:
            logger.warning(f"Ignoring invalid decorator of type {type(decorator)}")
    return valid


def setup(app: Sphinx):
    """Set up the sphinx extension."""
    app.add_directive('treeview', TreeViewDirective)
    app.add_config_value('stv_decorators', [], 'html')
    app.add_config_value('stv_disable_default_decorators', False, 'html')
    logger.verbose("Tree view added.")

    app.config.html_static_path.append(str(STATIC_DIR))
    app.connect("config-inited", config_inited)

    return {
        "version": metadata.version('sphinx-treeview'),
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
