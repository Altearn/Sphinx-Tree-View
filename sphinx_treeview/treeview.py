from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective

class TreeViewDirective(SphinxDirective):
    has_content = True

    def run(self):
        container = nodes.container()
        container.set_class("stv")
        
        if not self.options.get('collapsible', True):
            container.set_class("no-collapse")
            
        list_node = nodes.bullet_list()
        list_nodes = [list_node]

        for line in self.content:
            indent_level = (len(line) - len(line.lstrip('- ')) - 1) // 2
            text = line.lstrip('- ')

            while len(list_nodes) <= indent_level:
                new_item_node = nodes.list_item()
                if not list_nodes[-1].children or not isinstance(list_nodes[-1].children[-1], nodes.list_item):
                    list_nodes[-1] += new_item_node
                new_list_node = nodes.bullet_list()
                
                collapse_trigger = nodes.raw('', '<span class="collapse-trigger"></span>', format='html')
                new_item_node += collapse_trigger
                
                list_nodes[-1].children[-1] += new_list_node
                list_nodes.append(new_list_node)

            item_node = nodes.list_item()
            item_node.extend(self.state.inline_text(text, self.lineno)[0])
            list_nodes[indent_level] += item_node
            list_nodes = list_nodes[:indent_level+1]

        container.append(list_node)
        return [container]