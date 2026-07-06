from json_presenter.models import AnalysisResult, ViewRecommendation
from json_presenter.recommenders.rules import CardRule, TableRule, TreeRule, ViewRule


class ViewRecommender:
    """Recommend suitable presentation views based on JSON analysis."""

    def __init__(self, rules: list[ViewRule] | None = None):
        self._rules = rules or [
            TableRule(),
            CardRule(),
            TreeRule(),
        ]

    def recommend(self, analysis: AnalysisResult) -> list[ViewRecommendation]:
        recommendations: list[ViewRecommendation] = []

        for rule in self._rules:
            recommendation = rule.recommend(analysis)

            if recommendation is not None:
                recommendations.append(recommendation)

        return sorted(
            recommendations,
            key=lambda item: item.confidence,
            reverse=True,
        )
