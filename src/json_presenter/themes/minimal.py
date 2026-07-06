from json_presenter.themes.base import BaseTheme


class MinimalTheme(BaseTheme):
    """Clean minimal theme."""

    def variables(self) -> str:
        return """
:root {
    --jp-bg: #ffffff;
    --jp-surface: #ffffff;
    --jp-surface-soft: #f8fafc;
    --jp-text: #1f2937;
    --jp-title: #111827;
    --jp-muted: #6b7280;
    --jp-border: #e5e7eb;
    --jp-font-family: Arial, sans-serif;
    --jp-radius: 14px;
    --jp-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);

    --jp-space-sm: 0.5rem;
    --jp-space-md: 1rem;
    --jp-space-lg: 1.5rem;
    --jp-space-xl: 2.5rem;
    --jp-key: #4b5563;
    --jp-value: #111827;
}
"""
