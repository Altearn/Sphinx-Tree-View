# Quickstart

A tree view can have an associated *decorator type*, which is used to add custom icons to the tree.
By default, this extension provides a `dir` decorator type with basic `file` and `folder` icons.


---

## Basic Syntax

Use the `treeview` directive to display interactive file or folder trees in your documentation.

```{eval-rst}
.. treeview::
  - :dir:`folder` My Folder

    - :dir:`file` image.png
    - :dir:`file` document.pdf
```

`````{tab} MyST (Colon Fence)
  ```md
  :::{treeview}
  - {dir}`folder` My Folder
    - {dir}`file` image.png
    - {dir}`file` document.pdf
  :::
  ```
`````
`````{tab} MyST (Directive Fence)
  ````md
  ```{treeview}
  - {dir}`folder` My Folder
    - {dir}`file` image.png
    - {dir}`file` document.pdf
  ```
`````
`````{tab} RST
  ```rst
  .. treeview::
    - :dir:`folder` My Folder

      - :dir:`file` image.png
      - :dir:`file` document.pdf
  ```
`````

---

## Custom Icons

The `dir` decorator provides the default `folder` and `file` icons.
To add more icons, define **custom decorators** in your configuration.
For setup instructions, see the [Configuration](./config.md) section.

Once defined, custom decorators are used like this:

```md
:::{treeview}
- {<decorator-type>}`<icon1>` foo
  - {<decorator-type>}`<icon2>` bar
- {<other-decorator>}`<icon1>` baz
:::
```

---

## Collapsible Nodes

You can control whether nodes in the tree are expanded or collapsed by default using the following markers:

- `[-]`: Collapsed by default
- `[+]`: Expanded by default

```{warning}
Collapse markers should only be used on list items **that contain nested lists**.
If used on items without children, the indicator will be ignored or may produce warnings.
```

:::{treeview}
- [+] {dir}`folder` Open Folder
  - {dir}`file` document.pdf
- [-] {dir}`folder` Collapsed Folder
  - {dir}`file` secret.txt
:::


```md
:::{treeview}
- [+] {dir}`folder` Open Folder
  - {dir}`file` document.pdf
- [-] {dir}`folder` Collapsed Folder
  - {dir}`file` secret.txt
:::
```
