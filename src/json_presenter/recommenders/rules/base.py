from abc import ABC, abstractmethod

from json_presenter.models import AnalysisResult, ViewRecommendation


class ViewRule(ABC):
    """Base class for all view recommendation rules."""

    @abstractmethod
    def recommend(self, analysis: AnalysisResult) -> ViewRecommendation | None:
        """Return a recommendation or None."""
        raise NotImplementedError
