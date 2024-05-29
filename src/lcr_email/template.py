"""
Email template parsing and rendering.
"""

import os
from pathlib import Path
from typing import Any, TypeAlias

import frontmatter
import markdown2

FileName: TypeAlias = str | os.PathLike


class EmailTemplate:
    """
    Parse and load a email template file.
    """

    def __init__(self, filepath: FileName):
        """
        Args:
            filepath (FileName): Path to the email template

        Raises:
            FileNotFoundError: When file doesn't exist

        """
        path = Path(filepath)
        if not path.is_file():
            raise FileNotFoundError(f"No such file {path}")

        with path.open("rt") as fp:
            doc = frontmatter.load(fp)

        self._metadata = doc.metadata
        self._content = markdown2.markdown(doc.content)

    @property
    def content(self) -> str | None:
        """
        Get the email template content

        Returns:
            str | None: _description_
        """
        return self._content

    @property
    def metadata(self) -> dict[str, Any]:
        """
        Get the email template metadata

        Returns:
            dict[str, Any]: _description_
        """
        return self._metadata
