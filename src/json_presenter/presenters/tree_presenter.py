from typing import Any

from json_presenter.enums import ViewType
from json_presenter.presentation import PresentationDocument, TreeNode
from json_presenter.presenters.base import BasePresenter


class TreePresenter(BasePresenter):
    """Build a tree presentation document."""

    def build_document(self, data: Any) -> PresentationDocument:
        root = self._build_tree("root", data)

        return PresentationDocument(
            view=ViewType.TREE,
            nodes=[root],
        )

    def _build_tree(self, label: str, value: Any) -> TreeNode:
        if isinstance(value, dict):
            children = [
                self._build_tree(str(key), child_value)
                for key, child_value in value.items()
            ]

            return TreeNode(
                label=label,
                children=children,
            )

        if isinstance(value, list):
            children = [
                self._build_tree(f"[{index}]", item)
                for index, item in enumerate(value)
            ]

            return TreeNode(
                label=label,
                children=children,
            )

        return TreeNode(
            label=f"{label}: {value}",
            children=[],
        )
