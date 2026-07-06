from json_presenter.enums import ViewType
from json_presenter.models import AnalysisResult, ViewRecommendation
from json_presenter.recommenders.rules.base import ViewRule


class TableRule(ViewRule):
    """Recommend table view for list-of-dicts data."""

    def recommend(self, analysis: AnalysisResult) -> ViewRecommendation | None:
        if analysis.is_list_of_dicts:
            return ViewRecommendation(
                view=ViewType.TABLE,
                confidence=0.95,
                reason="The JSON root is a list of objects, which fits a table layout.",
            )

        return None
