from json_presenter.themes.base import BaseTheme


class WinterTheme(BaseTheme):
    """Cool winter-inspired theme."""

    def variables(self) -> str:
        return """
:root {
    --jp-bg: #f1f8ff;
    --jp-surface: #ffffff;
    --jp-surface-soft: #e8f3ff;
    --jp-text: #1d3557;
    --jp-title: #0f2742;
    --jp-muted: #5b7894;
    --jp-key: #2563eb;
    --jp-value: #132f4c;
    --jp-border: #cfe3f7;
    --jp-font-family: Arial, sans-serif;
    --jp-radius: 16px;
    --jp-shadow: 0 10px 28px rgba(37, 99, 235, 0.12);

    --jp-space-sm: 0.5rem;
    --jp-space-md: 1rem;
    --jp-space-lg: 1.5rem;
    --jp-space-xl: 2.5rem;
}
"""
