from sphinx.util.docutils import SphinxRole
from docutils import nodes

class TreeIconRenderer(SphinxRole):
    
    def __init__(self, name: str):
        self.name = name

    def run(self):
        svg = f'<span class="stv-{self.name}-{self.text}" title="{self.text}"></span>'
        node = nodes.raw("", nodes.Text(svg), format="html")
        self.set_source_info(node)
        return [node], []