# Sphinx Tree View

<!-- start-include-here -->

A lightweight Sphinx extension that provides a customizable, filesystem-like tree view for your documentation.

## Installation

Install the extension via PyPI:

```sh
pip install sphinx-treeview
```

Then, add it to the `extensions` list in your `conf.py`:

```python
extensions = ["sphinx_treeview"]
```

If you are using [MyST Parser](https://github.com/executablebooks/myst-parser) to write Markdown documentation, it’s recommended to enable the `colon_fence` syntax extension:

```python
extensions = ["myst_parser", "sphinx_treeview"]
myst_enable_extensions = ["colon_fence"]
```

<!-- end-include-here -->

## Example

![Example Image](https://raw.githubusercontent.com/Altearn/Sphinx-Tree-View/main/docs/_static/example.png)

```md
:::{treeview}
- {dir}`folder` folder
  - {dir}`file` file.jpeg
  - {dir}`file` file.png
:::
```

# License

This project is licensed under the MPL-2.0 License. See the [LICENSE](LICENSE) file for details.
Images came from [pictogrammers](https://pictogrammers.com/library/mdi/) and are under [Apache-2.0 License](https://pictogrammers.com/docs/general/license/).
