from dataclasses import dataclass

from json_presenter.enums import ViewType


@dataclass(frozen=True)
class ViewRecommendation:
    view: ViewType
    confidence: float
    reason: str
