from typing import Any

from json_presenter.enums import ViewType
from json_presenter.presentation import PresentationDocument, TableNode
from json_presenter.presenters.base import BasePresenter


class TablePresenter(BasePresenter):
    """Build a table presentation document."""

    def build_document(self, data: Any) -> PresentationDocument:
        if not self._is_list_of_dicts(data):
            return PresentationDocument(
                view=ViewType.TABLE,
                nodes=[
                    TableNode(
                        headers=["value"],
                        rows=[{"value": data}],
                    )
                ],
            )

        headers = self._extract_headers(data)

        return PresentationDocument(
            view=ViewType.TABLE,
            nodes=[
                TableNode(
                    headers=headers,
                    rows=data,
                )
            ],
        )

    def _is_list_of_dicts(self, data: Any) -> bool:
        return (
            isinstance(data, list)
            and len(data) > 0
            and all(isinstance(item, dict) for item in data)
        )

    def _extract_headers(self, rows: list[dict[str, Any]]) -> list[str]:
        headers: list[str] = []

        for row in rows:
            for key in row:
                if key not in headers:
                    headers.append(key)

        return headers
