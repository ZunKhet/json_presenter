from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from json_presenter.analyzer import StructureAnalyzer
from json_presenter.enums import ThemeType, ViewType
from json_presenter.exceptions import InvalidJsonError
from json_presenter.models import AnalysisResult, ViewRecommendation
from json_presenter.recommenders import ViewRecommender
from json_presenter.rendering import RenderEngine
from json_presenter.models import AnalysisResult, RenderedPresentation, ViewRecommendation


class Presenter:
    """Main entry point of json_presenter."""

    def __init__(self, data: Any):
        self._data = data
        self._analyzer = StructureAnalyzer()
        self._recommender = ViewRecommender()
        self._render_engine = RenderEngine()

    @property
    def data(self) -> Any:
        return self._data

    @classmethod
    def from_object(cls, obj: Any) -> "Presenter":
        return cls(obj)

    @classmethod
    def from_string(cls, json_string: str) -> "Presenter":
        try:
            data = json.loads(json_string)
        except json.JSONDecodeError as exc:
            raise InvalidJsonError("Invalid JSON string.") from exc

        return cls(data)

    @classmethod
    def from_file(cls, file_path: str | Path) -> "Presenter":
        path = Path(file_path)

        try:
            with path.open("r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as exc:
            raise InvalidJsonError(f"Invalid JSON file: {path}") from exc

        return cls(data)

    def analyze(self) -> AnalysisResult:
        return self._analyzer.analyze(self._data)

    def recommend_views(self) -> list[ViewRecommendation]:
        analysis = self.analyze()
        return self._recommender.recommend(analysis)

    def render(
        self,
        view: ViewType,
        theme: ThemeType = ThemeType.MINIMAL,
        root_key: str | None = None,
    ) -> RenderPresentation:
        return self._render_engine.render(
            data=self._data,
            view=view,
            theme=theme,
            root_key=root_key,
        )
