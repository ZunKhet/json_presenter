from json_presenter import ViewType
from json_presenter.presentation import (
    CardNode,
    CollectionField,
    NestedField,
    PresentationDocument,
    PrimitiveField,
    TableNode,
    TreeNode,
)
from json_presenter.rendering import HtmlRenderer


def test_html_renderer_renders_card_document():
    document = PresentationDocument(
        view=ViewType.CARDS,
        nodes=[
            CardNode(
                title="User",
                fields=[
                    PrimitiveField(label="Name", content="Alice"),
                ],
            )
        ],
    )

    html = HtmlRenderer().render(document)

    assert "jp-card" in html
    assert "Alice" in html


def test_html_renderer_renders_table_document():
    document = PresentationDocument(
        view=ViewType.TABLE,
        nodes=[
            TableNode(
                headers=["name", "age"],
                rows=[
                    {"name": "Alice", "age": 25},
                    {"name": "Bob", "age": 30},
                ],
            )
        ],
    )

    html = HtmlRenderer().render(document)

    assert "<table" in html
    assert "Alice" in html
    assert "Bob" in html


def test_html_renderer_renders_tree_document():
    document = PresentationDocument(
        view=ViewType.TREE,
        nodes=[
            TreeNode(
                label="root",
                children=[
                    TreeNode(
                        label="name: Alice",
                        children=[],
                    )
                ],
            )
        ],
    )

    html = HtmlRenderer().render(document)

    assert "jp-tree" in html
    assert "root" in html
    assert "name: Alice" in html


def test_html_renderer_escapes_html():
    document = PresentationDocument(
        view=ViewType.CARDS,
        nodes=[
            CardNode(
                title="<User>",
                fields=[
                    PrimitiveField(
                        label="Name",
                        content="<script>alert('x')</script>",
                    ),
                ],
            )
        ],
    )

    html = HtmlRenderer().render(document)

    assert "&lt;User&gt;" in html
    assert "&lt;script&gt;" in html
    assert "<script>" not in html


def test_html_renderer_renders_document_metadata():
    document = PresentationDocument(
        view=ViewType.CARDS,
        title="JSON Object",
        subtitle="2 properties",
        description="Object presented as key-value pairs.",
        nodes=[
            CardNode(
                title="Properties",
                fields=[
                    PrimitiveField(label="Name", content="Alice"),
                    PrimitiveField(label="Age", content=25),
                ],
            )
        ],
    )

    html = HtmlRenderer().render(document)

    assert "jp-document-header" in html
    assert "JSON Object" in html
    assert "2 properties" in html
    assert "Object presented as key-value pairs." in html
    assert "jp-content" in html


def test_html_renderer_renders_nested_field_as_disclosure():
    nested_card = CardNode(
        title="Profile",
        fields=[
            PrimitiveField(label="Country", content="Japan"),
        ],
    )

    document = PresentationDocument(
        view=ViewType.CARDS,
        nodes=[
            CardNode(
                title="User",
                fields=[
                    PrimitiveField(label="Name", content="Alice"),
                    NestedField(label="Profile", card=nested_card),
                ],
            )
        ],
    )

    html = HtmlRenderer().render(document)

    assert "<details" in html
    assert "jp-disclosure" in html
    assert "Profile · 1 field" in html
    assert "Profile" in html
    assert "Japan" in html


def test_html_renderer_renders_collection_field_as_disclosure():
    document = PresentationDocument(
        view=ViewType.CARDS,
        nodes=[
            CardNode(
                title="User",
                fields=[
                    CollectionField(
                        label="Skills",
                        items=[
                            PrimitiveField(label="Item 1", content="Python"),
                            PrimitiveField(label="Item 2", content="AI"),
                        ],
                    )
                ],
            )
        ],
    )

    html = HtmlRenderer().render(document)

    assert "<details" in html
    assert "Python" in html
    assert "AI" in html
    assert "Skills · 2 items" in html

    def test_html_renderer_renders_collection_of_cards_summary():
        document = PresentationDocument(
            view=ViewType.CARDS,
            nodes=[
                CardNode(
                    title="Team",
                    fields=[
                        CollectionField(
                            label="Members",
                            items=[
                                CardNode(
                                    title="Alice",
                                    fields=[
                                        PrimitiveField(
                                            label="Role", content="Engineer"),
                                    ],
                                ),
                                CardNode(
                                    title="Bob",
                                    fields=[
                                        PrimitiveField(
                                            label="Role", content="Designer"),
                                    ],
                                ),
                            ],
                        )
                    ],
                )
            ],
        )

        html = HtmlRenderer().render(document)

        assert "Members · 2 cards" in html
