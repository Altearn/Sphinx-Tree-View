# Sphinx Tree View

A lightweight Sphinx extension that provides a customizable tree view for documentation.
A tree view can have an associated decorator type, which can be used to add custom icons to the tree view.
By default, the extension provides a decorator type "dir" with file and folder icons.

## Installation

```sh
pip install sphinx-treeview
```

## Basic Usage

Add the extension to your Sphinx `conf.py`:

```python
extensions = [
    'sphinx_treeview'
]
```

Use the directive in your RST files:

```rst
:::{treeview}
- {<decorator name>}`<icon1>` foo
  - {<decorator name>}`<icon2>` bar
- <decorator>`<icon1>` baz
:::
```

For example, with the default decorator "dir":

```rst
:::{treeview}
- {dir}`<folder>` folder
  - {dir}`<file>` file.jpeg
  - {dir}`<file>` file.png
:::
```

The rendered tree view will look like this:

![Tree View](imgs/example.png)

## Configuration Options

The following options can be configured in your `conf.py`:

```python
# Add custom decorators
stv_decorators = [
    DecoratorType(name="custom", icons=[DecoratorIcon(path="path/to/icon.svg", sphinx_static_path="icon/path/for/sphinx/", width=1.3, height=1.3, css_properties={...})])
]

# Disable default decorators (dir decorator)
stv_disable_default_decorators = False
```

A decorator icon is defined by a `path` to the icon file, and the path where the icon will be copied to in the Sphinx static folder.
This second path is used in the CSS to load the icon.
`width` and `height` are the dimensions of the icon in `em`, and `css_properties` is a dictionary of CSS properties to be applied to the icon.
The name used for the icon in the tree view is the name of the icon file without the extension.

If you want to load all images of a folder as icons, you can use the `imagesToDecoratorIcons` function:

```python
icons = imagesToDecoratorIcons(path="path/to/folder", sphinx_static_path="path/to/sphinx/folder")
```

By default, the dimensions of the icons are 1.3em × 1.3em.

# License

This project is licensed under the MPL-2.0 License. See the [LICENSE](LICENSE) file for details.
Images came from [pictogrammers](https://pictogrammers.com/library/mdi/) and are under [Apache-2.0 License](https://pictogrammers.com/docs/general/license/).