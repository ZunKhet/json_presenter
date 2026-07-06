from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    from json_presenter.presentation.nodes import CardNode


@dataclass(frozen=True)
class PrimitiveField:
    label: str
    content: Any


@dataclass(frozen=True)
class NestedField:
    label: str
    card: CardNode


@dataclass(frozen=True)
class CollectionField:
    label: str
    items: list[PrimitiveField | CardNode]


CardContent: TypeAlias = PrimitiveField | NestedField | CollectionField
