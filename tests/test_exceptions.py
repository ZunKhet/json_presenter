import pytest

from json_presenter import (
    InvalidJsonError,
    Presenter,
    UnknownThemeError,
    UnknownViewError,
)
from json_presenter.rendering import PresenterRegistry, ThemeRegistry


def test_invalid_json_string_raises_custom_exception():
    with pytest.raises(InvalidJsonError):
        Presenter.from_string("{invalid json}")


def test_invalid_json_file_raises_custom_exception(tmp_path):
    file_path = tmp_path / "bad.json"
    file_path.write_text("{invalid json}", encoding="utf-8")

    with pytest.raises(InvalidJsonError):
        Presenter.from_file(file_path)


def test_unknown_view_raises_custom_exception():
    registry = PresenterRegistry()

    with pytest.raises(UnknownViewError):
        registry.get("unknown")  # type: ignore[arg-type]


def test_unknown_theme_raises_custom_exception():
    registry = ThemeRegistry()

    with pytest.raises(UnknownThemeError):
        registry.get("unknown")  # type: ignore[arg-type]
