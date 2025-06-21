from docutils import nodes
from sphinx.util.docutils import SphinxRole


class DecoratorIconRole(SphinxRole):
    def __init__(self, name: str):
        self.name = name

    def run(self):
        icon = f'<span class="treeview-icon treeview-{self.name}-{self.text}" title="{self.text}"></span>'
        node = nodes.raw('', icon, format='html')
        self.set_source_info(node)
        return [node], []
