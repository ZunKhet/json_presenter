from json_presenter.themes import (
    DarkDeveloperTheme,
    DigitalTheme,
    MinimalTheme,
    SpringTheme,
    WinterTheme,
)
from json_presenter.themes import AutumnTheme, SummerTheme


def test_minimal_theme_returns_css():
    css = MinimalTheme().css()

    assert ":root" in css
    assert "--jp-bg" in css
    assert ".jp-card" in css
    assert "--jp-key" in css
    assert "--jp-value" in css


def test_digital_theme_returns_css():
    css = DigitalTheme().css()

    assert "--jp-title: #00ffcc" in css
    assert "monospace" in css
    assert ".jp-table" in css
    assert "--jp-key" in css
    assert "--jp-value" in css


def test_spring_theme_returns_css():
    css = SpringTheme().css()

    assert "--jp-bg: #f3fff3" in css
    assert ".jp-document-header" in css
    assert "--jp-key" in css
    assert "--jp-value" in css


def test_winter_theme_returns_css():
    css = WinterTheme().css()

    assert "--jp-bg: #f1f8ff" in css
    assert ".jp-tree" in css
    assert "--jp-key" in css
    assert "--jp-value" in css


def test_dark_developer_theme_returns_css():
    css = DarkDeveloperTheme().css()

    assert "--jp-bg: #1e1e1e" in css
    assert ".jp-content" in css
    assert "--jp-key" in css
    assert "--jp-value" in css


def test_summer_theme_returns_css():
    css = SummerTheme().css()

    assert "--jp-bg: #fff8e6" in css
    assert "--jp-key" in css
    assert "--jp-value" in css


def test_autumn_theme_returns_css():
    css = AutumnTheme().css()

    assert "--jp-bg: #fff4e8" in css
    assert "--jp-key" in css
    assert "--jp-value" in css
