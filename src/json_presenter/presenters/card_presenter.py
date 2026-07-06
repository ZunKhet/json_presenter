from typing import Any

from json_presenter.enums import ViewType
from json_presenter.formatting import humanize_label
from json_presenter.presentation import (
    CardNode,
    CollectionField,
    NestedField,
    PresentationDocument,
    PrimitiveField,
)
from json_presenter.presenters.base import BasePresenter


class CardPresenter(BasePresenter):
    """Build a semantic card presentation document."""

    SMALL_PRIMITIVE_LIST_LIMIT = 5

    def build_document(self, data: Any) -> PresentationDocument:
        if self._is_list_of_dicts(data):
            cards = [
                self._build_card(
                    title=self._get_card_title(item, index),
                    data=item,
                )
                for index, item in enumerate(data, start=1)
            ]

            return PresentationDocument(
                view=ViewType.CARDS,
                title="JSON Collection",
                subtitle=f"{len(data)} item{'s' if len(data) != 1 else ''}",
                description="Collection presented as semantic cards.",
                nodes=cards,
            )

        if isinstance(data, dict):
            card = self._build_card(
                title="Properties",
                data=data,
            )

            return PresentationDocument(
                view=ViewType.CARDS,
                title="JSON Object",
                subtitle=f"{len(data)} propert{'y' if len(data) == 1 else 'ies'}",
                description="Object presented as semantic cards.",
                nodes=[card],
            )

        return PresentationDocument(
            view=ViewType.CARDS,
            title="JSON Value",
            subtitle=type(data).__name__,
            description="Single JSON value.",
            nodes=[
                CardNode(
                    title="Value",
                    fields=[
                        PrimitiveField(
                            label="Value",
                            content=data,
                        )
                    ],
                )
            ],
        )

    def _build_card(self, title: str, data: dict[str, Any]) -> CardNode:
        fields = []

        for key, value in data.items():
            label = humanize_label(str(key))

            if isinstance(value, dict):
                fields.append(
                    NestedField(
                        label=label,
                        card=self._build_card(
                            title=label,
                            data=value,
                        ),
                    )
                )
            elif isinstance(value, list):
                fields.append(
                    self._build_collection_field(
                        label=label,
                        values=value,
                    )
                )
            else:
                fields.append(
                    PrimitiveField(
                        label=label,
                        content=value,
                    )
                )

        return CardNode(
            title=title,
            fields=fields,
        )

    def _build_collection_field(
        self,
        label: str,
        values: list[Any],
    ) -> CollectionField:
        items: list[PrimitiveField | CardNode] = []

        for index, item in enumerate(values, start=1):
            if isinstance(item, dict):
                items.append(
                    self._build_card(
                        title=self._get_card_title(item, index),
                        data=item,
                    )
                )
            else:
                items.append(
                    PrimitiveField(
                        label=f"Item {index}",
                        content=item,
                    )
                )

        return CollectionField(
            label=label,
            items=items,
        )

    def _is_list_of_dicts(self, data: Any) -> bool:
        return (
            isinstance(data, list)
            and len(data) > 0
            and all(isinstance(item, dict) for item in data)
        )

    def _get_card_title(self, item: dict[str, Any], index: int) -> str:
        for key in ("name", "title", "label", "id"):
            if key in item:
                return str(item[key])

        return f"Item {index}"
