from json_presenter import ViewType
from json_presenter.presentation import (
    CardNode,
    CollectionField,
    NestedField,
    PresentationDocument,
    PrimitiveField,
    TableNode,
    TextNode,
    TreeNode,
)


def test_text_node_can_be_created():
    node = TextNode(text="Hello")

    assert node.text == "Hello"


def test_primitive_field_can_be_created():
    field = PrimitiveField(label="Name", content="Alice")

    assert field.label == "Name"
    assert field.content == "Alice"


def test_nested_field_can_be_created():
    nested_card = CardNode(
        title="Profile",
        fields=[
            PrimitiveField(label="Country", content="Japan"),
        ],
    )

    field = NestedField(
        label="Profile",
        card=nested_card,
    )

    assert field.label == "Profile"
    assert field.card.title == "Profile"


def test_collection_field_can_be_created():
    card = CardNode(
        title="Skill",
        fields=[
            PrimitiveField(label="Name", content="Python"),
        ],
    )

    field = CollectionField(
        label="Skills",
        items=[
            PrimitiveField(label="Item 1", content="Python"),
            card,
        ],
    )

    assert field.label == "Skills"
    assert field.items[0].label == "Item 1"
    assert field.items[1].title == "Skill"


def test_card_node_can_be_created():
    node = CardNode(
        title="User",
        fields=[
            PrimitiveField(label="Name", content="Alice"),
            PrimitiveField(label="Age", content=25),
        ],
    )

    assert node.title == "User"
    assert node.fields[0].label == "Name"


def test_table_node_can_be_created():
    node = TableNode(
        headers=["name", "age"],
        rows=[
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 30},
        ],
    )

    assert node.headers == ["name", "age"]
    assert len(node.rows) == 2


def test_tree_node_can_be_created():
    node = TreeNode(
        label="root",
        children=[
            TreeNode(
                label="name: Alice",
                children=[],
            )
        ],
    )

    assert node.label == "root"
    assert len(node.children) == 1


def test_presentation_document_can_be_created():
    document = PresentationDocument(
        view=ViewType.CARDS,
        title="User Data",
        subtitle="1 card",
        description="A card-based view of the JSON object.",
        nodes=[
            CardNode(
                title="User",
                fields=[
                    PrimitiveField(label="Name", content="Alice"),
                ],
            )
        ],
    )

    assert document.view == ViewType.CARDS
    assert document.title == "User Data"
    assert document.subtitle == "1 card"
    assert document.description == "A card-based view of the JSON object."
    assert len(document.nodes) == 1


def test_presentation_document_has_default_metadata():
    document = PresentationDocument(
        view=ViewType.CARDS,
        nodes=[],
    )

    assert document.title == "JSON Presentation"
    assert document.subtitle is None
    assert document.description is None
