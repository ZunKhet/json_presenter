from json_presenter.themes.base import BaseTheme


class SpringTheme(BaseTheme):
    """Soft spring-inspired theme."""

    def variables(self) -> str:
        return """
:root {
    --jp-bg: #f3fff3;
    --jp-surface: #ffffff;
    --jp-surface-soft: #eaf8e8;
    --jp-text: #244b2a;
    --jp-title: #14532d;
    --jp-muted: #5f7f62;
    --jp-key: #15803d;
    --jp-value: #1f3d25;
    --jp-border: #c7e8c7;
    --jp-font-family: Arial, sans-serif;
    --jp-radius: 18px;
    --jp-shadow: 0 10px 28px rgba(21, 128, 61, 0.12);

    --jp-space-sm: 0.5rem;
    --jp-space-md: 1rem;
    --jp-space-lg: 1.5rem;
    --jp-space-xl: 2.5rem;
}
"""
