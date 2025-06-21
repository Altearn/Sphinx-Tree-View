# Sphinx Tree View

```{include} ../README.md
:start-after: <!-- start-include-here -->
:end-before: <!-- end-include-here -->
```

## Examples

A basic tree structure with one folder and two files:

:::{treeview}
- {dir}`folder` folder
  - {dir}`file` file.jpeg
  - {dir}`file` file.png
:::

A collapsible tree with nested folders, one collapsed by default:

:::{treeview}
- [-] {dir}`folder` folder
  - [+] {dir}`folder` user
    - {dir}`file` notes.txt
  - [-] {dir}`folder` not-a-secret
    - {dir}`file` secret.txt
:::


```{toctree}
:hidden:
usage
config
```

```{toctree}
:caption: Useful Links
:hidden:
PyPI page <https://pypi.org/project/sphinx-treeview>
GitHub Repository <https://github.com/Altearn/Sphinx-Tree-View>
```
