from base64 import b64encode
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Dict
from urllib.parse import quote


VALID_EXTENSIONS = {
    '.png',
    '.svg',
    '.jpg',
    '.jpeg',
    '.gif',
    '.bmp',
}


@dataclass
class DecoratorType:
    """Represents a type of decorator with a name and associated icons."""
    name: str
    icons: List["DecoratorIcon"]


@dataclass
class DecoratorIcon:
    """Represents an icon for a decorator."""
    path: Path
    name: str
    width: Optional[float | str] = None
    height: Optional[float | str] = None
    css_properties: Dict[str, str] = field(default_factory=dict)

    @property
    def style(self) -> str:
        """Generate CSS style string for the icon."""
        props = self.css_properties
        props["width"] = f"{self.width}em" if isinstance(self.width, (int, float)) else self.width
        props["height"] = f"{self.height}em" if isinstance(self.height, (int, float)) else self.height

        if self.path.suffix == '.svg':
            data = self.path.read_text(encoding='utf-8')
            props["background-image"] = f"url('data:image/svg+xml;utf-8,{quote(data)}')"
        else:
            mime = f"image/{self.path.suffix[1:]}"
            data = b64encode(self.path.read_bytes()).decode('ascii')
            props["background-image"] = f"url('data:{mime};base64,{data}')"

        return ";".join(f"{k}: {v}" for k, v in props.items() if v is not None) + ";"


def imagesToDecoratorIcons(
    path: str,
    width: Optional[float | str] = None,
    height: Optional[float | str] = None,
    css_properties: Optional[Dict[str, str]] = None,
    **kwargs,  # catch legacy params (like sphinx_static_path)
) -> List[DecoratorIcon]:
    """Legacy function kept for backward compatibility.

    This wraps the new `images_to_decorator_icons` function, converting
    the old camelCase usage to the new snake_case API.

    Args and behavior same as `images_to_decorator_icons`.
    """
    return images_to_decorator_icons(path, width, height, css_properties)


def images_to_decorator_icons(
    path: Path,
    width: Optional[float | str] = None,
    height: Optional[float | str] = None,
    css_properties: Optional[Dict[str, str]] = None,
) -> List[DecoratorIcon]:
    """Load all images in a folder as DecoratorIcon instances.

    Parameters
    ----------
    path : Path
        Path to a directory containing image files.
    width : float, str, optional
        Width to assign to each icon (default is None).
    height : float, str, optional
        Height to assign to each icon (default is None).
    css_properties : dict[str, str], optional
        Optional dictionary of CSS styles to apply to icons.

    Returns
    -------
    List[DecoratorIcon]
        List of DecoratorIcon objects representing each image file in the folder.

    Raises
    ------
    FileNotFoundError
        If the provided path does not exist.
    NotADirectoryError
        If the provided path is not a directory.
    """

    directory = Path(path)
    if not directory.exists():
        raise FileNotFoundError(f"Provided path does not exist: {path}")
    if not directory.is_dir():
        raise NotADirectoryError(f"Provided path is not a directory: {path}")

    if css_properties is None:
        css_properties = {}

    return [
        DecoratorIcon(
            path=file,
            name=file.stem,
            width=width,
            height=height,
            css_properties=css_properties,
        )
        for file in directory.iterdir()
        if file.is_file() and file.suffix.lower() in VALID_EXTENSIONS
    ]
