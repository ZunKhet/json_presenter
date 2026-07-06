from json_presenter.themes.base import BaseTheme


class DarkDeveloperTheme(BaseTheme):
    """Dark developer-inspired theme."""

    def variables(self) -> str:
        return """
:root {
    --jp-bg: #1e1e1e;
    --jp-surface: #252526;
    --jp-surface-soft: #2d2d30;
    --jp-text: #d4d4d4;
    --jp-title: #ffffff;
    --jp-muted: #9ca3af;
    --jp-border: #3f3f46;
    --jp-font-family: "Courier New", monospace;
    --jp-radius: 12px;
    --jp-shadow: 0 12px 32px rgba(0, 0, 0, 0.35);

    --jp-space-sm: 0.5rem;
    --jp-space-md: 1rem;
    --jp-space-lg: 1.5rem;
    --jp-space-xl: 2.5rem;
    --jp-key: #60a5fa;
    --jp-value: #e5e7eb;
}
"""
