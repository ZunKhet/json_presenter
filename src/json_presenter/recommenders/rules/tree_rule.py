from json_presenter.enums import ViewType
from json_presenter.models import AnalysisResult, ViewRecommendation
from json_presenter.recommenders.rules.base import ViewRule


class TreeRule(ViewRule):
    """Recommend tree view for nested JSON data."""

    def recommend(self, analysis: AnalysisResult) -> ViewRecommendation | None:
        if analysis.depth >= 3:
            return ViewRecommendation(
                view=ViewType.TREE,
                confidence=0.9,
                reason="The JSON has nested structure, which fits a tree layout.",
            )

        return ViewRecommendation(
            view=ViewType.TREE,
            confidence=0.6,
            reason="Tree view is a safe default for general JSON structures.",
        )
