from json_presenter.themes.base import BaseTheme


class DigitalTheme(BaseTheme):
    """Digital-style theme."""

    def variables(self) -> str:
        return """
:root {
    --jp-bg: #041f1e;
    --jp-surface: #082f2d;
    --jp-surface-soft: #0b3d39;
    --jp-text: #d7fff7;
    --jp-title: #00ffcc;
    --jp-muted: #7ee8d7;
    --jp-border: #0f766e;
    --jp-font-family: "Courier New", monospace;
    --jp-radius: 10px;
    --jp-shadow: 0 0 28px rgba(0, 255, 204, 0.18);

    --jp-space-sm: 0.5rem;
    --jp-space-md: 1rem;
    --jp-space-lg: 1.5rem;
    --jp-space-xl: 2.5rem;
    --jp-key: #00ffcc;
    --jp-value: #d7fff7;
}
"""
