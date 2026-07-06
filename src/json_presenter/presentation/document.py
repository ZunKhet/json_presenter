from dataclasses import dataclass

from json_presenter.enums import ViewType
from json_presenter.presentation.nodes import PresentationNode


@dataclass(frozen=True)
class PresentationDocument:
    view: ViewType
    nodes: list[PresentationNode]
    title: str = "JSON Presentation"
    subtitle: str | None = None
    description: str | None = None
