from json_presenter.themes.base import BaseTheme


class SummerTheme(BaseTheme):
    """Warm summer-inspired theme."""

    def variables(self) -> str:
        return """
:root {
    --jp-bg: #fff8e6;
    --jp-surface: #ffffff;
    --jp-surface-soft: #fff1c2;
    --jp-text: #4a3416;
    --jp-title: #8a4b00;
    --jp-muted: #9a6b2f;
    --jp-key: #b45309;
    --jp-value: #3f2a12;
    --jp-border: #f2c879;
    --jp-font-family: Arial, sans-serif;
    --jp-radius: 18px;
    --jp-shadow: 0 10px 28px rgba(180, 83, 9, 0.14);

    --jp-space-sm: 0.5rem;
    --jp-space-md: 1rem;
    --jp-space-lg: 1.5rem;
    --jp-space-xl: 2.5rem;
}
"""
