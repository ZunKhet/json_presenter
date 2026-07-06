from __future__ import annotations

from dataclasses import dataclass
from html import escape
from re import match


@dataclass(frozen=True)
class FormattedValue:
    html: str


URL_PATTERN = r"^https?://[^\s]+$"
EMAIL_PATTERN = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
DATE_PATTERN = r"^\d{4}-\d{2}-\d{2}"
DATETIME_PATTERN = r"^\d{4}-\d{2}-\d{2}T"


def format_value(value: object) -> FormattedValue:
    if value is None:
        return FormattedValue('<span class="jp-value-muted">Not available</span>')

    if isinstance(value, bool):
        text = "Yes" if value else "No"
        symbol = "✓" if value else "✕"
        return FormattedValue(f'<span class="jp-value-boolean">{symbol} {text}</span>')

    text = str(value)

    if match(URL_PATTERN, text):
        escaped = escape(text)
        return FormattedValue(
            f'<a class="jp-value-link" href="{escaped}" target="_blank" rel="noopener noreferrer">{escaped}</a>'
        )

    if match(EMAIL_PATTERN, text):
        escaped = escape(text)
        return FormattedValue(
            f'<a class="jp-value-link" href="mailto:{escaped}">{escaped}</a>'
        )

    if match(DATETIME_PATTERN, text):
        return FormattedValue(
            f'<span class="jp-value-date">{escape(text.replace("T", " "))}</span>'
        )

    if match(DATE_PATTERN, text):
        return FormattedValue(f'<span class="jp-value-date">{escape(text)}</span>')

    return FormattedValue(escape(text))
