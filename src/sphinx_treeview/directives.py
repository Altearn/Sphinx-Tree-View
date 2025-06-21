from docutils import nodes
from sphinx.util.docutils import SphinxDirective


class TreeViewDirective(SphinxDirective):
    has_content = True

    def run(self):
        container = nodes.container(classes=["treeview"])

        node_list = nodes.Element()
        self.state.nested_parse(self.content, self.content_offset, node_list)

        bullet_list = next((n for n in node_list if isinstance(n, nodes.bullet_list)), None)
        if bullet_list is None:
            raise self.error("Expected a list in directive content")

        for list_item in bullet_list.traverse(nodes.list_item):
            if list_item.children and isinstance(list_item.children[0], nodes.paragraph):
                marker = self._extract_marker(list_item.children[0])
                if marker is not None:
                    if not any(isinstance(child, nodes.bullet_list) for child in list_item.children):
                        msg = f"Collapse indicator '{marker}' used on item without nested list at line {list_item.line or 'unknown'}"
                        reporter = self.state.document.reporter
                        reporter.warning(msg, line=list_item.line)
                        continue
                    list_item["classes"].append("collapsible")
                    list_item["classes"].append("collapsed" if marker == "[-]" else "")

        container += bullet_list
        return [container]


    def _extract_marker(self, paragraph: nodes.paragraph) -> str | None:
        """
        Detect and remove a leading marker in paragraph text.
        Supported markers: "[-]" (collapsed), "[+]" (expanded).
        Returns the marker string if found, else None.
        """
        if paragraph.children and isinstance(paragraph.children[0], nodes.Text):
            node = paragraph.children[0]
            text = node.astext()
            for marker in ("[-]", "[+]"):
                if text.startswith(marker):
                    new_text = text[len(marker):].lstrip()
                    paragraph.replace(node, nodes.Text(new_text))
                    return marker
        return None
