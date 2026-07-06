from typing import Any

from json_presenter.models import AnalysisResult


class StructureAnalyzer:
    """Analyze the structure of JSON-compatible Python data."""

    def analyze(self, data: Any) -> AnalysisResult:
        return AnalysisResult(
            root_type=self._get_type_name(data),
            depth=self._calculate_depth(data),
            total_keys=self._count_keys(data),
            total_items=self._count_items(data),
            is_list_of_dicts=self._is_list_of_dicts(data),
        )

    def _get_type_name(self, value: Any) -> str:
        return type(value).__name__

    def _calculate_depth(self, value: Any) -> int:
        if isinstance(value, dict):
            if not value:
                return 1
            return 1 + max(self._calculate_depth(v) for v in value.values())

        if isinstance(value, list):
            if not value:
                return 1
            return 1 + max(self._calculate_depth(item) for item in value)

        return 0

    def _count_keys(self, value: Any) -> int:
        if isinstance(value, dict):
            return len(value) + sum(self._count_keys(v) for v in value.values())

        if isinstance(value, list):
            return sum(self._count_keys(item) for item in value)

        return 0

    def _count_items(self, value: Any) -> int:
        if isinstance(value, list):
            return len(value) + sum(self._count_items(item) for item in value)

        if isinstance(value, dict):
            return sum(self._count_items(v) for v in value.values())

        return 0

    def _is_list_of_dicts(self, value: Any) -> bool:
        return (
            isinstance(value, list)
            and len(value) > 0
            and all(isinstance(item, dict) for item in value)
        )
