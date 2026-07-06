from json_presenter.enums import ViewType
from json_presenter.models import AnalysisResult, ViewRecommendation
from json_presenter.recommenders.rules.base import ViewRule


class CardRule(ViewRule):
    """Recommend card view for object-like JSON data."""

    def recommend(self, analysis: AnalysisResult) -> ViewRecommendation | None:
        if analysis.root_type == "dict" and analysis.depth <= 2:
            return ViewRecommendation(
                view=ViewType.CARDS,
                confidence=0.85,
                reason="The JSON is a shallow object, which fits a card layout.",
            )

        return None
