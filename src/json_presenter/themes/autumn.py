from json_presenter.themes.base import BaseTheme


class AutumnTheme(BaseTheme):
    """Earthy autumn-inspired theme."""

    def variables(self) -> str:
        return """
:root {
    --jp-bg: #fff4e8;
    --jp-surface: #fffaf5;
    --jp-surface-soft: #fde7d3;
    --jp-text: #4b2e1f;
    --jp-title: #7c2d12;
    --jp-muted: #8b5e3c;
    --jp-key: #9a3412;
    --jp-value: #3b2418;
    --jp-border: #e7b48f;
    --jp-font-family: Georgia, serif;
    --jp-radius: 16px;
    --jp-shadow: 0 12px 30px rgba(124, 45, 18, 0.16);

    --jp-space-sm: 0.5rem;
    --jp-space-md: 1rem;
    --jp-space-lg: 1.5rem;
    --jp-space-xl: 2.5rem;
}
"""
