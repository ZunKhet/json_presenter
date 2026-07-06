from typing import Any

from json_presenter.enums import ThemeType, ViewType
from json_presenter.rendering.html_renderer import HtmlRenderer
from json_presenter.rendering.presenter_registry import PresenterRegistry
from json_presenter.rendering.theme_registry import ThemeRegistry
from json_presenter.models import RenderedPresentation


class RenderEngine:
    """Coordinate presenters, themes, and HTML rendering."""

    def __init__(
        self,
        presenter_registry: PresenterRegistry | None = None,
        theme_registry: ThemeRegistry | None = None,
        html_renderer: HtmlRenderer | None = None,
    ):
        self._presenter_registry = presenter_registry or PresenterRegistry()
        self._theme_registry = theme_registry or ThemeRegistry()
        self._html_renderer = html_renderer or HtmlRenderer()

    def render(
        self,
        data: Any,
        view: ViewType,
        theme: ThemeType = ThemeType.MINIMAL,
        root_key: str | None = None,
    ) -> str:
        if root_key is not None:
            data = self._select_root(data, root_key)

        presenter_class = self._presenter_registry.get(view)
        theme_class = self._theme_registry.get(theme)

        presenter = presenter_class()
        theme_instance = theme_class()

        document = presenter.build_document(data)
        body_fragment = self._html_renderer.render(document)

        html = self._compose_html(
            body_fragment=body_fragment,
            css=theme_instance.css(),
        )

        return RenderedPresentation(html=html)

    def _select_root(self, data: Any, root_key: str) -> Any:
        if not isinstance(data, dict):
            raise KeyError(
                f"Cannot select root key '{root_key}' from non-object JSON.")

        if root_key not in data:
            raise KeyError(f"Root key not found: {root_key}")

        return data[root_key]

    def _compose_html(self, body_fragment: str, css: str) -> str:
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>json_presenter output</title>
    <style>
{css}
    </style>
</head>
<body>
    <main class="jp-root">
{body_fragment}
    </main>
</body>
</html>
"""
