# Configuration

This page describes the available configuration options for customizing the behavior and appearance of the tree view.

---

## Custom Icons

The following options can be configured in your `conf.py`:

```python
from sphinx_treeview.decorator import DecoratorType, DecoratorIcon

# Disable default decorators (e.g., the dir decorator)
stv_disable_default_decorators = False

# Add custom decorators
stv_decorators = [
    DecoratorType(
        name="custom",
        icons=[
            DecoratorIcon(
                path="path/to/icon.svg",
                width=None,
                height=None,
                css_properties={...},
            )
        ]
    )
]
```

```{important}
In your documentation, decorators are referenced by roles, for example: ``{dir}`folder` ...``.
The icon name used in the tree view corresponds to the icon file’s name **without** its extension.
```

- The optional `width` and `height` parameters define the icon’s size. They accept either:
  - A **valid CSS size string** (e.g., `16px`, `1.5em`)
  - A **number**, interpreted as `em` units (e.g., `1.3` → `1.3em`)
- The optional `css_properties` dictionary allows adding custom CSS styles to the icon.

While `width`, `height`, and `css_properties` are available for convenience, **using CSS is generally recommended** for advanced styling. See the [Custom Styles](#custom-styles) section.

To load all images from a folder as icons, use the `images_to_decorator_icons` helper:

```python
from sphinx_treeview.decorator import images_to_decorator_icons

icons = images_to_decorator_icons(path="path/to/folder")
```

---

## Custom Styles

This extension exposes the following CSS variables for customizing the tree view’s appearance:

```css
:root {
  --treeview-indent: 1.5rem;
  --treeview-spacing: 0.2rem;
  --treeview-icon-width: 1.3em;
  --treeview-icon-height: 1.3em;
  --treeview-color: oklch(0.5 0 0);
  --treeview-thickness: 1px;
}
```

Adjust these variables in your custom stylesheet to control indentation, icon sizing, colors, and line thickness.
