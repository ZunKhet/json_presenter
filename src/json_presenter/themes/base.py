from abc import ABC, abstractmethod

from json_presenter.themes.base_styles import BASE_STYLES


class BaseTheme(ABC):
    """Base interface for all themes."""

    def css(self) -> str:
        return f"""
{self.variables()}

{BASE_STYLES}
"""

    @abstractmethod
    def variables(self) -> str:
        """Return CSS custom properties for this theme."""
        raise NotImplementedError
