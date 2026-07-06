from json_presenter import Presenter, ThemeType, ViewType
from json_presenter.rendering import RenderEngine
import pytest


def test_render_engine_returns_complete_html_document():
    engine = RenderEngine()

    html = engine.render(
        data={"name": "Alice"},
        view=ViewType.CARDS,
        theme=ThemeType.MINIMAL,
    )

    assert "<!DOCTYPE html>" in html.html
    assert "<html" in html.html
    assert "<style>" in html.html
    assert "jp-root" in html.html
    assert "Alice" in html.html


def test_render_engine_uses_selected_theme():
    engine = RenderEngine()

    html = engine.render(
        data={"name": "Alice"},
        view=ViewType.CARDS,
        theme=ThemeType.WINTER,
    )

    assert "#f1f8ff" in html.html


def test_render_engine_uses_selected_view():
    engine = RenderEngine()

    html = engine.render(
        data=[{"name": "Alice"}],
        view=ViewType.TABLE,
        theme=ThemeType.MINIMAL,
    )

    assert "<table" in html.html
    assert "Alice" in html.html


def test_presenter_render_public_api():
    presenter = Presenter.from_object({"name": "Alice"})

    html = presenter.render(
        view=ViewType.CARDS,
        theme=ThemeType.WINTER,
    )

    assert "<!DOCTYPE html>" in html.html
    assert "#f1f8ff" in html.html
    assert "Alice" in html.html


def test_presenter_render_with_root_key():
    presenter = Presenter.from_object(
        {
            "project": {
                "name": "json_presenter",
                "version": "0.1.0",
            }
        }
    )

    html = presenter.render(
        view=ViewType.CARDS,
        theme=ThemeType.WINTER,
        root_key="project",
    )

    assert "json_presenter" in html.html
    assert "0.1.0" in html.html
    assert "project" not in html.html


def test_presenter_render_with_missing_root_key_raises_error():
    presenter = Presenter.from_object({"project": {"name": "json_presenter"}})

    with pytest.raises(KeyError):
        presenter.render(
            view=ViewType.CARDS,
            root_key="missing",
        )
