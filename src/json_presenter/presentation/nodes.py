from dataclasses import dataclass

from json_presenter.presentation.card_fields import CardContent


@dataclass(frozen=True)
class PresentationNode:
    pass


@dataclass(frozen=True)
class TextNode(PresentationNode):
    text: str


@dataclass(frozen=True)
class CardNode(PresentationNode):
    title: str
    fields: list[CardContent]


@dataclass(frozen=True)
class TableNode(PresentationNode):
    headers: list[str]
    rows: list[dict]


@dataclass(frozen=True)
class TreeNode(PresentationNode):
    label: str
    children: list["TreeNode"]
